# cloudcheckr_cmx_client.CredentialsApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_credentials**](CredentialsApi.md#get_account_credentials) | **GET** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials | Get all credentials configured on the account.
[**get_customer_credentials**](CredentialsApi.md#get_customer_credentials) | **GET** /credential/v1/customers/{customerId}/credentials | Get all credentials configured on the customer.

# **get_account_credentials**
> CredentialsResponseModel get_account_credentials(customer_id, account_id)

Get all credentials configured on the account.

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
api_instance = cloudcheckr_cmx_client.CredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Get all credentials configured on the account.
    api_response = api_instance.get_account_credentials(customer_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_account_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**CredentialsResponseModel**](CredentialsResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_credentials**
> CredentialsResponseModel get_customer_credentials(customer_id)

Get all credentials configured on the customer.

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
api_instance = cloudcheckr_cmx_client.CredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    # Get all credentials configured on the customer.
    api_response = api_instance.get_customer_credentials(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_customer_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**CredentialsResponseModel**](CredentialsResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

