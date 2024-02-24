# swagger_client.PlanetInviteApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_invites_id_delete**](PlanetInviteApiApi.md#api_invites_id_delete) | **DELETE** /api/invites/{id} | 
[**api_invites_id_put**](PlanetInviteApiApi.md#api_invites_id_put) | **PUT** /api/invites/{id} | 
[**api_invites_invite_code_get**](PlanetInviteApiApi.md#api_invites_invite_code_get) | **GET** /api/invites/{inviteCode} | 
[**api_invites_invite_code_planeticon_get**](PlanetInviteApiApi.md#api_invites_invite_code_planeticon_get) | **GET** /api/invites/{inviteCode}/planeticon | 
[**api_invites_invite_code_planetname_get**](PlanetInviteApiApi.md#api_invites_invite_code_planetname_get) | **GET** /api/invites/{inviteCode}/planetname | 
[**api_invites_invite_code_screen_get**](PlanetInviteApiApi.md#api_invites_invite_code_screen_get) | **GET** /api/invites/{inviteCode}/screen | 
[**api_invites_post**](PlanetInviteApiApi.md#api_invites_post) | **POST** /api/invites | 

# **api_invites_id_delete**
> api_invites_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
id = 789 # int | 

try:
    api_instance.api_invites_id_delete(id)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_id_delete: %s\n" % e)
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

# **api_invites_id_put**
> api_invites_id_put(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
body = swagger_client.PlanetInvite() # PlanetInvite |  (optional)

try:
    api_instance.api_invites_id_put(body=body)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanetInvite**](PlanetInvite.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invites_invite_code_get**
> api_invites_invite_code_get(invite_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
invite_code = 'invite_code_example' # str | 

try:
    api_instance.api_invites_invite_code_get(invite_code)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_invite_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invites_invite_code_planeticon_get**
> api_invites_invite_code_planeticon_get(invite_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
invite_code = 'invite_code_example' # str | 

try:
    api_instance.api_invites_invite_code_planeticon_get(invite_code)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_invite_code_planeticon_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invites_invite_code_planetname_get**
> api_invites_invite_code_planetname_get(invite_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
invite_code = 'invite_code_example' # str | 

try:
    api_instance.api_invites_invite_code_planetname_get(invite_code)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_invite_code_planetname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invites_invite_code_screen_get**
> api_invites_invite_code_screen_get(invite_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
invite_code = 'invite_code_example' # str | 

try:
    api_instance.api_invites_invite_code_screen_get(invite_code)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_invite_code_screen_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invites_post**
> api_invites_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanetInviteApiApi()
body = swagger_client.PlanetInvite() # PlanetInvite |  (optional)

try:
    api_instance.api_invites_post(body=body)
except ApiException as e:
    print("Exception when calling PlanetInviteApiApi->api_invites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanetInvite**](PlanetInvite.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

