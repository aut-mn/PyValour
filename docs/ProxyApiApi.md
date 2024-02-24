# swagger_client.ProxyApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxy_url_get**](ProxyApiApi.md#proxy_url_get) | **GET** /proxy/{url} | 

# **proxy_url_get**
> proxy_url_get(url)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProxyApiApi()
url = 'url_example' # str | 

try:
    api_instance.proxy_url_get(url)
except ApiException as e:
    print("Exception when calling ProxyApiApi->proxy_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

