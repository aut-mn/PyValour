# swagger_client.OrderApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_orders_order_id_capture_post**](OrderApiApi.md#api_orders_order_id_capture_post) | **POST** /api/orders/{orderId}/capture | 
[**api_orders_product_id_post**](OrderApiApi.md#api_orders_product_id_post) | **POST** /api/orders/{productId} | 

# **api_orders_order_id_capture_post**
> api_orders_order_id_capture_post(order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrderApiApi()
order_id = 'order_id_example' # str | 

try:
    api_instance.api_orders_order_id_capture_post(order_id)
except ApiException as e:
    print("Exception when calling OrderApiApi->api_orders_order_id_capture_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_orders_product_id_post**
> api_orders_product_id_post(product_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrderApiApi()
product_id = 'product_id_example' # str | 

try:
    api_instance.api_orders_product_id_post(product_id)
except ApiException as e:
    print("Exception when calling OrderApiApi->api_orders_product_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

