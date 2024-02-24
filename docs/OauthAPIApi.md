# swagger_client.OauthAPIApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_oauth_app_app_id_delete**](OauthAPIApi.md#api_oauth_app_app_id_delete) | **DELETE** /api/oauth/app/{app_id} | 
[**api_oauth_app_app_id_get**](OauthAPIApi.md#api_oauth_app_app_id_get) | **GET** /api/oauth/app/{app_id} | 
[**api_oauth_app_post**](OauthAPIApi.md#api_oauth_app_post) | **POST** /api/oauth/app | 
[**api_oauth_app_public_app_id_get**](OauthAPIApi.md#api_oauth_app_public_app_id_get) | **GET** /api/oauth/app/public/{app_id} | 
[**api_oauth_authorize_post**](OauthAPIApi.md#api_oauth_authorize_post) | **POST** /api/oauth/authorize | 
[**api_oauth_token_get**](OauthAPIApi.md#api_oauth_token_get) | **GET** /api/oauth/token | 
[**api_users_user_id_apps_get**](OauthAPIApi.md#api_users_user_id_apps_get) | **GET** /api/users/{userId}/apps | 

# **api_oauth_app_app_id_delete**
> api_oauth_app_app_id_delete(app_id, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
app_id = 789 # int | 
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_oauth_app_app_id_delete(app_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_app_app_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_oauth_app_app_id_get**
> api_oauth_app_app_id_get(app_id, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
app_id = 789 # int | 
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_oauth_app_app_id_get(app_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_app_app_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_oauth_app_post**
> api_oauth_app_post(body=body, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
body = swagger_client.OauthApp() # OauthApp |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_oauth_app_post(body=body, authorization=authorization)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_app_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthApp**](OauthApp.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_oauth_app_public_app_id_get**
> api_oauth_app_public_app_id_get(app_id, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
app_id = 789 # int | 
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_oauth_app_public_app_id_get(app_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_app_public_app_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_oauth_authorize_post**
> object api_oauth_authorize_post(body=body, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
body = swagger_client.AuthorizeModel() # AuthorizeModel |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_response = api_instance.api_oauth_authorize_post(body=body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_authorize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizeModel**](AuthorizeModel.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_oauth_token_get**
> api_oauth_token_get(client_id, client_secret=client_secret, grant_type=grant_type, code=code, redirect_uri=redirect_uri, state=state)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
client_id = 789 # int | 
client_secret = 'client_secret_example' # str |  (optional)
grant_type = 'grant_type_example' # str |  (optional)
code = 'code_example' # str |  (optional)
redirect_uri = 'redirect_uri_example' # str |  (optional)
state = 'state_example' # str |  (optional)

try:
    api_instance.api_oauth_token_get(client_id, client_secret=client_secret, grant_type=grant_type, code=code, redirect_uri=redirect_uri, state=state)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_oauth_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **client_secret** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **redirect_uri** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_user_id_apps_get**
> api_users_user_id_apps_get(authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthAPIApi()
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_users_user_id_apps_get(authorization=authorization)
except ApiException as e:
    print("Exception when calling OauthAPIApi->api_users_user_id_apps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

