# swagger_client.PlanetApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_planets_discoverable_get**](PlanetApiApi.md#api_planets_discoverable_get) | **GET** /api/planets/discoverable | 
[**api_planets_id_categories_get**](PlanetApiApi.md#api_planets_id_categories_get) | **GET** /api/planets/{id}/categories | 
[**api_planets_id_channels_chat_get**](PlanetApiApi.md#api_planets_id_channels_chat_get) | **GET** /api/planets/{id}/channels/chat | 
[**api_planets_id_channels_get**](PlanetApiApi.md#api_planets_id_channels_get) | **GET** /api/planets/{id}/channels | 
[**api_planets_id_channels_voice_get**](PlanetApiApi.md#api_planets_id_channels_voice_get) | **GET** /api/planets/{id}/channels/voice | 
[**api_planets_id_delete**](PlanetApiApi.md#api_planets_id_delete) | **DELETE** /api/planets/{id} | 
[**api_planets_id_discover_post**](PlanetApiApi.md#api_planets_id_discover_post) | **POST** /api/planets/{id}/discover | 
[**api_planets_id_get**](PlanetApiApi.md#api_planets_id_get) | **GET** /api/planets/{id} | 
[**api_planets_id_invites_get**](PlanetApiApi.md#api_planets_id_invites_get) | **GET** /api/planets/{id}/invites | 
[**api_planets_id_invites_ids_get**](PlanetApiApi.md#api_planets_id_invites_ids_get) | **GET** /api/planets/{id}/invites/ids | 
[**api_planets_id_join_post**](PlanetApiApi.md#api_planets_id_join_post) | **POST** /api/planets/{id}/join | 
[**api_planets_id_memberinfo_get**](PlanetApiApi.md#api_planets_id_memberinfo_get) | **GET** /api/planets/{id}/memberinfo | 
[**api_planets_id_put**](PlanetApiApi.md#api_planets_id_put) | **PUT** /api/planets/{id} | 
[**api_planets_id_roles_get**](PlanetApiApi.md#api_planets_id_roles_get) | **GET** /api/planets/{id}/roles | 
[**api_planets_id_roles_ids_get**](PlanetApiApi.md#api_planets_id_roles_ids_get) | **GET** /api/planets/{id}/roles/ids | 
[**api_planets_id_roles_order_post**](PlanetApiApi.md#api_planets_id_roles_order_post) | **POST** /api/planets/{id}/roles/order | 
[**api_planets_planet_id_planet_channels_insert_post**](PlanetApiApi.md#api_planets_planet_id_planet_channels_insert_post) | **POST** /api/planets/{planetId}/planetChannels/insert | 
[**api_planets_planet_id_planet_channels_order_post**](PlanetApiApi.md#api_planets_planet_id_planet_channels_order_post) | **POST** /api/planets/{planetId}/planetChannels/order | 
[**api_planets_post**](PlanetApiApi.md#api_planets_post) | **POST** /api/planets | 

# **api_planets_discoverable_get**
> api_planets_discoverable_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()

try:
    api_instance.api_planets_discoverable_get()
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_discoverable_get: %s\n" % e)
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

# **api_planets_id_categories_get**
> api_planets_id_categories_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_categories_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_categories_get: %s\n" % e)
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

# **api_planets_id_channels_chat_get**
> api_planets_id_channels_chat_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_channels_chat_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_channels_chat_get: %s\n" % e)
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

# **api_planets_id_channels_get**
> api_planets_id_channels_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_channels_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_channels_get: %s\n" % e)
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

# **api_planets_id_channels_voice_get**
> api_planets_id_channels_voice_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_channels_voice_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_channels_voice_get: %s\n" % e)
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

# **api_planets_id_delete**
> api_planets_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_delete(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_delete: %s\n" % e)
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

# **api_planets_id_discover_post**
> api_planets_id_discover_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_discover_post(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_discover_post: %s\n" % e)
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

# **api_planets_id_get**
> api_planets_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_get: %s\n" % e)
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

# **api_planets_id_invites_get**
> api_planets_id_invites_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_invites_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_invites_get: %s\n" % e)
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

# **api_planets_id_invites_ids_get**
> api_planets_id_invites_ids_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_invites_ids_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_invites_ids_get: %s\n" % e)
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

# **api_planets_id_join_post**
> api_planets_id_join_post(id, invite_code=invite_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 
invite_code = 'invite_code_example' # str |  (optional)

try:
    api_instance.api_planets_id_join_post(id, invite_code=invite_code)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **invite_code** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_id_memberinfo_get**
> api_planets_id_memberinfo_get(id, page=page)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 
page = 0 # int |  (optional) (default to 0)

try:
    api_instance.api_planets_id_memberinfo_get(id, page=page)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_memberinfo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_id_put**
> api_planets_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 
body = swagger_client.Planet() # Planet |  (optional)

try:
    api_instance.api_planets_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Planet**](Planet.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_id_roles_get**
> api_planets_id_roles_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_roles_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_roles_get: %s\n" % e)
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

# **api_planets_id_roles_ids_get**
> api_planets_id_roles_ids_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 

try:
    api_instance.api_planets_id_roles_ids_get(id)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_roles_ids_get: %s\n" % e)
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

# **api_planets_id_roles_order_post**
> api_planets_id_roles_order_post(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
id = 789 # int | 
body = [56] # list[int] |  (optional)

try:
    api_instance.api_planets_id_roles_order_post(id, body=body)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_id_roles_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_planet_id_planet_channels_insert_post**
> api_planets_planet_id_planet_channels_insert_post(planet_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
planet_id = 789 # int | 
body = swagger_client.InsertChannelChildModel() # InsertChannelChildModel |  (optional)

try:
    api_instance.api_planets_planet_id_planet_channels_insert_post(planet_id, body=body)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_planet_id_planet_channels_insert_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **body** | [**InsertChannelChildModel**](InsertChannelChildModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_planet_id_planet_channels_order_post**
> api_planets_planet_id_planet_channels_order_post(planet_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
planet_id = 789 # int | 
body = swagger_client.OrderChannelsModel() # OrderChannelsModel |  (optional)

try:
    api_instance.api_planets_planet_id_planet_channels_order_post(planet_id, body=body)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_planet_id_planet_channels_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **body** | [**OrderChannelsModel**](OrderChannelsModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_planets_post**
> api_planets_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetApiApi()
body = swagger_client.Planet() # Planet |  (optional)

try:
    api_instance.api_planets_post(body=body)
except ApiException as e:
    print("Exception when calling PlanetApiApi->api_planets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Planet**](Planet.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

