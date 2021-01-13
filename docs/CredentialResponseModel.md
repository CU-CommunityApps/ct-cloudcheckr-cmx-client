# CredentialResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The account&#x27;s cloud provider. | [optional] 
**provider_sub_type** | **str** | The account&#x27;s cloud provider sub-type. | [optional] 
**provider_identifier** | **str** | The account group&#x27;s cloud provider identifier. | [optional] 
**provider_billing_identifier** | **str** | The account group&#x27;s cloud provider billing identifier.  If the billing account ID is the same as the credential account ID, this will have no value.  This will have a value when billing is tracked under a different account ID from the  account group&#x27;s standard cloud provider identifier.  Example: An AWS Gov account has a separate commercial account ID for billing. | [optional] 
**region_group** | **str** | The account&#x27;s region group (i.e. the unique data center group that is being used, e.g. commercial, gov, etc). | [optional] 
**purpose** | **str** | The purpose of the account credential (i.e. what it will be used for). | [optional] 
**credential_metadata** | [**list[CredentialMetadataModel]**](CredentialMetadataModel.md) | Credential identification information. | [optional] 
**created_date** | **datetime** | The date when the credentials were created. | [optional] 
**updated_date** | **datetime** | The date when the credentials were last modified (e.g. new credential info specified). | [optional] 
**last_verified_date** | **datetime** | The date when the credentials were last checked if still valid.  These verification checks occur automatically on a periodic basis. | [optional] 
**last_refreshed_date** | **datetime** | The date when the credentials were last refreshed (if applicable). | [optional] 
**verification_summary** | **str** | Summary of last verification actions. | [optional] 
**verification_results** | [**list[VerificationActionModel]**](VerificationActionModel.md) | List of all verification actions and their results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

