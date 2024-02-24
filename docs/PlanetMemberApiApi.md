# swagger_client.PlanetMemberApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_members_byuser_planet_id_user_id_get**](PlanetMemberApiApi.md#api_members_byuser_planet_id_user_id_get) | **GET** /api/members/byuser/{planetId}/{userId} | 
[**api_members_id_authority_get**](PlanetMemberApiApi.md#api_members_id_authority_get) | **GET** /api/members/{id}/authority | 
[**api_members_id_delete**](PlanetMemberApiApi.md#api_members_id_delete) | **DELETE** /api/members/{id} | 
[**api_members_id_get**](PlanetMemberApiApi.md#api_members_id_get) | **GET** /api/members/{id} | 
[**api_members_id_put**](PlanetMemberApiApi.md#api_members_id_put) | **PUT** /api/members/{id} | 
[**api_members_id_roles_get**](PlanetMemberApiApi.md#api_members_id_roles_get) | **GET** /api/members/{id}/roles | 
[**api_members_id_roles_role_id_delete**](PlanetMemberApiApi.md#api_members_id_roles_role_id_delete) | **DELETE** /api/members/{id}/roles/{roleId} | 
[**api_members_id_roles_role_id_post**](PlanetMemberApiApi.md#api_members_id_roles_role_id_post) | **POST** /api/members/{id}/roles/{roleId} | 
[**api_members_self_planet_id_get**](PlanetMemberApiApi.md#api_members_self_planet_id_get) | **GET** /api/members/self/{planetId} | 

# **api_members_byuser_planet_id_user_id_get**
> api_members_byuser_planet_id_user_id_get(planet_id, user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
planet_id = 789 # int | 
user_id = 789 # int | 

try:
    api_instance.api_members_byuser_planet_id_user_id_get(planet_id, user_id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_byuser_planet_id_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_authority_get**
> api_members_id_authority_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 

try:
    api_instance.api_members_id_authority_get(id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_authority_get: %s\n" % e)
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

# **api_members_id_delete**
> api_members_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 

try:
    api_instance.api_members_id_delete(id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_delete: %s\n" % e)
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

# **api_members_id_get**
> api_members_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 

try:
    api_instance.api_members_id_get(id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_get: %s\n" % e)
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

# **api_members_id_put**
> api_members_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 
body = swagger_client.PlanetMember() # PlanetMember |  (optional)

try:
    api_instance.api_members_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**PlanetMember**](PlanetMember.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_roles_get**
> api_members_id_roles_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 

try:
    api_instance.api_members_id_roles_get(id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_roles_get: %s\n" % e)
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

# **api_members_id_roles_role_id_delete**
> api_members_id_roles_role_id_delete(id, role_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 
role_id = 789 # int | 

try:
    api_instance.api_members_id_roles_role_id_delete(id, role_id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_roles_role_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **role_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_roles_role_id_post**
> api_members_id_roles_role_id_post(id, role_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
id = 789 # int | 
role_id = 789 # int | 

try:
    api_instance.api_members_id_roles_role_id_post(id, role_id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_id_roles_role_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **role_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_self_planet_id_get**
> api_members_self_planet_id_get(planet_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetMemberApiApi()
planet_id = 789 # int | 

try:
    api_instance.api_members_self_planet_id_get(planet_id)
except ApiException as e:
    print("Exception when calling PlanetMemberApiApi->api_members_self_planet_id_get: %s\n" % e)
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

