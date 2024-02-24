# swagger_client.UploadApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_app_app_id_post**](UploadApiApi.md#upload_app_app_id_post) | **POST** /upload/app/{appId} | 
[**upload_file_plus_post**](UploadApiApi.md#upload_file_plus_post) | **POST** /upload/file/plus | 
[**upload_file_post**](UploadApiApi.md#upload_file_post) | **POST** /upload/file | 
[**upload_image_plus_post**](UploadApiApi.md#upload_image_plus_post) | **POST** /upload/image/plus | 
[**upload_image_post**](UploadApiApi.md#upload_image_post) | **POST** /upload/image | 
[**upload_planet_planet_id_post**](UploadApiApi.md#upload_planet_planet_id_post) | **POST** /upload/planet/{planetId} | 
[**upload_profile_post**](UploadApiApi.md#upload_profile_post) | **POST** /upload/profile | 
[**upload_profilebg_post**](UploadApiApi.md#upload_profilebg_post) | **POST** /upload/profilebg | 

# **upload_app_app_id_post**
> upload_app_app_id_post(app_id, uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
app_id = 789 # int | 
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_app_app_id_post(app_id, uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_app_app_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_plus_post**
> upload_file_plus_post(uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_file_plus_post(uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_file_plus_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_post**
> upload_file_post(uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_file_post(uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image_plus_post**
> upload_image_plus_post(uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_image_plus_post(uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_image_plus_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image_post**
> upload_image_post(uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_image_post(uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_planet_planet_id_post**
> upload_planet_planet_id_post(planet_id, uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
planet_id = 789 # int | 
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_planet_planet_id_post(planet_id, uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_planet_planet_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet_id** | **int**|  | 
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_profile_post**
> upload_profile_post(uploaded_file=uploaded_file)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)

try:
    api_instance.upload_profile_post(uploaded_file=uploaded_file)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_profile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_profilebg_post**
> upload_profilebg_post(uploaded_file=uploaded_file, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApiApi()
uploaded_file = '/path/to/file' # file |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.upload_profilebg_post(uploaded_file=uploaded_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling UploadApiApi->upload_profilebg_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_file** | [**file**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

