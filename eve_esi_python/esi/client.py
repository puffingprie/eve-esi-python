"""
eve-esi-python

ESI Client
"""  # noqa: E501

import requests
import base64
import secrets
import urllib.parse
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Dict, List, Optional, TypedDict, Tuple, Union

import jwt

from eve_esi_python.api_client import ApiClient
from eve_esi_python.esi_client.scope_manager import EsiScopeManager
from eve_esi_python.configuration import ServerVariablesT
from eve_esi_python.configuration import Configuration
from eve_esi_python.api import CharacterApi

# from eve_esi_python.api.character_api import CharacterApi
from eve_esi_python.esi_client.constants import (
    ESI_SSO_ENDPOINTS_URL_DEFAULT,
    ESI_SSO_AUTHORIZE_URL,
    ESI_SSO_TOKEN_URL,
    EVE_CLIENT_ID,
    EVE_CLIENT_SECRET,
)


class EsiJwk(BaseModel):
    model_config = ConfigDict(extra="allow")

    alg: str
    kid: str  # key id


class EsiJwkResponse(BaseModel):
    keys: List[EsiJwk]
    SkipUnresolvedJsonWebKeys: bool


class EsiSSOEndpointsURLResponse(BaseModel):
    issuer: str
    authorization_endpoint: str
    token_endpoint: str
    response_types_supported: List[str]
    jwks_uri: str
    revocation_endpoint: str
    subject_types_supported: List[str]
    revocation_endpoint_auth_methods_supported: List[str]
    token_endpoint_auth_methods_supported: List[str]
    id_token_signing_alg_values_supported: List[str]
    token_endpoint_auth_signing_alg_values_supported: List[str]
    code_challenge_methods_supported: List[str]


class EveTokenResponse(BaseModel):
    """EVE SSO OAuth2 token response model"""

    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str

    class Config:
        """Pydantic config"""

        extra = "allow"  # Allow additional fields from EVE


class EsiClientConfiguration(Configuration):
    def __init__(
        self,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_index: Optional[int] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_index: Optional[Dict[int, int]] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ignore_operation_servers: bool = False,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ):
        super().__init__(
            host=host or "https://esi.evetech.net/latest",
            api_key=api_key,
            api_key_prefix=api_key_prefix,
            username=username,
            password=password,
            access_token=access_token,
            server_index=server_index,
            server_variables=server_variables,
            server_operation_index=server_operation_index,
            server_operation_variables=server_operation_variables,
            ignore_operation_servers=ignore_operation_servers,
            ssl_ca_cert=ssl_ca_cert,
            retries=retries,
            ca_cert_data=ca_cert_data,
            debug=debug,
        )


class EsiClient(ApiClient):
    def __init__(
        self,
        configuration: Optional[EsiClientConfiguration] = None,
        user_agent: Optional[str] = None,
    ):
        super().__init__(configuration=configuration or EsiClientConfiguration())
        self.user_agent = user_agent or "eve-esi-python/0.1.0"


# We can make an EsiClient, whereby the user only needs to pass the following things in:
# Client ID (Optional, if the user wants to access private data)
# Client Secret (Optional, if the user wants to access private data)
# Redirect URI (Optional, if the user wants to access private data)
# Scopes, using the EsiScopeManager pydantic class (Optional, if the user wants to access private data)

# Usage should be:
# 1. Create EsiClient config
# 2. Create EsiClient with config
# 3. Create specific api instance
# 4. Call endpoint with created api instance.
# *This means that our EsiClient needs to be able to handle authentication automatically if the user provides a client id, client secret, redirect uri and scopes. (Question: do we need all of these? What if we're doing PKCE?)...not sure, lets focus on non-PKCE oauth flow for now.


def generate_auth_url(
    client_id: str = EVE_CLIENT_ID,
    redirect_uri: str = "http://localhost",
    scopes: Optional[EsiScopeManager] = None,
) -> tuple[str, str]:
    """Generate EVE SSO authorization URL for OAuth2 flow"""
    state = secrets.token_urlsafe(32)

    params = {
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "scope": scopes.to_oauth_string() if scopes else "",
        "state": state,
    }

    auth_url = f"{ESI_SSO_AUTHORIZE_URL}?{urllib.parse.urlencode(params)}"
    return auth_url, state


def exchange_code_for_tokens(
    client: EsiClient,
    code: str,
    client_id: str = EVE_CLIENT_ID,
    client_secret: str = EVE_CLIENT_SECRET,
) -> EveTokenResponse:
    """Exchange authorization code for access and refresh tokens"""
    # Create Basic Auth header (using urlsafe_b64encode like EVE docs)
    auth_string = f"{client_id}:{client_secret}"
    auth_b64 = base64.urlsafe_b64encode(auth_string.encode("utf-8")).decode("utf-8")

    # Prepare token request
    # http = urllib3.PoolManager()

    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    post_params = {
        "grant_type": "authorization_code",
        "code": code,
    }

    # Make request to token endpoint
    # response = http.request("POST", EVE_SSO_TOKEN_URL, headers=headers, body=body_data)
    # response = client.rest_client.request(
    #     method="POST", url=EVE_SSO_TOKEN_URL, headers=headers, post_params=post_params
    # )
    response = client.call_api(
        "POST", ESI_SSO_TOKEN_URL, header_params=headers, post_params=post_params
    )

    if response.status != 200:
        raise Exception(f"Token exchange failed: {response.status} - {response.read()}")

    try:
        return EveTokenResponse.model_validate_json(response.read())
    except Exception as e:
        raise e


def refresh_access_token(
    client: EsiClient,
    refresh_token: str,
    client_id: str = EVE_CLIENT_ID,
    client_secret: str = EVE_CLIENT_SECRET,
) -> EveTokenResponse:
    """Use refresh token to get new access token"""
    # Create Basic Auth header
    auth_string = f"{client_id}:{client_secret}"
    auth_b64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    # Prepare refresh request
    # http = urllib3.PoolManager()

    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # data = {
    #     "grant_type": "refresh_token",
    #     "refresh_token": refresh_token,
    # }
    post_params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    # Make request to token endpoint
    # response = http.request("POST", EVE_SSO_TOKEN_URL, headers=headers, body=body_data)
    response = client.call_api(
        "POST", ESI_SSO_TOKEN_URL, header_params=headers, post_params=post_params
    )

    if response.status != 200:
        raise Exception(f"Token refresh failed: {response.status} - {response.read()}")

    try:
        return EveTokenResponse.model_validate_json(response.read())
    except Exception as e:
        raise e


def fetch_jwks_metadata():
    res = requests.get(ESI_SSO_ENDPOINTS_URL_DEFAULT)
    res.raise_for_status()
    endpoints_url = EsiSSOEndpointsURLResponse.model_validate_json(res.json())
    jwk_res = EsiJwkResponse.model_validate_json(
        requests.get(endpoints_url.jwks_uri).json()
    )
    return jwk_res


def verify_token(access_token: str, key_id: str = "JWT-Signature-Key"):
    jwt.decode(access_token, key_id)


def get_char_blueprints(access_token: str, character_id: int):
    """Get character blueprints using access token"""
    # Create authenticated client
    config = EsiClientConfiguration(access_token=access_token)
    client = EsiClient(configuration=config)

    # Call the API
    api_instance = CharacterApi(client)
    x_compatibility_date = datetime(2025, 8, 26)

    try:
        res = api_instance.get_characters_character_id_blueprints(
            character_id, x_compatibility_date
        )

        return res

    except Exception as e:
        raise e
