# eve_esi_python.FleetsApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fleets_fleet_id_members_member_id**](FleetsApi.md#delete_fleets_fleet_id_members_member_id) | **DELETE** /fleets/{fleet_id}/members/{member_id} | Kick fleet member
[**delete_fleets_fleet_id_squads_squad_id**](FleetsApi.md#delete_fleets_fleet_id_squads_squad_id) | **DELETE** /fleets/{fleet_id}/squads/{squad_id} | Delete fleet squad
[**delete_fleets_fleet_id_wings_wing_id**](FleetsApi.md#delete_fleets_fleet_id_wings_wing_id) | **DELETE** /fleets/{fleet_id}/wings/{wing_id} | Delete fleet wing
[**get_characters_character_id_fleet**](FleetsApi.md#get_characters_character_id_fleet) | **GET** /characters/{character_id}/fleet | Get character fleet info
[**get_fleets_fleet_id**](FleetsApi.md#get_fleets_fleet_id) | **GET** /fleets/{fleet_id} | Get fleet information
[**get_fleets_fleet_id_members**](FleetsApi.md#get_fleets_fleet_id_members) | **GET** /fleets/{fleet_id}/members | Get fleet members
[**get_fleets_fleet_id_wings**](FleetsApi.md#get_fleets_fleet_id_wings) | **GET** /fleets/{fleet_id}/wings | Get fleet wings
[**post_fleets_fleet_id_members**](FleetsApi.md#post_fleets_fleet_id_members) | **POST** /fleets/{fleet_id}/members | Create fleet invitation
[**post_fleets_fleet_id_wings**](FleetsApi.md#post_fleets_fleet_id_wings) | **POST** /fleets/{fleet_id}/wings | Create fleet wing
[**post_fleets_fleet_id_wings_wing_id_squads**](FleetsApi.md#post_fleets_fleet_id_wings_wing_id_squads) | **POST** /fleets/{fleet_id}/wings/{wing_id}/squads | Create fleet squad
[**put_fleets_fleet_id**](FleetsApi.md#put_fleets_fleet_id) | **PUT** /fleets/{fleet_id} | Update fleet
[**put_fleets_fleet_id_members_member_id**](FleetsApi.md#put_fleets_fleet_id_members_member_id) | **PUT** /fleets/{fleet_id}/members/{member_id} | Move fleet member
[**put_fleets_fleet_id_squads_squad_id**](FleetsApi.md#put_fleets_fleet_id_squads_squad_id) | **PUT** /fleets/{fleet_id}/squads/{squad_id} | Rename fleet squad
[**put_fleets_fleet_id_wings_wing_id**](FleetsApi.md#put_fleets_fleet_id_wings_wing_id) | **PUT** /fleets/{fleet_id}/wings/{wing_id} | Rename fleet wing


# **delete_fleets_fleet_id_members_member_id**
> object delete_fleets_fleet_id_members_member_id(fleet_id, member_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Kick fleet member

Kick a fleet member

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    member_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Kick fleet member
        api_response = api_instance.delete_fleets_fleet_id_members_member_id(fleet_id, member_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->delete_fleets_fleet_id_members_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **member_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet member kicked |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleets_fleet_id_squads_squad_id**
> object delete_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Delete fleet squad

Delete a fleet squad, only empty squads can be deleted

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    squad_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Delete fleet squad
        api_response = api_instance.delete_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->delete_fleets_fleet_id_squads_squad_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_squads_squad_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **squad_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Squad deleted |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleets_fleet_id_wings_wing_id**
> object delete_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Delete fleet wing

Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    wing_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Delete fleet wing
        api_response = api_instance.delete_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->delete_fleets_fleet_id_wings_wing_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->delete_fleets_fleet_id_wings_wing_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **wing_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Wing deleted |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_fleet**
> CharactersCharacterIdFleetGet get_characters_character_id_fleet(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character fleet info

Return the fleet ID the character is in, if any.

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_fleet_get import CharactersCharacterIdFleetGet
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character fleet info
        api_response = api_instance.get_characters_character_id_fleet(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->get_characters_character_id_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_characters_character_id_fleet: %s\n" % e)
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

[**CharactersCharacterIdFleetGet**](CharactersCharacterIdFleetGet.md)

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

# **get_fleets_fleet_id**
> FleetsFleetIdGet get_fleets_fleet_id(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get fleet information

Return details about a fleet

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.fleets_fleet_id_get import FleetsFleetIdGet
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get fleet information
        api_response = api_instance.get_fleets_fleet_id(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->get_fleets_fleet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**FleetsFleetIdGet**](FleetsFleetIdGet.md)

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

# **get_fleets_fleet_id_members**
> List[FleetsFleetIdMembersGetInner] get_fleets_fleet_id_members(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get fleet members

Return information about fleet members

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.fleets_fleet_id_members_get_inner import FleetsFleetIdMembersGetInner
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get fleet members
        api_response = api_instance.get_fleets_fleet_id_members(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->get_fleets_fleet_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[FleetsFleetIdMembersGetInner]**](FleetsFleetIdMembersGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * Content-Language -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleets_fleet_id_wings**
> List[FleetsFleetIdWingsGetInner] get_fleets_fleet_id_wings(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get fleet wings

Return information about wings in a fleet

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.fleets_fleet_id_wings_get_inner import FleetsFleetIdWingsGetInner
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get fleet wings
        api_response = api_instance.get_fleets_fleet_id_wings(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->get_fleets_fleet_id_wings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->get_fleets_fleet_id_wings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[FleetsFleetIdWingsGetInner]**](FleetsFleetIdWingsGetInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * Content-Language -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_members**
> object post_fleets_fleet_id_members(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, post_fleets_fleet_id_members_request=post_fleets_fleet_id_members_request)

Create fleet invitation

Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.post_fleets_fleet_id_members_request import PostFleetsFleetIdMembersRequest
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    post_fleets_fleet_id_members_request = eve_esi_python.PostFleetsFleetIdMembersRequest() # PostFleetsFleetIdMembersRequest |  (optional)

    try:
        # Create fleet invitation
        api_response = api_instance.post_fleets_fleet_id_members(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, post_fleets_fleet_id_members_request=post_fleets_fleet_id_members_request)
        print("The response of FleetsApi->post_fleets_fleet_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **post_fleets_fleet_id_members_request** | [**PostFleetsFleetIdMembersRequest**](PostFleetsFleetIdMembersRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet invitation sent |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_wings**
> FleetsFleetIdWingsPost post_fleets_fleet_id_wings(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Create fleet wing

Create a new wing in a fleet

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.fleets_fleet_id_wings_post import FleetsFleetIdWingsPost
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Create fleet wing
        api_response = api_instance.post_fleets_fleet_id_wings(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->post_fleets_fleet_id_wings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_wings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**FleetsFleetIdWingsPost**](FleetsFleetIdWingsPost.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fleets_fleet_id_wings_wing_id_squads**
> FleetsFleetIdWingsWingIdSquadsPost post_fleets_fleet_id_wings_wing_id_squads(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Create fleet squad

Create a new squad in a fleet

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.fleets_fleet_id_wings_wing_id_squads_post import FleetsFleetIdWingsWingIdSquadsPost
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    wing_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Create fleet squad
        api_response = api_instance.post_fleets_fleet_id_wings_wing_id_squads(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of FleetsApi->post_fleets_fleet_id_wings_wing_id_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->post_fleets_fleet_id_wings_wing_id_squads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **wing_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**FleetsFleetIdWingsWingIdSquadsPost**](FleetsFleetIdWingsWingIdSquadsPost.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id**
> object put_fleets_fleet_id(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_request=put_fleets_fleet_id_request)

Update fleet

Update settings about a fleet

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.put_fleets_fleet_id_request import PutFleetsFleetIdRequest
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    put_fleets_fleet_id_request = eve_esi_python.PutFleetsFleetIdRequest() # PutFleetsFleetIdRequest |  (optional)

    try:
        # Update fleet
        api_response = api_instance.put_fleets_fleet_id(fleet_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_request=put_fleets_fleet_id_request)
        print("The response of FleetsApi->put_fleets_fleet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **put_fleets_fleet_id_request** | [**PutFleetsFleetIdRequest**](PutFleetsFleetIdRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet updated |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_members_member_id**
> object put_fleets_fleet_id_members_member_id(fleet_id, member_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_members_member_id_request=put_fleets_fleet_id_members_member_id_request)

Move fleet member

Move a fleet member around

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.put_fleets_fleet_id_members_member_id_request import PutFleetsFleetIdMembersMemberIdRequest
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    member_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    put_fleets_fleet_id_members_member_id_request = eve_esi_python.PutFleetsFleetIdMembersMemberIdRequest() # PutFleetsFleetIdMembersMemberIdRequest |  (optional)

    try:
        # Move fleet member
        api_response = api_instance.put_fleets_fleet_id_members_member_id(fleet_id, member_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_members_member_id_request=put_fleets_fleet_id_members_member_id_request)
        print("The response of FleetsApi->put_fleets_fleet_id_members_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **member_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **put_fleets_fleet_id_members_member_id_request** | [**PutFleetsFleetIdMembersMemberIdRequest**](PutFleetsFleetIdMembersMemberIdRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Fleet invitation sent |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_squads_squad_id**
> object put_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_squads_squad_id_request=put_fleets_fleet_id_squads_squad_id_request)

Rename fleet squad

Rename a fleet squad

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.put_fleets_fleet_id_squads_squad_id_request import PutFleetsFleetIdSquadsSquadIdRequest
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    squad_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    put_fleets_fleet_id_squads_squad_id_request = eve_esi_python.PutFleetsFleetIdSquadsSquadIdRequest() # PutFleetsFleetIdSquadsSquadIdRequest |  (optional)

    try:
        # Rename fleet squad
        api_response = api_instance.put_fleets_fleet_id_squads_squad_id(fleet_id, squad_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_squads_squad_id_request=put_fleets_fleet_id_squads_squad_id_request)
        print("The response of FleetsApi->put_fleets_fleet_id_squads_squad_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_squads_squad_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **squad_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **put_fleets_fleet_id_squads_squad_id_request** | [**PutFleetsFleetIdSquadsSquadIdRequest**](PutFleetsFleetIdSquadsSquadIdRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Squad renamed |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fleets_fleet_id_wings_wing_id**
> object put_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_squads_squad_id_request=put_fleets_fleet_id_squads_squad_id_request)

Rename fleet wing

Rename a fleet wing

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.put_fleets_fleet_id_squads_squad_id_request import PutFleetsFleetIdSquadsSquadIdRequest
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
    api_instance = eve_esi_python.FleetsApi(api_client)
    fleet_id = 56 # int | 
    wing_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    put_fleets_fleet_id_squads_squad_id_request = eve_esi_python.PutFleetsFleetIdSquadsSquadIdRequest() # PutFleetsFleetIdSquadsSquadIdRequest |  (optional)

    try:
        # Rename fleet wing
        api_response = api_instance.put_fleets_fleet_id_wings_wing_id(fleet_id, wing_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, put_fleets_fleet_id_squads_squad_id_request=put_fleets_fleet_id_squads_squad_id_request)
        print("The response of FleetsApi->put_fleets_fleet_id_wings_wing_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetsApi->put_fleets_fleet_id_wings_wing_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_id** | **int**|  | 
 **wing_id** | **int**|  | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **put_fleets_fleet_id_squads_squad_id_request** | [**PutFleetsFleetIdSquadsSquadIdRequest**](PutFleetsFleetIdSquadsSquadIdRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Wing renamed |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

