# Booth Creation in webapp

VirtualBuilderController.newVirtualLocation  allows creating a virtual room or space.
with a POST to https://CLIENT.6connexlocal.com/controlpanel/EVENT/virtual-builder/
e.g https://test.6connexlocal.com/controlpanel/MR-helpyes-rooms2/virtual-builder/

The body has 2 fields:

```json
settings : {
  "type": "booth",
  "name": "Booth2",
  "description": "Booth2",
  "locationKey": "Booth2",
  "enableScroll": false,
  "disableDoorwayInfo": false,
  "languages": [
    14
  ],
  "entitlements": [
    40
  ],
  "builderAccountId": 0,
  "timeBracketingList": [],
  "timeBracketingType": 0,
  "timeZoneId": -1,
  "filter1": "",
  "filter2": "",
  "active": true
}
```

If the Booth has been created by designers in the UI, we can ask to 

