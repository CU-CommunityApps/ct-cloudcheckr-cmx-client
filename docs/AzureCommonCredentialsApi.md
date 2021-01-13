# cloudcheckr_cmx_client.AzureCommonCredentialsApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_billing_account**](AzureCommonCredentialsApi.md#assign_billing_account) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credential/azure/billing-accounts | Assigns a billing account ID to an Azure credential.
[**get_billing_accounts**](AzureCommonCredentialsApi.md#get_billing_accounts) | **GET** /credential/v1/customers/{customerId}/accounts/{accountId}/credential/azure/billing-accounts | Retrieve billing accounts associated with credential.
[**request_authorization**](AzureCommonCredentialsApi.md#request_authorization) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/azure/request-authorization | Start the Azure authorization consent flow.

# **assign_billing_account**
> CredentialResponseModel assign_billing_account(customer_id, account_id, body=body)

Assigns a billing account ID to an Azure credential.

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
api_instance = cloudcheckr_cmx_client.AzureCommonCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.CreateRequestAzureBillingAccountSelectionRequestModel() # CreateRequestAzureBillingAccountSelectionRequestModel |  (optional)

try:
    # Assigns a billing account ID to an Azure credential.
    api_response = api_instance.assign_billing_account(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCommonCredentialsApi->assign_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**CreateRequestAzureBillingAccountSelectionRequestModel**](CreateRequestAzureBillingAccountSelectionRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_accounts**
> PaginationResponseAzureBillingAccountResponseModel get_billing_accounts(customer_id, account_id, pagination_key=pagination_key)

Retrieve billing accounts associated with credential.

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
api_instance = cloudcheckr_cmx_client.AzureCommonCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)

try:
    # Retrieve billing accounts associated with credential.
    api_response = api_instance.get_billing_accounts(customer_id, account_id, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCommonCredentialsApi->get_billing_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 

### Return type

[**PaginationResponseAzureBillingAccountResponseModel**](PaginationResponseAzureBillingAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_authorization**
> AzureAuthorizationResponseModel request_authorization(customer_id, account_id, body=body)

Start the Azure authorization consent flow.

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
api_instance = cloudcheckr_cmx_client.AzureCommonCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAzureTokenCredentialRequestModel() # UpdateRequestAzureTokenCredentialRequestModel |  (optional)

try:
    # Start the Azure authorization consent flow.
    api_response = api_instance.request_authorization(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCommonCredentialsApi->request_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAzureTokenCredentialRequestModel**](UpdateRequestAzureTokenCredentialRequestModel.md)|  | [optional] 

### Return type

[**AzureAuthorizationResponseModel**](AzureAuthorizationResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

