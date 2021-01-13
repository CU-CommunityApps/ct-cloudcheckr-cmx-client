# UserResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#x27;s unique ID. This property supports: searching. | [optional] 
**customer_id** | **str** | The ID of the customer that manages the user. | [optional] 
**roles** | [**list[MappedRoleResponseModel]**](MappedRoleResponseModel.md) | The roles that are assigned to the user. | [optional] 
**email** | **str** | The user&#x27;s email address. This property supports: sorting, filtering and searching. | [optional] 
**saml_provider** | [**UserSamlProviderResponseModel**](UserSamlProviderResponseModel.md) |  | [optional] 
**allowed_auth_types** | **list[str]** | The user&#x27;s allowed authorization types. | [optional] 
**created_date** | **datetime** | The user&#x27;s creation date. This property supports: sorting and filtering. | [optional] 
**last_login_date** | **datetime** | The user&#x27;s last login date. This property supports: sorting and filtering. | [optional] 
**is_locked_out** | **bool** | The user&#x27;s lock out status. If true, the user is locked out and will not be permitted to login. This property supports: filtering. | [optional] 
**last_lockout_date** | **datetime** | If the user is locked, the date on which the user was locked out. | [optional] 
**is_activated** | **bool** | The user&#x27;s activation status. Some actions may be limited if the user is inactive. This property supports: filtering. | [optional] 
**organization_note** | **str** | The user&#x27;s organizational, shared note. | [optional] 
**personal_note** | **str** | The user&#x27;s personal note. | [optional] 
**has_user_level_access** | **bool** | Flag that indicate whether or not the user has user level access. This property supports: filtering. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

