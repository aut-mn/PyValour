# swagger_client.UserApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_by_name_name_get**](UserApiApi.md#api_users_by_name_name_get) | **GET** /api/users/byName/{name} | 
[**api_users_count_get**](UserApiApi.md#api_users_count_get) | **GET** /api/users/count | 
[**api_users_id_frienddata_get**](UserApiApi.md#api_users_id_frienddata_get) | **GET** /api/users/{id}/frienddata | 
[**api_users_id_friends_get**](UserApiApi.md#api_users_id_friends_get) | **GET** /api/users/{id}/friends | 
[**api_users_id_get**](UserApiApi.md#api_users_id_get) | **GET** /api/users/{id} | 
[**api_users_id_put**](UserApiApi.md#api_users_id_put) | **PUT** /api/users/{id} | 
[**api_users_new_count_get**](UserApiApi.md#api_users_new_count_get) | **GET** /api/users/new/{count} | 
[**api_users_ping_get**](UserApiApi.md#api_users_ping_get) | **GET** /api/users/ping | 
[**api_users_register_post**](UserApiApi.md#api_users_register_post) | **POST** /api/users/register | 
[**api_users_resendemail_post**](UserApiApi.md#api_users_resendemail_post) | **POST** /api/users/resendemail | 
[**api_users_resetpassword_post**](UserApiApi.md#api_users_resetpassword_post) | **POST** /api/users/resetpassword | 
[**api_users_self_channelstates_get**](UserApiApi.md#api_users_self_channelstates_get) | **GET** /api/users/self/channelstates | 
[**api_users_self_compliance_birth_date_locality_post**](UserApiApi.md#api_users_self_compliance_birth_date_locality_post) | **POST** /api/users/self/compliance/{birthDate}/{locality} | 
[**api_users_self_get**](UserApiApi.md#api_users_self_get) | **GET** /api/users/self | 
[**api_users_self_hard_delete_post**](UserApiApi.md#api_users_self_hard_delete_post) | **POST** /api/users/self/hardDelete | 
[**api_users_self_logout_post**](UserApiApi.md#api_users_self_logout_post) | **POST** /api/users/self/logout | 
[**api_users_self_planetids_get**](UserApiApi.md#api_users_self_planetids_get) | **GET** /api/users/self/planetids | 
[**api_users_self_planets_get**](UserApiApi.md#api_users_self_planets_get) | **GET** /api/users/self/planets | 
[**api_users_self_recovery_post**](UserApiApi.md#api_users_self_recovery_post) | **POST** /api/users/self/recovery | 
[**api_users_self_referrals_get**](UserApiApi.md#api_users_self_referrals_get) | **GET** /api/users/self/referrals | 
[**api_users_self_statedata_get**](UserApiApi.md#api_users_self_statedata_get) | **GET** /api/users/self/statedata | 
[**api_users_self_tenorfavorites_get**](UserApiApi.md#api_users_self_tenorfavorites_get) | **GET** /api/users/self/tenorfavorites | 
[**api_users_token_post**](UserApiApi.md#api_users_token_post) | **POST** /api/users/token | 
[**api_users_verify_code_get**](UserApiApi.md#api_users_verify_code_get) | **GET** /api/users/verify/{code} | 

# **api_users_by_name_name_get**
> api_users_by_name_name_get(name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
name = 'name_example' # str | 

try:
    api_instance.api_users_by_name_name_get(name)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_by_name_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_count_get**
> api_users_count_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_count_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_count_get: %s\n" % e)
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

# **api_users_id_frienddata_get**
> api_users_id_frienddata_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
id = 789 # int | 

try:
    api_instance.api_users_id_frienddata_get(id)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_id_frienddata_get: %s\n" % e)
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

# **api_users_id_friends_get**
> api_users_id_friends_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
id = 789 # int | 

try:
    api_instance.api_users_id_friends_get(id)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_id_friends_get: %s\n" % e)
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

# **api_users_id_get**
> api_users_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
id = 789 # int | 

try:
    api_instance.api_users_id_get(id)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_id_get: %s\n" % e)
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

# **api_users_id_put**
> api_users_id_put(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.User() # User |  (optional)

try:
    api_instance.api_users_id_put(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_new_count_get**
> api_users_new_count_get(count)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
count = 56 # int | 

try:
    api_instance.api_users_new_count_get(count)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_new_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_ping_get**
> api_users_ping_get(is_mobile=is_mobile)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
is_mobile = false # bool |  (optional) (default to false)

try:
    api_instance.api_users_ping_get(is_mobile=is_mobile)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_ping_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_mobile** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_register_post**
> api_users_register_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.RegisterUserRequest() # RegisterUserRequest |  (optional)

try:
    api_instance.api_users_register_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_resendemail_post**
> api_users_resendemail_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.RegisterUserRequest() # RegisterUserRequest |  (optional)

try:
    api_instance.api_users_resendemail_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_resendemail_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_resetpassword_post**
> api_users_resetpassword_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_users_resetpassword_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_resetpassword_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_self_channelstates_get**
> api_users_self_channelstates_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_channelstates_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_channelstates_get: %s\n" % e)
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

# **api_users_self_compliance_birth_date_locality_post**
> api_users_self_compliance_birth_date_locality_post(birth_date, locality)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
birth_date = '2013-10-20T19:20:30+01:00' # datetime | 
locality = 'locality_example' # str | 

try:
    api_instance.api_users_self_compliance_birth_date_locality_post(birth_date, locality)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_compliance_birth_date_locality_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **birth_date** | **datetime**|  | 
 **locality** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_self_get**
> api_users_self_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_get: %s\n" % e)
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

# **api_users_self_hard_delete_post**
> api_users_self_hard_delete_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.DeleteAccountModel() # DeleteAccountModel |  (optional)

try:
    api_instance.api_users_self_hard_delete_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_hard_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAccountModel**](DeleteAccountModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_self_logout_post**
> api_users_self_logout_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_logout_post()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_logout_post: %s\n" % e)
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

# **api_users_self_planetids_get**
> api_users_self_planetids_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_planetids_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_planetids_get: %s\n" % e)
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

# **api_users_self_planets_get**
> api_users_self_planets_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_planets_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_planets_get: %s\n" % e)
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

# **api_users_self_recovery_post**
> api_users_self_recovery_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.PasswordRecoveryRequest() # PasswordRecoveryRequest |  (optional)

try:
    api_instance.api_users_self_recovery_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_recovery_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordRecoveryRequest**](PasswordRecoveryRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_self_referrals_get**
> api_users_self_referrals_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_referrals_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_referrals_get: %s\n" % e)
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

# **api_users_self_statedata_get**
> api_users_self_statedata_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_statedata_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_statedata_get: %s\n" % e)
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

# **api_users_self_tenorfavorites_get**
> api_users_self_tenorfavorites_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()

try:
    api_instance.api_users_self_tenorfavorites_get()
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_self_tenorfavorites_get: %s\n" % e)
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

# **api_users_token_post**
> api_users_token_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
body = swagger_client.TokenRequest() # TokenRequest |  (optional)

try:
    api_instance.api_users_token_post(body=body)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequest**](TokenRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_verify_code_get**
> api_users_verify_code_get(code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApiApi()
code = 'code_example' # str | 

try:
    api_instance.api_users_verify_code_get(code)
except ApiException as e:
    print("Exception when calling UserApiApi->api_users_verify_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

