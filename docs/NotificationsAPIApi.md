# swagger_client.NotificationsAPIApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_notification_subscribe_post**](NotificationsAPIApi.md#api_notification_subscribe_post) | **POST** /api/notification/subscribe | 
[**api_notification_unsubscribe_post**](NotificationsAPIApi.md#api_notification_unsubscribe_post) | **POST** /api/notification/unsubscribe | 

# **api_notification_subscribe_post**
> api_notification_subscribe_post(body=body, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsAPIApi()
body = swagger_client.NotificationSubscription() # NotificationSubscription |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_notification_subscribe_post(body=body, authorization=authorization)
except ApiException as e:
    print("Exception when calling NotificationsAPIApi->api_notification_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationSubscription**](NotificationSubscription.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_notification_unsubscribe_post**
> api_notification_unsubscribe_post(body=body, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsAPIApi()
body = swagger_client.NotificationSubscription() # NotificationSubscription |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_notification_unsubscribe_post(body=body, authorization=authorization)
except ApiException as e:
    print("Exception when calling NotificationsAPIApi->api_notification_unsubscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationSubscription**](NotificationSubscription.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

