# swagger_client.PlanetRoleApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_roles_id_delete**](PlanetRoleApiApi.md#api_roles_id_delete) | **DELETE** /api/roles/{id} | 
[**api_roles_id_get**](PlanetRoleApiApi.md#api_roles_id_get) | **GET** /api/roles/{id} | 
[**api_roles_id_nodes_get**](PlanetRoleApiApi.md#api_roles_id_nodes_get) | **GET** /api/roles/{id}/nodes | 
[**api_roles_id_put**](PlanetRoleApiApi.md#api_roles_id_put) | **PUT** /api/roles/{id} | 
[**api_roles_post**](PlanetRoleApiApi.md#api_roles_post) | **POST** /api/roles | 

# **api_roles_id_delete**
> api_roles_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetRoleApiApi()
id = 789 # int | 

try:
    api_instance.api_roles_id_delete(id)
except ApiException as e:
    print("Exception when calling PlanetRoleApiApi->api_roles_id_delete: %s\n" % e)
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

# **api_roles_id_get**
> api_roles_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetRoleApiApi()
id = 789 # int | 

try:
    api_instance.api_roles_id_get(id)
except ApiException as e:
    print("Exception when calling PlanetRoleApiApi->api_roles_id_get: %s\n" % e)
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

# **api_roles_id_nodes_get**
> api_roles_id_nodes_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetRoleApiApi()
id = 789 # int | 

try:
    api_instance.api_roles_id_nodes_get(id)
except ApiException as e:
    print("Exception when calling PlanetRoleApiApi->api_roles_id_nodes_get: %s\n" % e)
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

# **api_roles_id_put**
> api_roles_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetRoleApiApi()
id = 789 # int | 
body = swagger_client.PlanetRole() # PlanetRole |  (optional)

try:
    api_instance.api_roles_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling PlanetRoleApiApi->api_roles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**PlanetRole**](PlanetRole.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_roles_post**
> api_roles_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetRoleApiApi()
body = swagger_client.PlanetRole() # PlanetRole |  (optional)

try:
    api_instance.api_roles_post(body=body)
except ApiException as e:
    print("Exception when calling PlanetRoleApiApi->api_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanetRole**](PlanetRole.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

