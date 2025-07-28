# FwLeaderboardsCharactersGetKills

Top 100 rankings of pilots by number of kills from yesterday, last week and in total

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_total** | [**List[FwLeaderboardsCharactersGetKillsActiveTotalInner]**](FwLeaderboardsCharactersGetKillsActiveTotalInner.md) | Top 100 ranking of pilots active in faction warfare by total kills. A pilot is considered \&quot;active\&quot; if they have participated in faction warfare in the past 14 days | 
**last_week** | [**List[FwLeaderboardsCharactersGetKillsLastWeekInner]**](FwLeaderboardsCharactersGetKillsLastWeekInner.md) | Top 100 ranking of pilots by kills in the past week | 
**yesterday** | [**List[FwLeaderboardsCharactersGetKillsYesterdayInner]**](FwLeaderboardsCharactersGetKillsYesterdayInner.md) | Top 100 ranking of pilots by kills in the past day | 

## Example

```python
from eve_esi_python.models.fw_leaderboards_characters_get_kills import FwLeaderboardsCharactersGetKills

# TODO update the JSON string below
json = "{}"
# create an instance of FwLeaderboardsCharactersGetKills from a JSON string
fw_leaderboards_characters_get_kills_instance = FwLeaderboardsCharactersGetKills.from_json(json)
# print the JSON string representation of the object
print(FwLeaderboardsCharactersGetKills.to_json())

# convert the object into a dict
fw_leaderboards_characters_get_kills_dict = fw_leaderboards_characters_get_kills_instance.to_dict()
# create an instance of FwLeaderboardsCharactersGetKills from a dict
fw_leaderboards_characters_get_kills_from_dict = FwLeaderboardsCharactersGetKills.from_dict(fw_leaderboards_characters_get_kills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


