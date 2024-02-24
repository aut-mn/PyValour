# swagger_client.UserFriendApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_userfriends_add_friend_username_post**](UserFriendApiApi.md#api_userfriends_add_friend_username_post) | **POST** /api/userfriends/add/{friendUsername} | 
[**api_userfriends_cancel_username_post**](UserFriendApiApi.md#api_userfriends_cancel_username_post) | **POST** /api/userfriends/cancel/{username} | 
[**api_userfriends_decline_username_post**](UserFriendApiApi.md#api_userfriends_decline_username_post) | **POST** /api/userfriends/decline/{username} | 
[**api_userfriends_remove_friend_username_post**](UserFriendApiApi.md#api_userfriends_remove_friend_username_post) | **POST** /api/userfriends/remove/{friendUsername} | 
[**api_userfriends_user_id_friend_id_get**](UserFriendApiApi.md#api_userfriends_user_id_friend_id_get) | **GET** /api/userfriends/{userId}/{friendId} | 

# **api_userfriends_add_friend_username_post**
> api_userfriends_add_friend_username_post(friend_username)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserFriendApiApi()
friend_username = 'friend_username_example' # str | 

try:
    api_instance.api_userfriends_add_friend_username_post(friend_username)
except ApiException as e:
    print("Exception when calling UserFriendApiApi->api_userfriends_add_friend_username_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friend_username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userfriends_cancel_username_post**
> api_userfriends_cancel_username_post(username)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserFriendApiApi()
username = 'username_example' # str | 

try:
    api_instance.api_userfriends_cancel_username_post(username)
except ApiException as e:
    print("Exception when calling UserFriendApiApi->api_userfriends_cancel_username_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userfriends_decline_username_post**
> api_userfriends_decline_username_post(username)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserFriendApiApi()
username = 'username_example' # str | 

try:
    api_instance.api_userfriends_decline_username_post(username)
except ApiException as e:
    print("Exception when calling UserFriendApiApi->api_userfriends_decline_username_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userfriends_remove_friend_username_post**
> api_userfriends_remove_friend_username_post(friend_username)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserFriendApiApi()
friend_username = 'friend_username_example' # str | 

try:
    api_instance.api_userfriends_remove_friend_username_post(friend_username)
except ApiException as e:
    print("Exception when calling UserFriendApiApi->api_userfriends_remove_friend_username_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friend_username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userfriends_user_id_friend_id_get**
> api_userfriends_user_id_friend_id_get(user_id, friend_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserFriendApiApi()
user_id = 789 # int | 
friend_id = 789 # int | 

try:
    api_instance.api_userfriends_user_id_friend_id_get(user_id, friend_id)
except ApiException as e:
    print("Exception when calling UserFriendApiApi->api_userfriends_user_id_friend_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **friend_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

