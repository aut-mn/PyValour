# swagger_client.ChannelApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_channels_channel_id_children_get**](ChannelApiApi.md#api_channels_channel_id_children_get) | **GET** /api/channels/{channelId}/children | 
[**api_channels_channel_id_messages_get**](ChannelApiApi.md#api_channels_channel_id_messages_get) | **GET** /api/channels/{channelId}/messages | 
[**api_channels_channel_id_messages_message_id_delete**](ChannelApiApi.md#api_channels_channel_id_messages_message_id_delete) | **DELETE** /api/channels/{channelId}/messages/{messageId} | 
[**api_channels_channel_id_messages_message_id_get**](ChannelApiApi.md#api_channels_channel_id_messages_message_id_get) | **GET** /api/channels/{channelId}/messages/{messageId} | 
[**api_channels_channel_id_messages_message_id_put**](ChannelApiApi.md#api_channels_channel_id_messages_message_id_put) | **PUT** /api/channels/{channelId}/messages/{messageId} | 
[**api_channels_channel_id_messages_post**](ChannelApiApi.md#api_channels_channel_id_messages_post) | **POST** /api/channels/{channelId}/messages | 
[**api_channels_channel_id_nodes_get**](ChannelApiApi.md#api_channels_channel_id_nodes_get) | **GET** /api/channels/{channelId}/nodes | 
[**api_channels_channel_id_non_planet_members_get**](ChannelApiApi.md#api_channels_channel_id_non_planet_members_get) | **GET** /api/channels/{channelId}/nonPlanetMembers | 
[**api_channels_direct_other_user_id_get**](ChannelApiApi.md#api_channels_direct_other_user_id_get) | **GET** /api/channels/direct/{otherUserId} | 
[**api_channels_direct_self_get**](ChannelApiApi.md#api_channels_direct_self_get) | **GET** /api/channels/direct/self | 
[**api_channels_id_get**](ChannelApiApi.md#api_channels_id_get) | **GET** /api/channels/{id} | 
[**api_channels_id_typing_post**](ChannelApiApi.md#api_channels_id_typing_post) | **POST** /api/channels/{id}/typing | 
[**api_channels_post**](ChannelApiApi.md#api_channels_post) | **POST** /api/channels | 

# **api_channels_channel_id_children_get**
> api_channels_channel_id_children_get(channel_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 

try:
    api_instance.api_channels_channel_id_children_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_messages_get**
> api_channels_channel_id_messages_get(channel_id, index=index, count=count)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 
index = 789 # int |  (optional)
count = 10 # int |  (optional) (default to 10)

try:
    api_instance.api_channels_channel_id_messages_get(channel_id, index=index, count=count)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 
 **index** | **int**|  | [optional] 
 **count** | **int**|  | [optional] [default to 10]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_messages_message_id_delete**
> api_channels_channel_id_messages_message_id_delete(message_id, channel_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
message_id = 789 # int | 
channel_id = 789 # int | 

try:
    api_instance.api_channels_channel_id_messages_message_id_delete(message_id, channel_id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_messages_message_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 
 **channel_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_messages_message_id_get**
> api_channels_channel_id_messages_message_id_get(channel_id, message_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 
message_id = 789 # int | 

try:
    api_instance.api_channels_channel_id_messages_message_id_get(channel_id, message_id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_messages_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 
 **message_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_messages_message_id_put**
> api_channels_channel_id_messages_message_id_put(channel_id, message_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 
message_id = 789 # int | 
body = swagger_client.Message() # Message |  (optional)

try:
    api_instance.api_channels_channel_id_messages_message_id_put(channel_id, message_id, body=body)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_messages_message_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 
 **message_id** | **int**|  | 
 **body** | [**Message**](Message.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_messages_post**
> api_channels_channel_id_messages_post(channel_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 
body = swagger_client.Message() # Message |  (optional)

try:
    api_instance.api_channels_channel_id_messages_post(channel_id, body=body)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 
 **body** | [**Message**](Message.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_nodes_get**
> api_channels_channel_id_nodes_get(channel_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 

try:
    api_instance.api_channels_channel_id_nodes_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_channel_id_non_planet_members_get**
> api_channels_channel_id_non_planet_members_get(channel_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
channel_id = 789 # int | 

try:
    api_instance.api_channels_channel_id_non_planet_members_get(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_channel_id_non_planet_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_direct_other_user_id_get**
> api_channels_direct_other_user_id_get(other_user_id, create=create)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
other_user_id = 789 # int | 
create = true # bool |  (optional) (default to true)

try:
    api_instance.api_channels_direct_other_user_id_get(other_user_id, create=create)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_direct_other_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_user_id** | **int**|  | 
 **create** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_channels_direct_self_get**
> api_channels_direct_self_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()

try:
    api_instance.api_channels_direct_self_get()
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_direct_self_get: %s\n" % e)
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

# **api_channels_id_get**
> api_channels_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
id = 789 # int | 

try:
    api_instance.api_channels_id_get(id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_id_get: %s\n" % e)
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

# **api_channels_id_typing_post**
> api_channels_id_typing_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
id = 789 # int | 

try:
    api_instance.api_channels_id_typing_post(id)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_id_typing_post: %s\n" % e)
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

# **api_channels_post**
> api_channels_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelApiApi()
body = swagger_client.CreateChannelRequest() # CreateChannelRequest |  (optional)

try:
    api_instance.api_channels_post(body=body)
except ApiException as e:
    print("Exception when calling ChannelApiApi->api_channels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

