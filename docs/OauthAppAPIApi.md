# swagger_client.OauthAppAPIApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_oauthapps_id_put**](OauthAppAPIApi.md#api_oauthapps_id_put) | **PUT** /api/oauthapps/{id} | 

# **api_oauthapps_id_put**
> api_oauthapps_id_put(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAppAPIApi()
body = swagger_client.OauthApp() # OauthApp |  (optional)

try:
    api_instance.api_oauthapps_id_put(body=body)
except ApiException as e:
    print("Exception when calling OauthAppAPIApi->api_oauthapps_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthApp**](OauthApp.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

