# -*- encoding: utf-8 -*-
"""
EsiPy Security definition for EVE Online SSO authentication.

This module provides OAuth2 authentication handling for EVE Online's ESI API,
supporting both confidential (secret key) and public (PKCE) client flows.
"""

from __future__ import annotations

import base64
import logging
import time
import warnings
from dataclasses import dataclass
from typing import Dict, List, Optional, Union
from urllib.parse import quote

import requests
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError, JWTClaimsError

from .events import AFTER_TOKEN_REFRESH
from .exceptions import APIException
from .utils import generate_code_challenge

LOGGER = logging.getLogger(__name__)

# Constants
DEFAULT_SSO_ENDPOINTS_URL = (
    "https://login.eveonline.com/.well-known/oauth-authorization-server"
)
DEFAULT_USER_AGENT = "EsiPy/Security/ - https://github.com/Kyria/EsiPy"
DEFAULT_SECURITY_NAME = "evesso"
DEFAULT_AUDIENCE = "EVE Online"
DEFAULT_JWT_KID = "JWT-Signature-Key"

# Request timeout settings
REQUEST_TIMEOUT = (10, 30)  # (connect_timeout, read_timeout)


@dataclass
class TokenInfo:
    """Container for OAuth2 token information."""

    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_expiry: Optional[int] = None
    token_type: str = "Bearer"


class EsiSecurityError(Exception):
    """Base exception for ESI Security operations."""

    pass


class TokenExpiredError(EsiSecurityError):
    """Raised when a token has expired and cannot be refreshed."""

    pass


class InvalidConfigurationError(EsiSecurityError):
    """Raised when the security configuration is invalid."""

    pass


class EsiSecurity:
    """
    OAuth2 security handler for EVE Online ESI API.

    Supports both confidential clients (with secret key) and public clients (PKCE).
    Provides automatic token refresh and comprehensive error handling.
    """

    def __init__(
        self,
        redirect_uri: str,
        client_id: str,
        *,
        secret_key: Optional[str] = None,
        code_verifier: Optional[str] = None,
        token_identifier: Optional[str] = None,
        security_name: str = DEFAULT_SECURITY_NAME,
        headers: Optional[Dict[str, str]] = None,
        signal_token_updated=None,
        sso_endpoints: Optional[Dict[str, str]] = None,
        sso_endpoints_url: str = DEFAULT_SSO_ENDPOINTS_URL,
        jwks_key: Optional[Dict] = None,
        request_timeout: tuple = REQUEST_TIMEOUT,
    ):
        """
        Initialize the ESI Security Object.

        Args:
            redirect_uri: URI to redirect user after SSO login
            client_id: OAuth2 client ID
            secret_key: OAuth2 secret key (for confidential clients)
            code_verifier: PKCE code verifier (for public clients)
            token_identifier: Optional identifier for token callbacks
            security_name: Name of security definition in API spec
            headers: Additional HTTP headers for requests
            signal_token_updated: Signal to emit on token refresh
            sso_endpoints: Pre-fetched SSO endpoint configuration
            sso_endpoints_url: URL to fetch SSO endpoints from
            jwks_key: Pre-fetched JWKS key data
            request_timeout: Timeout settings for HTTP requests

        Raises:
            InvalidConfigurationError: If configuration is invalid
        """
        self._validate_init_params(
            redirect_uri, client_id, secret_key, code_verifier, sso_endpoints_url
        )

        self.redirect_uri = redirect_uri
        self.client_id = client_id
        self.secret_key = secret_key
        self.code_verifier = code_verifier
        self.security_name = security_name
        self.token_identifier = token_identifier
        self.request_timeout = request_timeout

        # Initialize token storage
        self._token_info = TokenInfo()

        # Setup HTTP session
        self._session = self._create_session(headers)

        # Load SSO endpoints
        self._load_sso_endpoints(sso_endpoints, sso_endpoints_url)

        # Load JWKS keys
        self._load_jwks_keys(jwks_key)

        # Setup event signal
        self.signal_token_updated = signal_token_updated or AFTER_TOKEN_REFRESH

    @staticmethod
    def _validate_init_params(
        redirect_uri: str,
        client_id: str,
        secret_key: Optional[str],
        code_verifier: Optional[str],
        sso_endpoints_url: str,
    ) -> None:
        """Validate initialization parameters."""
        if not redirect_uri or not redirect_uri.strip():
            raise InvalidConfigurationError("redirect_uri cannot be empty")

        if not client_id or not client_id.strip():
            raise InvalidConfigurationError("client_id cannot be empty")

        if not sso_endpoints_url or not sso_endpoints_url.strip():
            raise InvalidConfigurationError("sso_endpoints_url cannot be empty")

        if secret_key is None and code_verifier is None:
            raise InvalidConfigurationError(
                "Either secret_key or code_verifier must be provided"
            )

        if secret_key is not None and code_verifier is not None:
            raise InvalidConfigurationError(
                "Cannot use both secret_key and code_verifier simultaneously"
            )

    def _create_session(self, headers: Optional[Dict[str, str]]) -> requests.Session:
        """Create and configure HTTP session."""
        session = requests.Session()

        # Set default headers
        default_headers = {
            "Accept": "application/json",
            "User-Agent": f"{DEFAULT_USER_AGENT} - ClientID: {self.client_id}",
        }

        # Warn about missing User-Agent if not provided
        if headers and "User-Agent" not in headers:
            warning_msg = (
                "Defining a 'User-Agent' header is a good practice and allows "
                "CCP to contact you if required. Add it to headers parameter."
            )
            LOGGER.warning(warning_msg)
            warnings.warn(warning_msg, UserWarning, stacklevel=3)

        session.headers.update(default_headers)
        if headers:
            session.headers.update(headers)

        return session

    def _load_sso_endpoints(
        self,
        sso_endpoints: Optional[Dict[str, str]],
        sso_endpoints_url: str,
    ) -> None:
        """Load SSO endpoints from provided dict or fetch from URL."""
        if sso_endpoints and isinstance(sso_endpoints, dict):
            endpoints = sso_endpoints
        else:
            try:
                response = self._session.get(
                    sso_endpoints_url, timeout=self.request_timeout
                )
                response.raise_for_status()
                endpoints = response.json()
            except requests.RequestException as e:
                raise EsiSecurityError(f"Failed to fetch SSO endpoints: {e}") from e
            except ValueError as e:
                raise EsiSecurityError(
                    f"Invalid JSON in SSO endpoints response: {e}"
                ) from e

        # Validate required endpoints
        required_endpoints = [
            "issuer",
            "authorization_endpoint",
            "token_endpoint",
            "revocation_endpoint",
            "jwks_uri",
        ]
        missing = [ep for ep in required_endpoints if ep not in endpoints]
        if missing:
            raise EsiSecurityError(f"Missing required SSO endpoints: {missing}")

        self.oauth_issuer = endpoints["issuer"]
        self.oauth_authorize = endpoints["authorization_endpoint"]
        self.oauth_token = endpoints["token_endpoint"]
        self.oauth_revoke = endpoints["revocation_endpoint"]
        self._jwks_uri = endpoints["jwks_uri"]

    def _load_jwks_keys(self, jwks_key: Optional[Dict]) -> None:
        """Load JWKS keys from provided data or fetch from URI."""
        if jwks_key:
            keys_data = jwks_key
        else:
            try:
                response = self._session.get(
                    self._jwks_uri, timeout=self.request_timeout
                )
                response.raise_for_status()
                keys_data = response.json()
            except requests.RequestException as e:
                raise EsiSecurityError(f"Failed to fetch JWKS keys: {e}") from e
            except ValueError as e:
                raise EsiSecurityError(f"Invalid JSON in JWKS response: {e}") from e

        if "keys" in keys_data:
            self.jwks_key_set = {key["kid"]: key for key in keys_data["keys"]}
            self.jwks_key = None
        else:
            self.jwks_key_set = None
            self.jwks_key = keys_data

    def _get_basic_auth_header(self) -> Dict[str, str]:
        """Generate Basic Authentication header for confidential clients."""
        if self.secret_key is None:
            return {}

        credentials = f"{self.client_id}:{self.secret_key}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        return {"Authorization": f"Basic {encoded_credentials}"}

    def _prepare_token_request(
        self, params: Dict[str, str], url: Optional[str] = None
    ) -> Dict[str, Union[str, Dict]]:
        """Prepare token request parameters."""
        if self.secret_key is None:
            # Public client (PKCE)
            params.update(
                {
                    "code_verifier": self.code_verifier,
                    "client_id": self.client_id,
                }
            )

        return {
            "headers": self._get_basic_auth_header(),
            "data": params,
            "url": url or self.oauth_token,
            "timeout": self.request_timeout,
        }

    def get_auth_uri(
        self, state: str, scopes: Optional[List[str]] = None, implicit: bool = False
    ) -> str:
        """
        Generate authorization URI for OAuth2 flow.

        Args:
            state: State parameter for CSRF protection
            scopes: List of OAuth2 scopes to request
            implicit: Whether to use implicit flow

        Returns:
            Authorization URL for user to visit

        Raises:
            InvalidConfigurationError: If state is empty
        """
        if not state or not state.strip():
            raise InvalidConfigurationError("state must be a non-empty string")

        response_type = "token" if implicit else "code"
        scope_param = f"&scope={'+'.join(scopes)}" if scopes else ""

        auth_uri = (
            f"{self.oauth_authorize}"
            f"?response_type={response_type}"
            f"&redirect_uri={quote(self.redirect_uri, safe='')}"
            f"&client_id={self.client_id}"
            f"{scope_param}"
            f"&state={state}"
        )

        # Add PKCE challenge for public clients
        if self.secret_key is None and not implicit:
            code_challenge = generate_code_challenge(self.code_verifier)
            auth_uri += f"&code_challenge_method=S256&code_challenge={code_challenge}"

        return auth_uri

    def auth(self, code: str) -> Dict:
        """
        Exchange authorization code for access token.

        Args:
            code: Authorization code from OAuth2 callback

        Returns:
            Token response from authorization server

        Raises:
            APIException: If token request fails
        """
        params = {
            "grant_type": "authorization_code",
            "code": code,
        }

        request_data = self._prepare_token_request(params)

        try:
            response = self._session.post(**request_data)
            response.raise_for_status()
        except requests.RequestException as e:
            raise APIException(
                request_data["url"],
                getattr(e.response, "status_code", 0),
                response=getattr(e.response, "content", str(e)),
                request_param=request_data,
                response_header=getattr(e.response, "headers", {}),
            ) from e

        try:
            json_response = response.json()
        except ValueError as e:
            raise APIException(
                request_data["url"],
                response.status_code,
                response=f"Invalid JSON response: {e}",
                request_param=request_data,
                response_header=response.headers,
            ) from e

        self.update_token(json_response)
        return json_response

    def refresh(self, scope_list: Optional[List[str]] = None) -> Dict:
        """
        Refresh access token using refresh token.

        Args:
            scope_list: Optional list of scopes to request

        Returns:
            Token response from authorization server

        Raises:
            TokenExpiredError: If no refresh token is available
            APIException: If refresh request fails
        """
        if not self._token_info.refresh_token:
            raise TokenExpiredError("No refresh token available")

        params = {
            "grant_type": "refresh_token",
            "refresh_token": self._token_info.refresh_token,
        }

        if scope_list:
            if not isinstance(scope_list, list):
                raise ValueError("scope_list must be a list of strings")
            params["scope"] = "+".join(scope_list)

        request_data = self._prepare_token_request(params)

        try:
            response = self._session.post(**request_data)
            response.raise_for_status()
        except requests.RequestException as e:
            raise APIException(
                request_data["url"],
                getattr(e.response, "status_code", 0),
                response=getattr(e.response, "content", str(e)),
                request_param=request_data,
                response_header=getattr(e.response, "headers", {}),
            ) from e

        try:
            json_response = response.json()
        except ValueError as e:
            raise APIException(
                request_data["url"],
                response.status_code,
                response=f"Invalid JSON response: {e}",
                request_param=request_data,
                response_header=response.headers,
            ) from e

        self.update_token(json_response)
        return json_response

    def update_token(self, response_json: Dict, **kwargs) -> None:
        """
        Update token information from OAuth2 response.

        Args:
            response_json: Token response from authorization server
            **kwargs: Additional parameters (e.g., token_identifier)
        """
        self.token_identifier = kwargs.get("token_identifier", self.token_identifier)

        self._token_info.access_token = response_json["access_token"]
        self._token_info.token_expiry = int(time.time()) + response_json["expires_in"]

        if "refresh_token" in response_json:
            self._token_info.refresh_token = response_json["refresh_token"]

        if "token_type" in response_json:
            self._token_info.token_type = response_json["token_type"]

    def is_token_expired(self, offset: int = 0) -> bool:
        """
        Check if access token is expired.

        Args:
            offset: Time offset in seconds (positive = expire sooner)

        Returns:
            True if token is expired or missing
        """
        if self._token_info.token_expiry is None:
            return True
        return int(time.time()) >= (self._token_info.token_expiry - offset)

    def revoke(self) -> None:
        """
        Revoke current tokens and clear stored credentials.

        Note: Currently not fully supported with JWT tokens.
        """
        if not self._token_info.refresh_token and not self._token_info.access_token:
            raise TokenExpiredError("No access/refresh tokens available")

        token_to_revoke = (
            self._token_info.refresh_token or self._token_info.access_token
        )
        token_type = (
            "refresh_token" if self._token_info.refresh_token else "access_token"
        )

        params = {
            "token_type_hint": token_type,
            "token": token_to_revoke,
        }

        request_data = self._prepare_token_request(params, self.oauth_revoke)

        try:
            self._session.post(**request_data)
        except requests.RequestException as e:
            LOGGER.warning("Token revocation failed: %s", e)
        finally:
            # Clear tokens regardless of revocation result
            self._clear_tokens()

    def _clear_tokens(self) -> None:
        """Clear all stored token information."""
        self._token_info = TokenInfo()

    def verify(
        self, kid: str = DEFAULT_JWT_KID, options: Optional[Dict] = None
    ) -> Dict:
        """
        Verify and decode JWT access token.

        Args:
            kid: Key ID for JWT verification
            options: JWT decoding options

        Returns:
            Decoded JWT payload

        Raises:
            TokenExpiredError: If no access token is available
            JWTError: If token verification fails
        """
        if not self._token_info.access_token:
            raise TokenExpiredError("No access token available")

        if self.jwks_key_set is None:
            key = self.jwks_key
        else:
            if kid not in self.jwks_key_set:
                raise JWTError(f"Key ID '{kid}' not found in JWKS key set")
            key = self.jwks_key_set[kid]

        try:
            return jwt.decode(
                self._token_info.access_token,
                key,
                issuer=self.oauth_issuer,
                options=options or {},
                audience=DEFAULT_AUDIENCE,
            )
        except (JWTError, ExpiredSignatureError, JWTClaimsError) as e:
            LOGGER.error("JWT verification failed: %s", e)
            raise

    # Properties for backward compatibility
    @property
    def access_token(self) -> Optional[str]:
        """Get current access token."""
        return self._token_info.access_token

    @access_token.setter
    def access_token(self, value: Optional[str]) -> None:
        """Set access token."""
        self._token_info.access_token = value

    @property
    def refresh_token(self) -> Optional[str]:
        """Get current refresh token."""
        return self._token_info.refresh_token

    @refresh_token.setter
    def refresh_token(self, value: Optional[str]) -> None:
        """Set refresh token."""
        self._token_info.refresh_token = value

    @property
    def token_expiry(self) -> Optional[int]:
        """Get token expiry timestamp."""
        return self._token_info.token_expiry

    @token_expiry.setter
    def token_expiry(self, value: Optional[int]) -> None:
        """Set token expiry timestamp."""
        self._token_info.token_expiry = value

    def __call__(self, request):
        """
        Apply authentication to pyswagger request.

        Args:
            request: pyswagger request object

        Returns:
            Request with authentication headers applied
        """
        if not request._security:
            return request

        # Auto-refresh expired tokens
        if self.is_token_expired():
            try:
                json_response = self.refresh()
                self.signal_token_updated.send(
                    token_identifier=self.token_identifier, **json_response
                )
            except (TokenExpiredError, APIException) as e:
                LOGGER.error("Failed to refresh token: %s", e)
                # Continue with expired token - let the API handle it

        # Apply authorization header
        for security in request._security:
            if self.security_name not in security:
                LOGGER.warning("Missing security: %s", list(security.keys()))
                continue

            if self._token_info.access_token:
                auth_header = (
                    f"{self._token_info.token_type} {self._token_info.access_token}"
                )
                request._p["header"]["Authorization"] = auth_header

        return request

    def __repr__(self) -> str:
        """String representation of security object."""
        return (
            f"EsiSecurity(client_id='{self.client_id}', "
            f"has_token={bool(self._token_info.access_token)}, "
            f"expired={self.is_token_expired()})"
        )
