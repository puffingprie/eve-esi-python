# esi_client.InsuranceApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_insurance_prices**](InsuranceApi.md#get_insurance_prices) | **GET** /insurance/prices | List insurance levels


# **get_insurance_prices**
> List[InsurancePricesGetInner] get_insurance_prices(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)

List insurance levels

Return available insurance levels for all ship types

### Example


```python
import esi_client
from esi_client.models.insurance_prices_get_inner import InsurancePricesGetInner
from esi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://esi.evetech.net
# See configuration.py for a list of all supported configuration parameters.
configuration = esi_client.Configuration(
    host = "https://esi.evetech.net"
)


# Enter a context with an instance of the API client
with esi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esi_client.InsuranceApi(api_client)
    x_compatibility_date = '2020-01-01' # date | The compatibility date for the request.
    accept_language = 'en' # str | The language to use for the response. Defaults to 'en'. (optional)
    if_none_match = 'if_none_match_example' # str | The ETag of the previous request. A 304 will be returned if this matches the current ETag. (optional)
    x_tenant = 'tranquility' # str | The tenant ID for the request. Defaults to 'tranquility'. (optional)

    try:
        # List insurance levels
        api_response = api_instance.get_insurance_prices(x_compatibility_date, accept_language=accept_language, if_none_match=if_none_match, x_tenant=x_tenant)
        print("The response of InsuranceApi->get_insurance_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsuranceApi->get_insurance_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_compatibility_date** | **date**| The compatibility date for the request. | 
 **accept_language** | **str**| The language to use for the response. Defaults to &#39;en&#39;. | [optional] 
 **if_none_match** | **str**| The ETag of the previous request. A 304 will be returned if this matches the current ETag. | [optional] 
 **x_tenant** | **str**| The tenant ID for the request. Defaults to &#39;tranquility&#39;. | [optional] 

### Return type

[**List[InsurancePricesGetInner]**](InsurancePricesGetInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Cache-Control -  <br>  * Content-Language -  <br>  * ETag -  <br>  * Last-Modified -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

