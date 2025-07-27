# esi_api_client.UserInterfaceEsiApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_ui_autopilot_waypoint**](UserInterfaceEsiApi.md#post_ui_autopilot_waypoint) | **POST** /ui/autopilot/waypoint | Set Autopilot Waypoint
[**post_ui_openwindow_contract**](UserInterfaceEsiApi.md#post_ui_openwindow_contract) | **POST** /ui/openwindow/contract | Open Contract Window
[**post_ui_openwindow_information**](UserInterfaceEsiApi.md#post_ui_openwindow_information) | **POST** /ui/openwindow/information | Open Information Window
[**post_ui_openwindow_marketdetails**](UserInterfaceEsiApi.md#post_ui_openwindow_marketdetails) | **POST** /ui/openwindow/marketdetails | Open Market Details
[**post_ui_openwindow_newmail**](UserInterfaceEsiApi.md#post_ui_openwindow_newmail) | **POST** /ui/openwindow/newmail | Open New Mail Window


# **post_ui_autopilot_waypoint**
> object post_ui_autopilot_waypoint(add_to_beginning, clear_other_waypoints, destination_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Set Autopilot Waypoint

Set a solar system as autopilot waypoint

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
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
    api_instance = esi_api_client.UserInterfaceEsiApi(api_client)
    add_to_beginning = False # bool |  (default to False)
    clear_other_waypoints = False # bool |  (default to False)
    destination_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Set Autopilot Waypoint
        api_response = api_instance.post_ui_autopilot_waypoint(add_to_beginning, clear_other_waypoints, destination_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of UserInterfaceEsiApi->post_ui_autopilot_waypoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceEsiApi->post_ui_autopilot_waypoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_beginning** | **bool**|  | [default to False]
 **clear_other_waypoints** | **bool**|  | [default to False]
 **destination_id** | **int**|  | 
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
**204** | Open window request received |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ui_openwindow_contract**
> object post_ui_openwindow_contract(contract_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Open Contract Window

Open the contract window inside the client

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
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
    api_instance = esi_api_client.UserInterfaceEsiApi(api_client)
    contract_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Open Contract Window
        api_response = api_instance.post_ui_openwindow_contract(contract_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of UserInterfaceEsiApi->post_ui_openwindow_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceEsiApi->post_ui_openwindow_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 
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
**204** | Open window request received |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ui_openwindow_information**
> object post_ui_openwindow_information(target_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Open Information Window

Open the information window for a character, corporation or alliance inside the client

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
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
    api_instance = esi_api_client.UserInterfaceEsiApi(api_client)
    target_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Open Information Window
        api_response = api_instance.post_ui_openwindow_information(target_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of UserInterfaceEsiApi->post_ui_openwindow_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceEsiApi->post_ui_openwindow_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**|  | 
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
**204** | Open window request received |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ui_openwindow_marketdetails**
> object post_ui_openwindow_marketdetails(type_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

Open Market Details

Open the market details window for a specific typeID inside the client

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
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
    api_instance = esi_api_client.UserInterfaceEsiApi(api_client)
    type_id = 56 # int | 
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # Open Market Details
        api_response = api_instance.post_ui_openwindow_marketdetails(type_id, x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of UserInterfaceEsiApi->post_ui_openwindow_marketdetails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceEsiApi->post_ui_openwindow_marketdetails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **int**|  | 
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
**204** | Open window request received |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ui_openwindow_newmail**
> object post_ui_openwindow_newmail(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, post_ui_openwindow_newmail_request=post_ui_openwindow_newmail_request)

Open New Mail Window

Open the New Mail window, according to settings from the request if applicable

### Example

* OAuth Authentication (OAuth2):

```python
import esi_api_client
from esi_api_client.models.post_ui_openwindow_newmail_request import PostUiOpenwindowNewmailRequest
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
    api_instance = esi_api_client.UserInterfaceEsiApi(api_client)
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)
    post_ui_openwindow_newmail_request = esi_api_client.PostUiOpenwindowNewmailRequest() # PostUiOpenwindowNewmailRequest |  (optional)

    try:
        # Open New Mail Window
        api_response = api_instance.post_ui_openwindow_newmail(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant, post_ui_openwindow_newmail_request=post_ui_openwindow_newmail_request)
        print("The response of UserInterfaceEsiApi->post_ui_openwindow_newmail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInterfaceEsiApi->post_ui_openwindow_newmail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 
 **post_ui_openwindow_newmail_request** | [**PostUiOpenwindowNewmailRequest**](PostUiOpenwindowNewmailRequest.md)|  | [optional] 

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
**204** | Open window request received |  * Cache-Control -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

