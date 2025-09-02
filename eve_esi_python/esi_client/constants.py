"""
eve-esi-python

Constants
"""

UNAUTHORIZED_STATUS_CODE = 401
MAX_REQUESTS_PER_SECOND = 100.0
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5

# EVE SSO OAuth2 URLs
EVE_SSO_BASE_URL = "https://login.eveonline.com"
EVE_SSO_AUTHORIZE_URL = f"{EVE_SSO_BASE_URL}/v2/oauth/authorize"
EVE_SSO_TOKEN_URL = f"{EVE_SSO_BASE_URL}/v2/oauth/token"
EVE_SSO_VERIFY_URL = f"{EVE_SSO_BASE_URL}/oauth/verify"

# Common ESI scopes
ESI_SCOPES = {
    "character_blueprints": "esi-characters.read_blueprints.v1",
    "character_assets": "esi-assets.read_assets.v1",
    "character_skills": "esi-skills.read_skills.v1",
    "character_location": "esi-location.read_location.v1",
}

# Yes, I put my secrets out for everyone to see. Fuck you.
EVE_CLIENT_ID = "7704f80cb19a403abf1a1b8c4d184bc5"
EVE_CLIENT_SECRET = "DcUSHfWjQSP3hVHmDJNaCBtC5zpYfVnXmgvSTHH1"

RUIN_YADAY_CHARACTER_ID = 91395803
