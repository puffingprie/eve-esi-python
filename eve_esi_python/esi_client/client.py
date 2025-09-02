"""
eve-esi-python

ESI Client
"""  # noqa: E501

import base64
import secrets
import urllib.parse
from datetime import datetime
from pydantic import BaseModel

from eve_esi_python.api_client import ApiClient
from eve_esi_python.configuration import Configuration
from eve_esi_python.api import CharacterApi

# from eve_esi_python.api.character_api import CharacterApi
from eve_esi_python.esi_client.constants import (
    EVE_SSO_AUTHORIZE_URL,
    EVE_SSO_TOKEN_URL,
    ESI_SCOPES,
    EVE_CLIENT_ID,
    EVE_CLIENT_SECRET,
)


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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_agent = "eve-esi-python/1.0.0"
        self.host = "https://esi.evetech.net/latest"


class EsiClient(ApiClient):
    def __init__(
        self,
        configuration: EsiClientConfiguration | None = EsiClientConfiguration(),
        user_agent="eve-esi-python/0.1.0",  # or eve-esi-client/version/python
    ):
        super().__init__(configuration=configuration)
        self.user_agent = user_agent


def generate_auth_url(
    client_id: str = EVE_CLIENT_ID,
    redirect_uri: str = "http://localhost",
    scopes: list[str] | None = None,
) -> tuple[str, str]:
    """Generate EVE SSO authorization URL for OAuth2 flow"""
    if scopes is None:
        scopes = [ESI_SCOPES["character_blueprints"]]

    state = secrets.token_urlsafe(32)

    params = {
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "scope": " ".join(scopes),
        "state": state,
    }

    auth_url = f"{EVE_SSO_AUTHORIZE_URL}?{urllib.parse.urlencode(params)}"
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
        "POST", EVE_SSO_TOKEN_URL, header_params=headers, post_params=post_params
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
        "POST", EVE_SSO_TOKEN_URL, header_params=headers, post_params=post_params
    )

    if response.status != 200:
        raise Exception(f"Token refresh failed: {response.status} - {response.read()}")

    try:
        return EveTokenResponse.model_validate_json(response.read())
    except Exception as e:
        raise e


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
