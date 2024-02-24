# swagger_client.EcoApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_eco_accounts_byname_username_get**](EcoApiApi.md#api_eco_accounts_byname_username_get) | **GET** /api/eco/accounts/byname/{username} | 
[**api_eco_accounts_id_delete**](EcoApiApi.md#api_eco_accounts_id_delete) | **DELETE** /api/eco/accounts/{id} | 
[**api_eco_accounts_id_get**](EcoApiApi.md#api_eco_accounts_id_get) | **GET** /api/eco/accounts/{id} | 
[**api_eco_accounts_id_put**](EcoApiApi.md#api_eco_accounts_id_put) | **PUT** /api/eco/accounts/{id} | 
[**api_eco_accounts_planet_can_send_post**](EcoApiApi.md#api_eco_accounts_planet_can_send_post) | **POST** /api/eco/accounts/planet/canSend | 
[**api_eco_accounts_planet_planet_id_byuser_user_id_get**](EcoApiApi.md#api_eco_accounts_planet_planet_id_byuser_user_id_get) | **GET** /api/eco/accounts/planet/{planetId}/byuser/{userId} | 
[**api_eco_accounts_planet_planet_id_member_get**](EcoApiApi.md#api_eco_accounts_planet_planet_id_member_get) | **GET** /api/eco/accounts/planet/{planetId}/member | 
[**api_eco_accounts_planet_planet_id_planet_get**](EcoApiApi.md#api_eco_accounts_planet_planet_id_planet_get) | **GET** /api/eco/accounts/planet/{planetId}/planet | 
[**api_eco_accounts_planet_planet_id_user_get**](EcoApiApi.md#api_eco_accounts_planet_planet_id_user_get) | **GET** /api/eco/accounts/planet/{planetId}/user | 
[**api_eco_accounts_post**](EcoApiApi.md#api_eco_accounts_post) | **POST** /api/eco/accounts | 
[**api_eco_accounts_self_get**](EcoApiApi.md#api_eco_accounts_self_get) | **GET** /api/eco/accounts/self | 
[**api_eco_accounts_self_global_get**](EcoApiApi.md#api_eco_accounts_self_global_get) | **GET** /api/eco/accounts/self/global | 
[**api_eco_currencies_by_planet_planet_id_get**](EcoApiApi.md#api_eco_currencies_by_planet_planet_id_get) | **GET** /api/eco/currencies/byPlanet/{planetId} | 
[**api_eco_currencies_id_get**](EcoApiApi.md#api_eco_currencies_id_get) | **GET** /api/eco/currencies/{id} | 
[**api_eco_currencies_id_put**](EcoApiApi.md#api_eco_currencies_id_put) | **PUT** /api/eco/currencies/{id} | 
[**api_eco_currencies_post**](EcoApiApi.md#api_eco_currencies_post) | **POST** /api/eco/currencies | 
[**api_eco_transactions_id_get**](EcoApiApi.md#api_eco_transactions_id_get) | **GET** /api/eco/transactions/{id} | 
[**api_eco_transactions_id_receipt_get**](EcoApiApi.md#api_eco_transactions_id_receipt_get) | **GET** /api/eco/transactions/{id}/receipt | 
[**api_eco_transactions_post**](EcoApiApi.md#api_eco_transactions_post) | **POST** /api/eco/transactions | 

# **api_eco_accounts_byname_username_get**
> api_eco_accounts_byname_username_get(username)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
username = 'username_example' # str | 

try:
    api_instance.api_eco_accounts_byname_username_get(username)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_byname_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_id_delete**
> api_eco_accounts_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 789 # int | 

try:
    api_instance.api_eco_accounts_id_delete(id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_id_delete: %s\n" % e)
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

# **api_eco_accounts_id_get**
> api_eco_accounts_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 789 # int | 

try:
    api_instance.api_eco_accounts_id_get(id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_id_get: %s\n" % e)
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

# **api_eco_accounts_id_put**
> api_eco_accounts_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 789 # int | 
body = swagger_client.EcoAccount() # EcoAccount |  (optional)

try:
    api_instance.api_eco_accounts_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EcoAccount**](EcoAccount.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_planet_can_send_post**
> api_eco_accounts_planet_can_send_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
body = swagger_client.EcoPlanetAccountSearchRequest() # EcoPlanetAccountSearchRequest |  (optional)

try:
    api_instance.api_eco_accounts_planet_can_send_post(body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_planet_can_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EcoPlanetAccountSearchRequest**](EcoPlanetAccountSearchRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_planet_planet_id_byuser_user_id_get**
> api_eco_accounts_planet_planet_id_byuser_user_id_get(planet_id, user_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
planet_id = 789 # int | 
user_id = 789 # int | 

try:
    api_instance.api_eco_accounts_planet_planet_id_byuser_user_id_get(planet_id, user_id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_planet_planet_id_byuser_user_id_get: %s\n" % e)
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

# **api_eco_accounts_planet_planet_id_member_get**
> api_eco_accounts_planet_planet_id_member_get(planet_id, skip=skip, take=take)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
planet_id = 789 # int | 
skip = 0 # int |  (optional) (default to 0)
take = 50 # int |  (optional) (default to 50)

try:
    api_instance.api_eco_accounts_planet_planet_id_member_get(planet_id, skip=skip, take=take)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_planet_planet_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_planet_planet_id_planet_get**
> api_eco_accounts_planet_planet_id_planet_get(planet_id, skip=skip, take=take)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
planet_id = 789 # int | 
skip = 0 # int |  (optional) (default to 0)
take = 50 # int |  (optional) (default to 50)

try:
    api_instance.api_eco_accounts_planet_planet_id_planet_get(planet_id, skip=skip, take=take)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_planet_planet_id_planet_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_planet_planet_id_user_get**
> api_eco_accounts_planet_planet_id_user_get(planet_id, skip=skip, take=take)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
planet_id = 789 # int | 
skip = 0 # int |  (optional) (default to 0)
take = 50 # int |  (optional) (default to 50)

try:
    api_instance.api_eco_accounts_planet_planet_id_user_get(planet_id, skip=skip, take=take)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_planet_planet_id_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_post**
> api_eco_accounts_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
body = swagger_client.EcoAccount() # EcoAccount |  (optional)

try:
    api_instance.api_eco_accounts_post(body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EcoAccount**](EcoAccount.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_accounts_self_get**
> api_eco_accounts_self_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()

try:
    api_instance.api_eco_accounts_self_get()
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_self_get: %s\n" % e)
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

# **api_eco_accounts_self_global_get**
> api_eco_accounts_self_global_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()

try:
    api_instance.api_eco_accounts_self_global_get()
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_accounts_self_global_get: %s\n" % e)
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

# **api_eco_currencies_by_planet_planet_id_get**
> api_eco_currencies_by_planet_planet_id_get(planet_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
planet_id = 789 # int | 

try:
    api_instance.api_eco_currencies_by_planet_planet_id_get(planet_id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_currencies_by_planet_planet_id_get: %s\n" % e)
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

# **api_eco_currencies_id_get**
> api_eco_currencies_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 789 # int | 

try:
    api_instance.api_eco_currencies_id_get(id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_currencies_id_get: %s\n" % e)
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

# **api_eco_currencies_id_put**
> api_eco_currencies_id_put(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 789 # int | 
body = swagger_client.Currency() # Currency |  (optional)

try:
    api_instance.api_eco_currencies_id_put(id, body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_currencies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Currency**](Currency.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_currencies_post**
> api_eco_currencies_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
body = swagger_client.Currency() # Currency |  (optional)

try:
    api_instance.api_eco_currencies_post(body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_currencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Currency**](Currency.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_transactions_id_get**
> api_eco_transactions_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 'id_example' # str | 

try:
    api_instance.api_eco_transactions_id_get(id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_transactions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_transactions_id_receipt_get**
> api_eco_transactions_id_receipt_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
id = 'id_example' # str | 

try:
    api_instance.api_eco_transactions_id_receipt_get(id)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_transactions_id_receipt_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_eco_transactions_post**
> api_eco_transactions_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EcoApiApi()
body = swagger_client.Transaction() # Transaction |  (optional)

try:
    api_instance.api_eco_transactions_post(body=body)
except ApiException as e:
    print("Exception when calling EcoApiApi->api_eco_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transaction**](Transaction.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

