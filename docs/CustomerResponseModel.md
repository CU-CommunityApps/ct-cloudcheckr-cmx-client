# CustomerResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The customer&#x27;s ID. This property supports: filtering and searching. | [optional] 
**name** | **str** | The customer&#x27;s name. This property supports: sorting, filtering and searching. | [optional] 
**parent_id** | **str** | The customer&#x27;s parent ID if there is an L1/L2 relationship. This property supports: filtering. | [optional] 
**state** | **str** | The customer&#x27;s current state. | [optional] 
**signup_type** | **str** | The customer&#x27;s signup type. This property supports: sorting. | [optional] 
**disabled_date** | **datetime** | The customer&#x27;s disabled date. This property supports: filtering. | [optional] 
**saas_customer_id** | **str** | The customer&#x27;s external Saas ID. This property supports: sorting. | [optional] 
**plan** | [**CustomerPlanResponseModel**](CustomerPlanResponseModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

