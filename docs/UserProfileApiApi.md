# swagger_client.UserProfileApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_user_profiles_id_get**](UserProfileApiApi.md#api_user_profiles_id_get) | **GET** /api/userProfiles/{id} | 
[**api_user_profiles_id_put**](UserProfileApiApi.md#api_user_profiles_id_put) | **PUT** /api/userProfiles/{id} | 

# **api_user_profiles_id_get**
> api_user_profiles_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApiApi()
id = 789 # int | 

try:
    api_instance.api_user_profiles_id_get(id)
except ApiException as e:
    print("Exception when calling UserProfileApiApi->api_user_profiles_id_get: %s\n" % e)
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

# **api_user_profiles_id_put**
> api_user_profiles_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApiApi()
id = 789 # int | 
body = swagger_client.UserProfile() # UserProfile |  (optional)

try:
    api_instance.api_user_profiles_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling UserProfileApiApi->api_user_profiles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**UserProfile**](UserProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

