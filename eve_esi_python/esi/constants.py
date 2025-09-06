"""
eve-esi-python

Constants
"""

from enum import Enum

UNAUTHORIZED_STATUS_CODE = 401
MAX_REQUESTS_PER_SECOND = 100.0
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5

ESI_USER_AGENT_DEFAULT = "eve-esi-python/0.1.0"


# Yes, I put my secrets out for everyone to see. Fuck you.
EVE_CLIENT_ID = "7704f80cb19a403abf1a1b8c4d184bc5"
EVE_CLIENT_SECRET = "DcUSHfWjQSP3hVHmDJNaCBtC5zpYfVnXmgvSTHH1"

RUIN_YADAY_CHARACTER_ID = 91395803
