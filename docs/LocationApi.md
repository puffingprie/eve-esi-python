# eve_esi_python.LocationApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_location**](LocationApi.md#get_characters_character_id_location) | **GET** /characters/{character_id}/location | Get character location
[**get_characters_character_id_online**](LocationApi.md#get_characters_character_id_online) | **GET** /characters/{character_id}/online | Get character online
[**get_characters_character_id_ship**](LocationApi.md#get_characters_character_id_ship) | **GET** /characters/{character_id}/ship | Get current ship


# **get_characters_character_id_location**
> CharactersCharacterIdLocationGet get_characters_character_id_location(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character location

Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_location_get import CharactersCharacterIdLocationGet
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.LocationApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character location
        api_response = api_instance.get_characters_character_id_location(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of LocationApi->get_characters_character_id_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationApi->get_characters_character_id_location: %s\n" % e)
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

[**CharactersCharacterIdLocationGet**](CharactersCharacterIdLocationGet.md)

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

# **get_characters_character_id_online**
> CharactersCharacterIdOnlineGet get_characters_character_id_online(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character online

Checks if the character is currently online

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_online_get import CharactersCharacterIdOnlineGet
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.LocationApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character online
        api_response = api_instance.get_characters_character_id_online(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of LocationApi->get_characters_character_id_online:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationApi->get_characters_character_id_online: %s\n" % e)
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

[**CharactersCharacterIdOnlineGet**](CharactersCharacterIdOnlineGet.md)

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

# **get_characters_character_id_ship**
> CharactersCharacterIdShipGet get_characters_character_id_ship(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get current ship

Get the current ship type, name and id

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_ship_get import CharactersCharacterIdShipGet
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.LocationApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get current ship
        api_response = api_instance.get_characters_character_id_ship(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of LocationApi->get_characters_character_id_ship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationApi->get_characters_character_id_ship: %s\n" % e)
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

[**CharactersCharacterIdShipGet**](CharactersCharacterIdShipGet.md)

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

