# swagger_client.SubscriptionApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_subscriptions_active_user_id_get**](SubscriptionApiApi.md#api_subscriptions_active_user_id_get) | **GET** /api/subscriptions/active/{userId} | 
[**api_subscriptions_end_post**](SubscriptionApiApi.md#api_subscriptions_end_post) | **POST** /api/subscriptions/end | 
[**api_subscriptions_sub_type_price_get**](SubscriptionApiApi.md#api_subscriptions_sub_type_price_get) | **GET** /api/subscriptions/{subType}/price | 
[**api_subscriptions_sub_type_start_post**](SubscriptionApiApi.md#api_subscriptions_sub_type_start_post) | **POST** /api/subscriptions/{subType}/start | 

# **api_subscriptions_active_user_id_get**
> api_subscriptions_active_user_id_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionApiApi()

try:
    api_instance.api_subscriptions_active_user_id_get()
except ApiException as e:
    print("Exception when calling SubscriptionApiApi->api_subscriptions_active_user_id_get: %s\n" % e)
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

# **api_subscriptions_end_post**
> api_subscriptions_end_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionApiApi()

try:
    api_instance.api_subscriptions_end_post()
except ApiException as e:
    print("Exception when calling SubscriptionApiApi->api_subscriptions_end_post: %s\n" % e)
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

# **api_subscriptions_sub_type_price_get**
> api_subscriptions_sub_type_price_get(sub_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionApiApi()
sub_type = 'sub_type_example' # str | 

try:
    api_instance.api_subscriptions_sub_type_price_get(sub_type)
except ApiException as e:
    print("Exception when calling SubscriptionApiApi->api_subscriptions_sub_type_price_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_subscriptions_sub_type_start_post**
> api_subscriptions_sub_type_start_post(sub_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionApiApi()
sub_type = 'sub_type_example' # str | 

try:
    api_instance.api_subscriptions_sub_type_start_post(sub_type)
except ApiException as e:
    print("Exception when calling SubscriptionApiApi->api_subscriptions_sub_type_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

