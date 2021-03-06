# GeneralAccountRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account&#x27;s name. | [optional] 
**provider** | **str** | The cloud provider associated with the cloud account.  This property cannot be updated. | [optional] 
**parent_id** | **str** | The account&#x27;s parent. This property supports: resetting. | [optional] 
**payee_configuration** | [**PayeeConfigurationModel**](PayeeConfigurationModel.md) |  | [optional] 
**associated_account_attributes** | [**list[AccountAttributeModification]**](AccountAttributeModification.md) | Associated account attributes. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

