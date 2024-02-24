# swagger_client.NotificationApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_notifications_self_clear_post**](NotificationApiApi.md#api_notifications_self_clear_post) | **POST** /api/notifications/self/clear | 
[**api_notifications_self_id_read_value_post**](NotificationApiApi.md#api_notifications_self_id_read_value_post) | **POST** /api/notifications/self/{id}/read/{value} | 
[**api_notifications_self_unread_all_get**](NotificationApiApi.md#api_notifications_self_unread_all_get) | **GET** /api/notifications/self/unread/all | 

# **api_notifications_self_clear_post**
> api_notifications_self_clear_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApiApi()

try:
    api_instance.api_notifications_self_clear_post()
except ApiException as e:
    print("Exception when calling NotificationApiApi->api_notifications_self_clear_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_notifications_self_id_read_value_post**
> api_notifications_self_id_read_value_post(id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApiApi()
id = 789 # int | 
value = true # bool | 

try:
    api_instance.api_notifications_self_id_read_value_post(id, value)
except ApiException as e:
    print("Exception when calling NotificationApiApi->api_notifications_self_id_read_value_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **value** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_notifications_self_unread_all_get**
> api_notifications_self_unread_all_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApiApi()

try:
    api_instance.api_notifications_self_unread_all_get()
except ApiException as e:
    print("Exception when calling NotificationApiApi->api_notifications_self_unread_all_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

