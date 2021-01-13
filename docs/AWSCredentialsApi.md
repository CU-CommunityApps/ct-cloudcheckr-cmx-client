# cloudcheckr_cmx_client.AWSCredentialsApi

All URIs are relative to *//api-us.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aws_external_id**](AWSCredentialsApi.md#get_aws_external_id) | **GET** /credential/v1/customers/{customerId}/accounts/{accountId}/external-id/aws/{awsRegionGroup} | Get the external ID to use when creating an AWS cross-account role.
[**modify_credential**](AWSCredentialsApi.md#modify_credential) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/aws/{purpose} | Modify the credential on the account.
[**modify_customer_aws_assume_role_credential**](AWSCredentialsApi.md#modify_customer_aws_assume_role_credential) | **PUT** /credential/v1/customers/{customerId}/credentials/aws/assume-role/{awsRegionGroup} | Set the credential to use when assuming a cross-acount role.
[**modify_default_credential**](AWSCredentialsApi.md#modify_default_credential) | **PUT** /credential/v1/customers/{customerId}/accounts/{accountId}/credentials/aws | Modify the default credential on the account.

# **get_aws_external_id**
> AwsCrossAccountRoleSetupResponseModel get_aws_external_id(customer_id, account_id, aws_region_group)

Get the external ID to use when creating an AWS cross-account role.

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
api_instance = cloudcheckr_cmx_client.AWSCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
aws_region_group = 'aws_region_group_example' # str | AWS region group where the cross-account role will be created.

try:
    # Get the external ID to use when creating an AWS cross-account role.
    api_response = api_instance.get_aws_external_id(customer_id, account_id, aws_region_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AWSCredentialsApi->get_aws_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **aws_region_group** | **str**| AWS region group where the cross-account role will be created. | 

### Return type

[**AwsCrossAccountRoleSetupResponseModel**](AwsCrossAccountRoleSetupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_credential**
> CredentialResponseModel modify_credential(customer_id, account_id, purpose, body=body)

Modify the credential on the account.

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
api_instance = cloudcheckr_cmx_client.AWSCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
purpose = 'purpose_example' # str | How the credential will be used.
body = cloudcheckr_cmx_client.UpdateRequestAwsCredentialRequestModel() # UpdateRequestAwsCredentialRequestModel |  (optional)

try:
    # Modify the credential on the account.
    api_response = api_instance.modify_credential(customer_id, account_id, purpose, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AWSCredentialsApi->modify_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **purpose** | **str**| How the credential will be used. | 
 **body** | [**UpdateRequestAwsCredentialRequestModel**](UpdateRequestAwsCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_customer_aws_assume_role_credential**
> CredentialResponseModel modify_customer_aws_assume_role_credential(customer_id, aws_region_group, body=body)

Set the credential to use when assuming a cross-acount role.

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
api_instance = cloudcheckr_cmx_client.AWSCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
aws_region_group = 'aws_region_group_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAwsAssumeRoleCredentialRequestModel() # UpdateRequestAwsAssumeRoleCredentialRequestModel |  (optional)

try:
    # Set the credential to use when assuming a cross-acount role.
    api_response = api_instance.modify_customer_aws_assume_role_credential(customer_id, aws_region_group, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AWSCredentialsApi->modify_customer_aws_assume_role_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **aws_region_group** | **str**|  | 
 **body** | [**UpdateRequestAwsAssumeRoleCredentialRequestModel**](UpdateRequestAwsAssumeRoleCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_default_credential**
> CredentialResponseModel modify_default_credential(customer_id, account_id, body=body)

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
api_instance = cloudcheckr_cmx_client.AWSCredentialsApi(cloudcheckr_cmx_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx_client.UpdateRequestAwsCredentialRequestModel() # UpdateRequestAwsCredentialRequestModel |  (optional)

try:
    # Modify the default credential on the account.
    api_response = api_instance.modify_default_credential(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AWSCredentialsApi->modify_default_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAwsCredentialRequestModel**](UpdateRequestAwsCredentialRequestModel.md)|  | [optional] 

### Return type

[**CredentialResponseModel**](CredentialResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

