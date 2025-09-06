"""
eve-esi-python

EVE SSO helper (OAuth 2.0 + JWT/JWKS) using urllib3.
- Discovery via well-known
- Auth Code (confidential) and PKCE (public)
- JWT verification via JWKS (no external HTTP libs)
- Refresh, revoke, state check, scope checks
"""

from __future__ import annotations

import base64
import hashlib
import json
import time
import urllib.parse
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import jwt
import urllib3
from jwt.algorithms import RSAAlgorithm

from eve_esi_python.esi.sso.constants import (
    EVE_SSO_ENDPOINTS_URL_DEFAULT,
    EVE_SSO_ISSUER_ENDPOINT_DEFAULT,
    EVE_SSO_AUTH_ENDPOINT_DEFAULT,
    EVE_SSO_TOKEN_ENDPOINT_DEFAULT,
    EVE_SSO_JWKS_URI_DEFAULT,
    EVE_SSO_REVOCATION_ENDPOINT_DEFAULT,
)
from eve_esi_python.esi.sso.constants import EsiScope
from eve_esi_python.esi.sso.scope_manager import EsiScopeManager


# -----------------------------
# Lightweight models/utilities
# -----------------------------


@dataclass
class TokenSet:
    access_token: str
    refresh_token: Optional[str]
    token_type: str
    # Unix timestamp when the access token expires
    expires_at: int

    @classmethod
    def from_token_response(cls, data: Dict[str, Union[str, int]]) -> "TokenSet":
        now = int(time.time())
        expires_in = int(data.get("expires_in", 0))
        return cls(
            access_token=str(data["access_token"]),
            refresh_token=str(data.get("refresh_token"))
            if data.get("refresh_token")
            else None,
            token_type=str(data.get("token_type", "Bearer")),
            expires_at=now + expires_in,
        )


def _b64url_no_pad(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode().rstrip("=")


def _basic_auth_header_value(client_id: str, client_secret: str) -> str:
    # Standard base64 for HTTP Basic (NOT urlsafe)
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return f"Basic {base64.b64encode(raw).decode('utf-8')}"


# -----------------------------
# EveSSO (urllib3)
# -----------------------------


class EveSSO:
    def __init__(
        self,
        client_id: str,
        client_secret: Optional[str] = None,  # None for PKCE/public clients
        redirect_uri: Optional[str] = None,
        issuer: str = EVE_SSO_ISSUER_ENDPOINT_DEFAULT,
        metadata_url: str = EVE_SSO_ENDPOINTS_URL_DEFAULT,
        metadata_ttl: int = 300,
        jwks_ttl: int = 300,
        expected_audience_extra: str = "EVE Online",
        http: Optional[urllib3.PoolManager] = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.issuer = issuer
        self.metadata_url = metadata_url
        self.metadata_ttl = metadata_ttl
        self.jwks_ttl = jwks_ttl
        self.expected_audience_extra = expected_audience_extra

        # HTTP client
        self.http = http or urllib3.PoolManager()

        # Caches
        self._metadata: Optional[Dict[str, str]] = None
        self._metadata_expires_at: int = 0

        self._jwks: Optional[Dict[str, Dict]] = None
        self._jwks_expires_at: int = 0

    def discover_metadata(self, force: bool = False) -> Dict[str, str]:
        now = int(time.time())
        if not force and self._metadata and now < self._metadata_expires_at:
            return self._metadata

        try:
            m = self._http_get_json(self.metadata_url)
            self._metadata = {
                "issuer": str(m.get("issuer", self.issuer)),
                "authorization_endpoint": str(
                    m.get("authorization_endpoint", EVE_SSO_AUTH_ENDPOINT_DEFAULT)
                ),
                "token_endpoint": str(
                    m.get("token_endpoint", EVE_SSO_TOKEN_ENDPOINT_DEFAULT)
                ),
                "jwks_uri": str(m.get("jwks_uri", EVE_SSO_JWKS_URI_DEFAULT)),
                "revocation_endpoint": str(
                    m.get("revocation_endpoint", EVE_SSO_REVOCATION_ENDPOINT_DEFAULT)
                ),
            }
        except Exception:
            # Fallback to known defaults if discovery fails
            self._metadata = {
                "issuer": self.issuer,
                "authorization_endpoint": EVE_SSO_AUTH_ENDPOINT_DEFAULT,
                "token_endpoint": EVE_SSO_TOKEN_ENDPOINT_DEFAULT,
                "jwks_uri": EVE_SSO_JWKS_URI_DEFAULT,
                "revocation_endpoint": EVE_SSO_REVOCATION_ENDPOINT_DEFAULT,
            }

        self._metadata_expires_at = now + self.metadata_ttl
        return self._metadata

    def fetch_jwks(self, force: bool = False) -> Dict[str, Dict]:
        now = int(time.time())
        if not force and self._jwks and now < self._jwks_expires_at:
            return self._jwks

        metadata = self.discover_metadata()
        jwks_uri = metadata["jwks_uri"]
        data = self._http_get_json(jwks_uri)
        # Index by kid for quick lookup
        keys = data.get("keys", [])
        self._jwks = {k["kid"]: k for k in keys if "kid" in k}
        self._jwks_expires_at = now + self.jwks_ttl
        return self._jwks

    # ---- Authorization URL / PKCE ----

    def generate_pkce(self) -> Tuple[str, str]:
        """
        Returns (code_verifier, code_challenge) using S256.
        """
        verifier = _b64url_no_pad(urllib3.util.generate_random_bytes(32))
        digest = hashlib.sha256(verifier.encode("utf-8")).digest()
        challenge = _b64url_no_pad(digest)
        return verifier, challenge

    def get_authorization_url(
        self,
        scopes: Optional[EsiScopeManager] = None,
        state: Optional[str] = None,
        code_challenge: Optional[str] = None,
        code_challenge_method: Optional[str] = "S256",
        extra_params: Optional[Dict[str, str]] = None,
    ) -> Tuple[str, str]:
        """
        Build the EVE SSO authorization URL.
        Returns (url, state). If state not provided, one is generated.
        Include code_challenge for PKCE flows (public clients).
        """
        if not self.redirect_uri:
            raise ValueError("redirect_uri is required to build auth URL")

        metadata = self.discover_metadata()
        auth_ep = metadata["authorization_endpoint"]

        st = (
            state
            or urllib3.util.make_headers().get("x-request-id")
            or _b64url_no_pad(urllib3.util.generate_random_bytes(12))
        )
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": scopes.to_oauth_string() if scopes else "",
            "state": st,
        }

        if code_challenge:
            params["code_challenge"] = code_challenge
            if code_challenge_method:
                params["code_challenge_method"] = code_challenge_method

        if extra_params:
            params.update(extra_params)

        url = f"{auth_ep}?{urllib.parse.urlencode(params)}"
        return url, st

    # ---- Code exchange / Refresh ----

    def authorize(
        self,
        code: str,
        code_verifier: Optional[str] = None,
        timeout: int = 10,
    ) -> TokenSet:
        """
        Exchange authorization code for access/refresh tokens.
        - Confidential clients: authenticate with client_secret (Basic)
        - Public clients (PKCE): no client_secret; include code_verifier
        """
        metadata = self.discover_metadata()
        token_ep = metadata["token_endpoint"]

        headers: Dict[str, str] = {}
        data: Dict[str, str] = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri or "",
        }

        if self.client_secret:
            headers["Authorization"] = _basic_auth_header_value(
                self.client_id, self.client_secret
            )
        else:
            # Public client: include client_id and PKCE verifier
            data["client_id"] = self.client_id
            if not code_verifier:
                raise ValueError("code_verifier is required for PKCE/public clients")
            data["code_verifier"] = code_verifier

        resp = self._http_post_form(token_ep, data, timeout=timeout, headers=headers)
        return TokenSet.from_token_response(resp)

    def refresh(self, refresh_token: str, timeout: int = 10) -> TokenSet:
        """
        Exchange refresh_token for a new access token (and possibly rotated refresh token).
        """
        metadata = self.discover_metadata()
        token_ep = metadata["token_endpoint"]

        headers: Dict[str, str] = {}
        data: Dict[str, str] = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }

        if self.client_secret:
            headers["Authorization"] = _basic_auth_header_value(
                self.client_id, self.client_secret
            )
        else:
            data["client_id"] = self.client_id

        resp = self._http_post_form(token_ep, data, timeout=timeout, headers=headers)
        return TokenSet.from_token_response(resp)

    # ---- Verification / Claims / Scopes ----

    def _select_jwk_for_token(self, token: str) -> Dict:
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
        alg = header.get("alg")
        if not kid or not alg:
            raise RuntimeError("JWT header missing kid or alg")

        jwks = self.fetch_jwks()
        jwk = jwks.get(kid)
        if not jwk:
            # Attempt a forced refresh once (key rotation)
            jwks = self.fetch_jwks(force=True)
            jwk = jwks.get(kid)
        if not jwk:
            raise RuntimeError(f"No matching JWK for kid={kid}")
        if jwk.get("alg") and jwk["alg"] != alg:
            # Some providers don't set alg in JWKS; tolerate if absent
            pass
        return jwk

    def verify_token(
        self,
        access_token: str,
        require_client_id_aud: bool = True,
    ) -> Dict[str, Union[str, int, List[str]]]:
        """
        Verify JWT signature (via JWKS), issuer, audience, and exp.
        Returns the token claims if valid.
        """
        metadata = self.discover_metadata()
        issuer = metadata["issuer"]

        jwk = self._select_jwk_for_token(access_token)
        public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))

        # Verify signature/issuer/audience (your client_id)
        claims = jwt.decode(
            access_token,
            public_key,
            algorithms=["RS256", "RS384", "RS512"],
            audience=self.client_id if require_client_id_aud else None,
            issuer=issuer,
            options={"require": ["exp", "iss", "aud"]},
        )

        # EVE includes BOTH your client_id and "EVE Online" in aud
        aud = claims.get("aud")
        aud_list = [aud] if isinstance(aud, str) else list(aud or [])
        if self.expected_audience_extra not in aud_list:
            raise RuntimeError("aud claim missing 'EVE Online'")

        sub = str(claims.get("sub", ""))
        if not sub.startswith("EVE:CHARACTER:"):
            raise RuntimeError("unexpected sub format in access token")

        return claims

    def parse_access_token_claims(
        self, access_token: str
    ) -> Dict[str, Union[str, int, List[str]]]:
        """
        Decode claims without verifying signature (for quick inspection).
        Only use after verify_token() in security-sensitive paths.
        """
        return jwt.decode(
            access_token, options={"verify_signature": False, "verify_exp": False}
        )

    def has_required_scopes(
        self,
        claims_or_token: Union[Dict[str, Union[str, int, List[str]]], str],
        required_scopes: EsiScopeManager,
    ) -> bool:
        """
        Check scp array contains all required scopes.
        Accepts either verified claims or a raw token (decoded locally).
        """
        if isinstance(claims_or_token, str):
            claims = self.parse_access_token_claims(claims_or_token)
        else:
            claims = claims_or_token

        scp = claims.get("scp", [])
        if isinstance(scp, str):
            granted = set(scp.split())
        else:
            granted = set(scp or [])

        needed = set(required_scopes.get_scope_strings())
        return needed.issubset(granted)

    def is_access_token_expired(
        self, claims_or_token: Union[Dict, str], skew_seconds: int = 60
    ) -> bool:
        """
        Quick expiry check with small skew. If passing a raw token,
        it decodes without verifying signature (safe for local exp check).
        """
        if isinstance(claims_or_token, str):
            claims = self.parse_access_token_claims(claims_or_token)
        else:
            claims = claims_or_token

        exp = int(claims.get("exp", 0))
        now = int(time.time())
        return now >= (exp - max(0, skew_seconds))

    def ensure_fresh_access_token(
        self,
        token_set: TokenSet,
        skew_seconds: int = 60,
        timeout: int = 10,
    ) -> TokenSet:
        """
        Ensure the token set has a usable, non-expired access token.
        Refreshes if near/at expiry. Returns possibly updated token set.
        """
        claims = self.parse_access_token_claims(token_set.access_token)
        if not self.is_access_token_expired(claims, skew_seconds=skew_seconds):
            return token_set

        if not token_set.refresh_token:
            raise RuntimeError("access token expired and no refresh token present")

        refreshed = self.refresh(refresh_token=token_set.refresh_token, timeout=timeout)
        # Verify the new access token before returning
        self.verify_token(refreshed.access_token)

        return refreshed

    # ---- Revocation / State / Helpers ----

    def revoke_token(
        self, token: str, token_type_hint: str = "refresh_token", timeout: int = 10
    ) -> None:
        """
        Revoke a refresh token (recommended) or access token (usually unneeded).
        EVE responds 200 OK whether or not the token existed.
        """
        metadata = self.discover_metadata()
        revoke_ep = metadata["revocation_endpoint"]

        headers: Dict[str, str] = {}
        data: Dict[str, str] = {"token": token, "token_type_hint": token_type_hint}

        if self.client_secret:
            headers["Authorization"] = _basic_auth_header_value(
                self.client_id, self.client_secret
            )
        else:
            # Public clients typically cannot authenticate here; prefer revoking
            # via a backend that holds the client secret, or user self-service.
            data["client_id"] = self.client_id

        # RFC 7009 requires application/x-www-form-urlencoded
        self._http_post_form(revoke_ep, data, timeout=timeout, headers=headers)

    @staticmethod
    def validate_state(state_sent: str, state_returned: str) -> bool:
        """
        Compare returned state against what was issued to prevent CSRF.
        """
        return bool(state_sent) and state_sent == state_returned

    @classmethod
    def extract_character_id(cls, claims_or_token: Union[Dict, str]) -> int:
        """
        Return integer character ID from sub (EVE:CHARACTER:<id>).
        Accepts verified claims or a raw token (decodes locally).
        """
        if isinstance(claims_or_token, str):
            claims = jwt.decode(
                claims_or_token,
                options={"verify_signature": False, "verify_exp": False},
            )
        else:
            claims = claims_or_token

        sub = str(claims.get("sub", ""))
        prefix = "EVE:CHARACTER:"
        if not sub.startswith(prefix):
            raise ValueError("unexpected sub format; cannot extract character id")
        return int(sub[len(prefix) :])
