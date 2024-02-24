# swagger_client.PlanetBanApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_bans_id_delete**](PlanetBanApiApi.md#api_bans_id_delete) | **DELETE** /api/bans/{id} | 
[**api_bans_id_get**](PlanetBanApiApi.md#api_bans_id_get) | **GET** /api/bans/{id} | 
[**api_bans_id_put**](PlanetBanApiApi.md#api_bans_id_put) | **PUT** /api/bans/{id} | 
[**api_bans_post**](PlanetBanApiApi.md#api_bans_post) | **POST** /api/bans | 

# **api_bans_id_delete**
> api_bans_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetBanApiApi()
id = 789 # int | 

try:
    api_instance.api_bans_id_delete(id)
except ApiException as e:
    print("Exception when calling PlanetBanApiApi->api_bans_id_delete: %s\n" % e)
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

# **api_bans_id_get**
> api_bans_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetBanApiApi()
id = 789 # int | 

try:
    api_instance.api_bans_id_get(id)
except ApiException as e:
    print("Exception when calling PlanetBanApiApi->api_bans_id_get: %s\n" % e)
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

# **api_bans_id_put**
> api_bans_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetBanApiApi()
id = 789 # int | 
body = swagger_client.PlanetBan() # PlanetBan |  (optional)

try:
    api_instance.api_bans_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling PlanetBanApiApi->api_bans_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**PlanetBan**](PlanetBan.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_bans_post**
> api_bans_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetBanApiApi()
body = swagger_client.PlanetBan() # PlanetBan |  (optional)

try:
    api_instance.api_bans_post(body=body)
except ApiException as e:
    print("Exception when calling PlanetBanApiApi->api_bans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanetBan**](PlanetBan.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

