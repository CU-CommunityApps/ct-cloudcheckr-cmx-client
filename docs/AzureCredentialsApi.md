# cloudcheckr_cmx_client.AzureCredentialsApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_azure_enterprise_agreement_credentials**](AzureCredentialsApi.md#modify_azure_enterprise_agreement_credentials) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/azure/enterprise-agreement | Modify the credentials on the account.
[**modify_azure_subscription_credentials**](AzureCredentialsApi.md#modify_azure_subscription_credentials) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/azure/subscription | Modify the credentials on the account.
[**request_csp_authorization**](AzureCredentialsApi.md#request_csp_authorization) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/azure/csp/request-authorization | Start the Azure CSP authorization consent flow.

# **modify_azure_enterprise_agreement_credentials**
> CredentialResponseModel modify_azure_enterprise_agreement_credentials(customer_id, account_id, body=body)

Modify the credentials on the account.

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
api_instance = cloudcheckr_cmx_client.AzureCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAzureEnterpriseAgreementCredentialRequestModel() # UpdateRequestAzureEnterpriseAgreementCredentialRequestModel |  (optional)

try:
    # Modify the credentials on the account.
    api_response = api_instance.modify_azure_enterprise_agreement_credentials(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCredentialsApi->modify_azure_enterprise_agreement_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAzureEnterpriseAgreementCredentialRequestModel**](UpdateRequestAzureEnterpriseAgreementCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_azure_subscription_credentials**
> CredentialResponseModel modify_azure_subscription_credentials(customer_id, account_id, body=body)

Modify the credentials on the account.

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
api_instance = cloudcheckr_cmx_client.AzureCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAzureSubscriptionCredentialRequestModel() # UpdateRequestAzureSubscriptionCredentialRequestModel |  (optional)

try:
    # Modify the credentials on the account.
    api_response = api_instance.modify_azure_subscription_credentials(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCredentialsApi->modify_azure_subscription_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAzureSubscriptionCredentialRequestModel**](UpdateRequestAzureSubscriptionCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_csp_authorization**
> AzureAuthorizationResponseModel request_csp_authorization(customer_id, account_id, body=body)

Start the Azure CSP authorization consent flow.

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
api_instance = cloudcheckr_cmx_client.AzureCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAzureCspAuthorizationRequestModel() # UpdateRequestAzureCspAuthorizationRequestModel |  (optional)

try:
    # Start the Azure CSP authorization consent flow.
    api_response = api_instance.request_csp_authorization(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureCredentialsApi->request_csp_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAzureCspAuthorizationRequestModel**](UpdateRequestAzureCspAuthorizationRequestModel.md)|  | [optional] 

### Return type

[**AzureAuthorizationResponseModel**](AzureAuthorizationResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

