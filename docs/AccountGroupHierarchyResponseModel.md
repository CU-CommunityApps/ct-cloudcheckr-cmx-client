# AccountGroupHierarchyResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_account_id** | **str** | The legacy account&#x27;s ID. | [optional] 
**parent_id** | **str** | The account group&#x27;s parent. | [optional] 
**provider_identifier** | **str** | The account&#x27;s cloud provider identifier. | [optional] 
**provider_sub_type** | **str** | The account&#x27;s cloud provider sub-type. | [optional] 
**provider_payment_type** | **str** | The account&#x27;s payment model. | [optional] 
**payer_identifier** | **str** | The account&#x27;s payer identifier. | [optional] 
**include_all_accounts** | **bool** | Includes all accounts. | [optional] 
**associated_account_attributes** | [**list[AccountAttributeBasicInfo]**](AccountAttributeBasicInfo.md) | List of associated account attributes. | [optional] 
**has_children** | **bool** | Determines if the account group has children. | [optional] 
**costs** | [**list[AccountCost]**](AccountCost.md) | The total cost of all accounts in the account group and any of its descendents. | [optional] 
**type** | **str** | The account group&#x27;s type. Valid types are General, Group, and MAV. This property supports: filtering and sorting. | [optional] 
**provider** | **str** | The account&#x27;s cloud provider. This property supports: sorting, filtering and searching. | [optional] 
**created_date** | **datetime** | The account&#x27;s creation date. This property supports: sorting and filtering. | [optional] 
**has_pending_change** | **bool** | True if the account has a pending change. | [optional] 
**is_system_managed** | **bool** | Setting to indicate whether an account is managed automatically. | [optional] 
**credential_verification_status** | **str** | Indicates the account&#x27;s credential verification status. This property supports: sorting and filtering. | [optional] 
**id** | **str** | The account&#x27;s ID. This property supports: sorting and filtering. | [optional] 
**name** | **str** | The account&#x27;s name. This property supports: sorting, filtering and searching. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

