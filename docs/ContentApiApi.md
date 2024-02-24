# swagger_client.ContentApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_category_user_id_hash_get**](ContentApiApi.md#content_category_user_id_hash_get) | **GET** /content/{category}/{userId}/{hash} | 

# **content_category_user_id_hash_get**
> content_category_user_id_hash_get(category, hash, user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApiApi()
category = 'category_example' # str | 
hash = 'hash_example' # str | 
user_id = 789 # int | 

try:
    api_instance.content_category_user_id_hash_get(category, hash, user_id)
except ApiException as e:
    print("Exception when calling ContentApiApi->content_category_user_id_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **hash** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

