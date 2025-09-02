from eve_esi_python.esi_client.client import (
    EsiClient,
    EsiClientConfiguration,
    generate_auth_url,
    exchange_code_for_tokens,
    refresh_access_token,
    get_char_blueprints,
)
from eve_esi_python.esi_client.constants import RUIN_YADAY_CHARACTER_ID
from eve_esi_python import CharacterApi

from datetime import datetime


def run_test():
    client = EsiClient()
    auth_url, state = generate_auth_url()
    print(f"\nURL: {auth_url}\nstate: {state}")
    code = input("\nInput the code: ").strip()
    token = exchange_code_for_tokens(client, code)
    print(token)

    # try refreshing access token
    # refresh_token = refresh_access_token(client, token.refresh_token)
    # print(refresh_token)

    # get char bps
    # print(get_char_blueprints(token.access_token, RUIN_YADAY_CHARACTER_ID))
    authed_client = EsiClient(
        configuration=EsiClientConfiguration(access_token=token.access_token)
    )
    instance = CharacterApi(authed_client)
    res = instance.get_characters_character_id_blueprints(
        RUIN_YADAY_CHARACTER_ID, datetime(2025, 8, 26)
    )
    print(res)


run_test()
