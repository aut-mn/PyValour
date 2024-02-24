# swagger_client.ReportApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_reports_post**](ReportApiApi.md#api_reports_post) | **POST** /api/reports | 
[**api_reports_unreviewed_get**](ReportApiApi.md#api_reports_unreviewed_get) | **GET** /api/reports/unreviewed | 

# **api_reports_post**
> api_reports_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApiApi()
body = swagger_client.Report() # Report |  (optional)

try:
    api_instance.api_reports_post(body=body)
except ApiException as e:
    print("Exception when calling ReportApiApi->api_reports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Report**](Report.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_reports_unreviewed_get**
> api_reports_unreviewed_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApiApi()

try:
    api_instance.api_reports_unreviewed_get()
except ApiException as e:
    print("Exception when calling ReportApiApi->api_reports_unreviewed_get: %s\n" % e)
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

