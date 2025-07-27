# esi_api_client.PlanetaryInteractionEsiApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_planets**](PlanetaryInteractionEsiApi.md#get_characters_character_id_planets) | **GET** /characters/{character_id}/planets | Get colonies
[**get_characters_character_id_planets_planet_id**](PlanetaryInteractionEsiApi.md#get_characters_character_id_planets_planet_id) | **GET** /characters/{character_id}/planets/{planet_id} | Get colony layout
[**get_corporations_corporation_id_customs_offices**](PlanetaryInteractionEsiApi.md#get_corporations_corporation_id_customs_offices) | **GET** /corporations/{corporation_id}/customs_offices | List corporation customs offices
[**get_universe_schematics_schematic_id**](PlanetaryInteractionEsiApi.md#get_universe_schematics_schematic_id) | **GET** /universe/schematics/{schematic_id} | Get schematic information


# **get_characters_character_id_planets**
> List[CharactersCharacterIdPlanetsGetInner] get_characters_character_id_planets(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get colonies

Returns a list of all planetary colonies owned by a character.

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
from esi_api_client.models.characters_character_id_planets_get_inner import CharactersCharacterIdPlanetsGetInner
from esi_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_api_client.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_api_client.PlanetaryInteractionEsiApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get colonies
        api_response = api_instance.get_characters_character_id_planets(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of PlanetaryInteractionEsiApi->get_characters_character_id_planets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanetaryInteractionEsiApi->get_characters_character_id_planets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[CharactersCharacterIdPlanetsGetInner]**](CharactersCharacterIdPlanetsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_planets_planet_id**
> CharactersCharacterIdPlanetsPlanetIdGet get_characters_character_id_planets_planet_id(character_id, planet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get colony layout

Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
from esi_api_client.models.characters_character_id_planets_planet_id_get import CharactersCharacterIdPlanetsPlanetIdGet
from esi_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_api_client.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_api_client.PlanetaryInteractionEsiApi(api_client)
    character_id = 56 # int | The ID of the character
    planet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get colony layout
        api_response = api_instance.get_characters_character_id_planets_planet_id(character_id, planet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of PlanetaryInteractionEsiApi->get_characters_character_id_planets_planet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanetaryInteractionEsiApi->get_characters_character_id_planets_planet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **planet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**CharactersCharacterIdPlanetsPlanetIdGet**](CharactersCharacterIdPlanetsPlanetIdGet.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_customs_offices**
> List[CorporationsCorporationIdCustomsOfficesGetInner] get_corporations_corporation_id_customs_offices(corporation_id, x_compatibility_date, page=page, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

List corporation customs offices

List customs offices owned by a corporation

Requires one of the following EVE corporation role(s): Director

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
from esi_api_client.models.corporations_corporation_id_customs_offices_get_inner import CorporationsCorporationIdCustomsOfficesGetInner
from esi_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_api_client.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with esi_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_api_client.PlanetaryInteractionEsiApi(api_client)
    corporation_id = 56 # int | The ID of the corporation
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    page = 56 # int |  (optional)
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # List corporation customs offices
        api_response = api_instance.get_corporations_corporation_id_customs_offices(corporation_id, x_compatibility_date, page=page, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of PlanetaryInteractionEsiApi->get_corporations_corporation_id_customs_offices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanetaryInteractionEsiApi->get_corporations_corporation_id_customs_offices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| The ID of the corporation | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **page** | **int**|  | [optional] 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[CorporationsCorporationIdCustomsOfficesGetInner]**](CorporationsCorporationIdCustomsOfficesGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  * X-Pages - The total number of pages in the result set. <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_schematics_schematic_id**
> UniverseSchematicsSchematicIdGet get_universe_schematics_schematic_id(schematic_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get schematic information

Get information on a planetary factory schematic

### Example


```python
import esi_api_client
from esi_api_client.models.universe_schematics_schematic_id_get import UniverseSchematicsSchematicIdGet
from esi_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_api_client.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with esi_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_api_client.PlanetaryInteractionEsiApi(api_client)
    schematic_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get schematic information
        api_response = api_instance.get_universe_schematics_schematic_id(schematic_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of PlanetaryInteractionEsiApi->get_universe_schematics_schematic_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanetaryInteractionEsiApi->get_universe_schematics_schematic_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schematic_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**UniverseSchematicsSchematicIdGet**](UniverseSchematicsSchematicIdGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

