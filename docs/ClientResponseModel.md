# ClientResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The client&#x27;s unique ID. This property supports: searching. | [optional] 
**name** | **str** | The client&#x27;s name. This property supports: sorting, filtering and searching. | [optional] 
**description** | **str** | The client&#x27;s description. This property supports: sorting, filtering and searching. | [optional] 
**type** | **str** | The client&#x27;s type. This property supports: sorting. | [optional] 
**roles** | [**list[MappedRoleResponseModel]**](MappedRoleResponseModel.md) | The roles that are assigned to the client. | [optional] 
**access_key_count** | **int** | The number of access keys belonging to the client. This property supports: sorting and filtering. | [optional] 
**created_date** | **datetime** | The date that the client was created. This property supports: sorting and filtering. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

