# CharactersCharacterIdAssetsGetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_blueprint_copy** | **bool** |  | [optional] 
**is_singleton** | **bool** |  | 
**item_id** | **int** |  | 
**location_flag** | **str** |  | 
**location_id** | **int** |  | 
**location_type** | **str** |  | 
**quantity** | **int** |  | 
**type_id** | **int** |  | 

## Example

```python
from esi_api_client.models.characters_character_id_assets_get_inner import CharactersCharacterIdAssetsGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of CharactersCharacterIdAssetsGetInner from a JSON string
characters_character_id_assets_get_inner_instance = CharactersCharacterIdAssetsGetInner.from_json(json)
# print the JSON string representation of the object
print(CharactersCharacterIdAssetsGetInner.to_json())

# convert the object into a dict
characters_character_id_assets_get_inner_dict = characters_character_id_assets_get_inner_instance.to_dict()
# create an instance of CharactersCharacterIdAssetsGetInner from a dict
characters_character_id_assets_get_inner_from_dict = CharactersCharacterIdAssetsGetInner.from_dict(characters_character_id_assets_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


