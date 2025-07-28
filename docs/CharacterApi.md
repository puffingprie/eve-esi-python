# eve_esi_python.CharacterApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id**](CharacterApi.md#get_characters_character_id) | **GET** /characters/{character_id} | Get character&#39;s public information
[**get_characters_character_id_agents_research**](CharacterApi.md#get_characters_character_id_agents_research) | **GET** /characters/{character_id}/agents_research | Get agents research
[**get_characters_character_id_blueprints**](CharacterApi.md#get_characters_character_id_blueprints) | **GET** /characters/{character_id}/blueprints | Get blueprints
[**get_characters_character_id_corporationhistory**](CharacterApi.md#get_characters_character_id_corporationhistory) | **GET** /characters/{character_id}/corporationhistory | Get corporation history
[**get_characters_character_id_fatigue**](CharacterApi.md#get_characters_character_id_fatigue) | **GET** /characters/{character_id}/fatigue | Get jump fatigue
[**get_characters_character_id_medals**](CharacterApi.md#get_characters_character_id_medals) | **GET** /characters/{character_id}/medals | Get medals
[**get_characters_character_id_notifications**](CharacterApi.md#get_characters_character_id_notifications) | **GET** /characters/{character_id}/notifications | Get character notifications
[**get_characters_character_id_notifications_contacts**](CharacterApi.md#get_characters_character_id_notifications_contacts) | **GET** /characters/{character_id}/notifications/contacts | Get new contact notifications
[**get_characters_character_id_portrait**](CharacterApi.md#get_characters_character_id_portrait) | **GET** /characters/{character_id}/portrait | Get character portraits
[**get_characters_character_id_roles**](CharacterApi.md#get_characters_character_id_roles) | **GET** /characters/{character_id}/roles | Get character corporation roles
[**get_characters_character_id_standings**](CharacterApi.md#get_characters_character_id_standings) | **GET** /characters/{character_id}/standings | Get standings
[**get_characters_character_id_titles**](CharacterApi.md#get_characters_character_id_titles) | **GET** /characters/{character_id}/titles | Get character corporation titles
[**post_characters_affiliation**](CharacterApi.md#post_characters_affiliation) | **POST** /characters/affiliation | Character affiliation
[**post_characters_character_id_cspa**](CharacterApi.md#post_characters_character_id_cspa) | **POST** /characters/{character_id}/cspa | Calculate a CSPA charge cost


# **get_characters_character_id**
> CharactersCharacterIdGet get_characters_character_id(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character's public information

Public information about a character

### Example


```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_get import CharactersCharacterIdGet
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character's public information
        api_response = api_instance.get_characters_character_id(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id: %s\n" % e)
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

[**CharactersCharacterIdGet**](CharactersCharacterIdGet.md)

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

# **get_characters_character_id_agents_research**
> List[CharactersCharacterIdAgentsResearchGetInner] get_characters_character_id_agents_research(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get agents research

Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints = remainderPoints + pointsPerDay * days(currentTime - researchStartDate)

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_agents_research_get_inner import CharactersCharacterIdAgentsResearchGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get agents research
        api_response = api_instance.get_characters_character_id_agents_research(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_agents_research:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_agents_research: %s\n" % e)
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

[**List[CharactersCharacterIdAgentsResearchGetInner]**](CharactersCharacterIdAgentsResearchGetInner.md)

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

# **get_characters_character_id_blueprints**
> List[CharactersCharacterIdBlueprintsGetInner] get_characters_character_id_blueprints(character_id, x_compatibility_date, page=page, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get blueprints

Return a list of blueprints the character owns

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_blueprints_get_inner import CharactersCharacterIdBlueprintsGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    page = 56 # int |  (optional)
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get blueprints
        api_response = api_instance.get_characters_character_id_blueprints(character_id, x_compatibility_date, page=page, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_blueprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **page** | **int**|  | [optional] 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[CharactersCharacterIdBlueprintsGetInner]**](CharactersCharacterIdBlueprintsGetInner.md)

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

# **get_characters_character_id_corporationhistory**
> List[CharactersCharacterIdCorporationhistoryGetInner] get_characters_character_id_corporationhistory(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get corporation history

Get a list of all the corporations a character has been a member of

### Example


```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_corporationhistory_get_inner import CharactersCharacterIdCorporationhistoryGetInner
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get corporation history
        api_response = api_instance.get_characters_character_id_corporationhistory(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_corporationhistory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_corporationhistory: %s\n" % e)
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

[**List[CharactersCharacterIdCorporationhistoryGetInner]**](CharactersCharacterIdCorporationhistoryGetInner.md)

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

# **get_characters_character_id_fatigue**
> CharactersCharacterIdFatigueGet get_characters_character_id_fatigue(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get jump fatigue

Return a character's jump activation and fatigue information

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_fatigue_get import CharactersCharacterIdFatigueGet
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get jump fatigue
        api_response = api_instance.get_characters_character_id_fatigue(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_fatigue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_fatigue: %s\n" % e)
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

[**CharactersCharacterIdFatigueGet**](CharactersCharacterIdFatigueGet.md)

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

# **get_characters_character_id_medals**
> List[CharactersCharacterIdMedalsGetInner] get_characters_character_id_medals(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get medals

Return a list of medals the character has

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_medals_get_inner import CharactersCharacterIdMedalsGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get medals
        api_response = api_instance.get_characters_character_id_medals(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_medals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_medals: %s\n" % e)
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

[**List[CharactersCharacterIdMedalsGetInner]**](CharactersCharacterIdMedalsGetInner.md)

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

# **get_characters_character_id_notifications**
> List[CharactersCharacterIdNotificationsGetInner] get_characters_character_id_notifications(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character notifications

Return character notifications

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_notifications_get_inner import CharactersCharacterIdNotificationsGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character notifications
        api_response = api_instance.get_characters_character_id_notifications(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_notifications: %s\n" % e)
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

[**List[CharactersCharacterIdNotificationsGetInner]**](CharactersCharacterIdNotificationsGetInner.md)

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

# **get_characters_character_id_notifications_contacts**
> List[CharactersCharacterIdNotificationsContactsGetInner] get_characters_character_id_notifications_contacts(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get new contact notifications

Return notifications about having been added to someone's contact list

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_notifications_contacts_get_inner import CharactersCharacterIdNotificationsContactsGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get new contact notifications
        api_response = api_instance.get_characters_character_id_notifications_contacts(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_notifications_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_notifications_contacts: %s\n" % e)
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

[**List[CharactersCharacterIdNotificationsContactsGetInner]**](CharactersCharacterIdNotificationsContactsGetInner.md)

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

# **get_characters_character_id_portrait**
> CharactersCharacterIdPortraitGet get_characters_character_id_portrait(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character portraits

Get portrait urls for a character

This route expires daily at 11:05

### Example


```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_portrait_get import CharactersCharacterIdPortraitGet
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character portraits
        api_response = api_instance.get_characters_character_id_portrait(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_portrait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_portrait: %s\n" % e)
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

[**CharactersCharacterIdPortraitGet**](CharactersCharacterIdPortraitGet.md)

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

# **get_characters_character_id_roles**
> CharactersCharacterIdRolesGet get_characters_character_id_roles(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character corporation roles

Returns a character's corporation roles

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_roles_get import CharactersCharacterIdRolesGet
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character corporation roles
        api_response = api_instance.get_characters_character_id_roles(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_roles: %s\n" % e)
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

[**CharactersCharacterIdRolesGet**](CharactersCharacterIdRolesGet.md)

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

# **get_characters_character_id_standings**
> List[CharactersCharacterIdStandingsGetInner] get_characters_character_id_standings(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get standings

Return character standings from agents, NPC corporations, and factions

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_standings_get_inner import CharactersCharacterIdStandingsGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get standings
        api_response = api_instance.get_characters_character_id_standings(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)
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

[**List[CharactersCharacterIdStandingsGetInner]**](CharactersCharacterIdStandingsGetInner.md)

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

# **get_characters_character_id_titles**
> List[CharactersCharacterIdTitlesGetInner] get_characters_character_id_titles(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Get character corporation titles

Returns a character's titles

### Example

* OAuth Authentication (OAuth2):

```python
import eve_esi_python
from eve_esi_python.models.characters_character_id_titles_get_inner import CharactersCharacterIdTitlesGetInner
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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Get character corporation titles
        api_response = api_instance.get_characters_character_id_titles(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of CharacterApi->get_characters_character_id_titles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->get_characters_character_id_titles: %s\n" % e)
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

[**List[CharactersCharacterIdTitlesGetInner]**](CharactersCharacterIdTitlesGetInner.md)

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

# **post_characters_affiliation**
> List[CharactersAffiliationPostInner] post_characters_affiliation(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, request_body=request_body)

Character affiliation

Bulk lookup of character IDs to corporation, alliance and faction

### Example


```python
import eve_esi_python
from eve_esi_python.models.characters_affiliation_post_inner import CharactersAffiliationPostInner
from eve_esi_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = eve_esi_python.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with eve_esi_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eve_esi_python.CharacterApi(api_client)
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    request_body = [56] # List[int] |  (optional)

    try:
        # Character affiliation
        api_response = api_instance.post_characters_affiliation(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, request_body=request_body)
        print("The response of CharacterApi->post_characters_affiliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->post_characters_affiliation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **request_body** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**List[CharactersAffiliationPostInner]**](CharactersAffiliationPostInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characters_character_id_cspa**
> float post_characters_character_id_cspa(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, request_body=request_body)

Calculate a CSPA charge cost

Takes a source character ID in the url and a set of target character ID's in the body, returns a CSPA charge cost

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
    api_instance = eve_esi_python.CharacterApi(api_client)
    character_id = 56 # int | The ID of the character
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    request_body = [56] # List[int] |  (optional)

    try:
        # Calculate a CSPA charge cost
        api_response = api_instance.post_characters_character_id_cspa(character_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, request_body=request_body)
        print("The response of CharacterApi->post_characters_character_id_cspa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharacterApi->post_characters_character_id_cspa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The ID of the character | 
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **request_body** | [**List[int]**](int.md)|  | [optional] 

### Return type

**float**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

