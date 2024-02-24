# swagger_client.EmbedAPIApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_embed_interact_post**](EmbedAPIApi.md#api_embed_interact_post) | **POST** /api/embed/interact | 
[**api_embed_planetchannelupdate_post**](EmbedAPIApi.md#api_embed_planetchannelupdate_post) | **POST** /api/embed/planetchannelupdate | 
[**api_embed_planetpersonalupdate_post**](EmbedAPIApi.md#api_embed_planetpersonalupdate_post) | **POST** /api/embed/planetpersonalupdate | 

# **api_embed_interact_post**
> api_embed_interact_post(authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmbedAPIApi()
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_embed_interact_post(authorization=authorization)
except ApiException as e:
    print("Exception when calling EmbedAPIApi->api_embed_interact_post: %s\n" % e)
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

# **api_embed_planetchannelupdate_post**
> api_embed_planetchannelupdate_post(authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmbedAPIApi()
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_embed_planetchannelupdate_post(authorization=authorization)
except ApiException as e:
    print("Exception when calling EmbedAPIApi->api_embed_planetchannelupdate_post: %s\n" % e)
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

# **api_embed_planetpersonalupdate_post**
> api_embed_planetpersonalupdate_post(authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmbedAPIApi()
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.api_embed_planetpersonalupdate_post(authorization=authorization)
except ApiException as e:
    print("Exception when calling EmbedAPIApi->api_embed_planetpersonalupdate_post: %s\n" % e)
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

