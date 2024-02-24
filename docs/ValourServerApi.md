# swagger_client.ValourServerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_node_handshake_get**](ValourServerApi.md#api_node_handshake_get) | **GET** /api/node/handshake | 
[**api_node_name_get**](ValourServerApi.md#api_node_name_get) | **GET** /api/node/name | 
[**api_node_planet_id_get**](ValourServerApi.md#api_node_planet_id_get) | **GET** /api/node/planet/{id} | 
[**api_nodestats_detailed_get**](ValourServerApi.md#api_nodestats_detailed_get) | **GET** /api/nodestats/detailed | 
[**api_nodestats_get**](ValourServerApi.md#api_nodestats_get) | **GET** /api/nodestats | 
[**api_ping_get**](ValourServerApi.md#api_ping_get) | **GET** /api/ping | 
[**api_version_get**](ValourServerApi.md#api_version_get) | **GET** /api/version | 

# **api_node_handshake_get**
> NodeHandshakeResponse api_node_handshake_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_response = api_instance.api_node_handshake_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_node_handshake_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeHandshakeResponse**](NodeHandshakeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_node_name_get**
> str api_node_name_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_response = api_instance.api_node_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_node_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_node_planet_id_get**
> api_node_planet_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()
id = 789 # int | 

try:
    api_instance.api_node_planet_id_get(id)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_node_planet_id_get: %s\n" % e)
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

# **api_nodestats_detailed_get**
> api_nodestats_detailed_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_instance.api_nodestats_detailed_get()
except ApiException as e:
    print("Exception when calling ValourServerApi->api_nodestats_detailed_get: %s\n" % e)
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

# **api_nodestats_get**
> NodeStats api_nodestats_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_response = api_instance.api_nodestats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_nodestats_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStats**](NodeStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ping_get**
> str api_ping_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_response = api_instance.api_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_version_get**
> str api_version_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValourServerApi()

try:
    api_response = api_instance.api_version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValourServerApi->api_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

