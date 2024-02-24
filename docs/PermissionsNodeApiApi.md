# swagger_client.PermissionsNodeApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_permissionsnodes_all_planet_id_get**](PermissionsNodeApiApi.md#api_permissionsnodes_all_planet_id_get) | **GET** /api/permissionsnodes/all/{planetId} | 
[**api_permissionsnodes_id_get**](PermissionsNodeApiApi.md#api_permissionsnodes_id_get) | **GET** /api/permissionsnodes/{id} | 
[**api_permissionsnodes_post**](PermissionsNodeApiApi.md#api_permissionsnodes_post) | **POST** /api/permissionsnodes | 
[**api_permissionsnodes_type_target_id_role_id_get**](PermissionsNodeApiApi.md#api_permissionsnodes_type_target_id_role_id_get) | **GET** /api/permissionsnodes/{type}/{targetId}/{roleId} | 
[**api_permissionsnodes_type_target_id_role_id_put**](PermissionsNodeApiApi.md#api_permissionsnodes_type_target_id_role_id_put) | **PUT** /api/permissionsnodes/{type}/{targetId}/{roleId} | 

# **api_permissionsnodes_all_planet_id_get**
> api_permissionsnodes_all_planet_id_get(planet_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsNodeApiApi()
planet_id = 789 # int | 

try:
    api_instance.api_permissionsnodes_all_planet_id_get(planet_id)
except ApiException as e:
    print("Exception when calling PermissionsNodeApiApi->api_permissionsnodes_all_planet_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_permissionsnodes_id_get**
> api_permissionsnodes_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsNodeApiApi()
id = 789 # int | 

try:
    api_instance.api_permissionsnodes_id_get(id)
except ApiException as e:
    print("Exception when calling PermissionsNodeApiApi->api_permissionsnodes_id_get: %s\n" % e)
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

# **api_permissionsnodes_post**
> api_permissionsnodes_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsNodeApiApi()
body = swagger_client.PermissionsNode() # PermissionsNode |  (optional)

try:
    api_instance.api_permissionsnodes_post(body=body)
except ApiException as e:
    print("Exception when calling PermissionsNodeApiApi->api_permissionsnodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionsNode**](PermissionsNode.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_permissionsnodes_type_target_id_role_id_get**
> api_permissionsnodes_type_target_id_role_id_get(type, target_id, role_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsNodeApiApi()
type = 'type_example' # str | 
target_id = 789 # int | 
role_id = 789 # int | 

try:
    api_instance.api_permissionsnodes_type_target_id_role_id_get(type, target_id, role_id)
except ApiException as e:
    print("Exception when calling PermissionsNodeApiApi->api_permissionsnodes_type_target_id_role_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **target_id** | **int**|  | 
 **role_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_permissionsnodes_type_target_id_role_id_put**
> api_permissionsnodes_type_target_id_role_id_put(type, target_id, role_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsNodeApiApi()
type = 'type_example' # str | 
target_id = 789 # int | 
role_id = 789 # int | 
body = swagger_client.PermissionsNode() # PermissionsNode |  (optional)

try:
    api_instance.api_permissionsnodes_type_target_id_role_id_put(type, target_id, role_id, body=body)
except ApiException as e:
    print("Exception when calling PermissionsNodeApiApi->api_permissionsnodes_type_target_id_role_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **target_id** | **int**|  | 
 **role_id** | **int**|  | 
 **body** | [**PermissionsNode**](PermissionsNode.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

