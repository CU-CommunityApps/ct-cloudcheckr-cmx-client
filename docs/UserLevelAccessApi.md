# cloudcheckr_cmx_client.UserLevelAccessApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_level_access**](UserLevelAccessApi.md#get_user_level_access) | **GET** /policy/v1/customers/{customerId}/user-level-access/{userId} | Get user-level access for a single user.
[**update_user_level_access**](UserLevelAccessApi.md#update_user_level_access) | **PUT** /policy/v1/customers/{customerId}/user-level-access/{userId} | Updates the user-level access for the given user.

# **get_user_level_access**
> UserLevelAccessResponseModel get_user_level_access(customer_id, user_id)

Get user-level access for a single user.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx_client
from cloudcheckr_cmx_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx_client.UserLevelAccessApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Get user-level access for a single user.
    api_response = api_instance.get_user_level_access(customer_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLevelAccessApi->get_user_level_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserLevelAccessResponseModel**](UserLevelAccessResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_level_access**
> UserLevelAccessResponseModel update_user_level_access(customer_id, user_id, body=body)

Updates the user-level access for the given user.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx_client
from cloudcheckr_cmx_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx_client.UserLevelAccessApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestUserLevelAccessRequestModel() # UpdateRequestUserLevelAccessRequestModel |  (optional)

try:
    # Updates the user-level access for the given user.
    api_response = api_instance.update_user_level_access(customer_id, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserLevelAccessApi->update_user_level_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 
 **body** | [**UpdateRequestUserLevelAccessRequestModel**](UpdateRequestUserLevelAccessRequestModel.md)|  | [optional] 

### Return type

[**UserLevelAccessResponseModel**](UserLevelAccessResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

