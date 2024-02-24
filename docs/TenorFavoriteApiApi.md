# swagger_client.TenorFavoriteApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tenorfavorites_id_delete**](TenorFavoriteApiApi.md#api_tenorfavorites_id_delete) | **DELETE** /api/tenorfavorites/{id} | 
[**api_tenorfavorites_post**](TenorFavoriteApiApi.md#api_tenorfavorites_post) | **POST** /api/tenorfavorites | 

# **api_tenorfavorites_id_delete**
> api_tenorfavorites_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenorFavoriteApiApi()
id = 789 # int | 

try:
    api_instance.api_tenorfavorites_id_delete(id)
except ApiException as e:
    print("Exception when calling TenorFavoriteApiApi->api_tenorfavorites_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tenorfavorites_post**
> api_tenorfavorites_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenorFavoriteApiApi()
body = swagger_client.TenorFavorite() # TenorFavorite |  (optional)

try:
    api_instance.api_tenorfavorites_post(body=body)
except ApiException as e:
    print("Exception when calling TenorFavoriteApiApi->api_tenorfavorites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenorFavorite**](TenorFavorite.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

