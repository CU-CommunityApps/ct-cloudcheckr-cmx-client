# UserLevelAccessResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_account_access_rule** | **str** | The user&#x27;s access rule. This controls how customer and account access is determined. | [optional] 
**permission_sets** | [**list[PermissionSetBasicInfo]**](PermissionSetBasicInfo.md) | The user&#x27;s permission sets. | [optional] 
**customer_accounts** | [**list[CustomerAccountBasicInfo]**](CustomerAccountBasicInfo.md) | The customers and/or accounts to which the user has access. | [optional] 
**created_date** | **datetime** | The date this user-level access was first assigned. | [optional] 
**updated_date** | **datetime** | The date this user-level access was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

