# cloudcheckr_cmx_client.GoogleCredentialsApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_google_credential**](GoogleCredentialsApi.md#modify_google_credential) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/google | Modify the default credential on the account.

# **modify_google_credential**
> CredentialResponseModel modify_google_credential(customer_id, account_id, body=body)

Modify the default credential on the account.

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
api_instance = cloudcheckr_cmx_client.GoogleCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestGoogleCredentialRequestModel() # UpdateRequestGoogleCredentialRequestModel |  (optional)

try:
    # Modify the default credential on the account.
    api_response = api_instance.modify_google_credential(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleCredentialsApi->modify_google_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestGoogleCredentialRequestModel**](UpdateRequestGoogleCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

