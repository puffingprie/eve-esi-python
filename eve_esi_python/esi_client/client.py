"""
eve-esi-python

ESI Client
"""  # noqa: E501

from pydantic import BaseModel
from datetime import datetime

from eve_esi_python.api_client import ApiClient
from eve_esi_python.configuration import Configuration
from eve_esi_python.api.alliance_api import AllianceApi


class EsiClientConfiguration(Configuration):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_agent = "eve-esi-python/1.0.0"
        self.host = "https://esi.evetech.net/latest"


class EsiClient(ApiClient):
    def __init__(
        self, configuration: EsiClientConfiguration | None = EsiClientConfiguration()
    ):
        super().__init__(configuration=configuration)


# def create_esi_client():
#     api_client_configuration = Configuration()
#     api_client = ApiClient(configuration=api_client_configuration)
# return api_client


def test_get_alliances(client: EsiClient):
    alliance_api_instance = AllianceApi(client)
    x_compatibility_date = datetime(2020, 1, 1)
    try:
        res = alliance_api_instance.get_alliances(x_compatibility_date)
        return res
    except Exception as e:
        return e
