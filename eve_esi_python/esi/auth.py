from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from eve_esi_python.esi_client.scope_manager import EsiScopeManager


class EsiToken(BaseModel):
    access_token: Optional[str] = None
    expiry: Optional[datetime] = None
    token_type: str = "Bearer"
    refresh_token: Optional[str] = None


class EsiAuthManager:
    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope_manager: EsiScopeManager = EsiScopeManager(),
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope_manager = scope_manager

    # this should validate init params or whenever params change so we never have to do it again? Do we even need this?
    def _validate_init_params(self):
        pass

    def auth_uri(self):
        pass

    def auth(self):
        pass

    def refresh(self):
        pass

    @classmethod
    def is_token_expired(cls):
        pass


auth_manager = EsiAuthManager()

# Usage
auth_manager = EsiAuthManager()
auth_uri = (
    auth_manager.auth_uri
)  # property that dynamically changes based on changes to the auth_manager itself?
token_info = auth_manager.auth()
token_info = auth_manager.refresh()

# do we need to add other functions?
# this auth manager will be used in the EsiClient
# EsiToken is based on EveTokenResponse, which is what we get when getting a new access token or refreshing tokens. The only difference is expiry, which we calculate based on the expires_in we get from the response.

# We see that esipy is using things like sessions and jwk and also implements PKCE, we definitely need that as well
