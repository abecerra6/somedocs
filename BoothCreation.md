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

And

```json
template : {
  "templateType": "public",
  "templateId": 4,
  "bgImage": "/5/40/1611675366364_27_Booth_1.jpg",
  "bgImageHeight": 1050,
  "bgImageWidth": 1680,
  "fgImage": null,
  "fgImageHeight": 0,
  "fgImageWidth": 0,
  "flvHeight": 0,
  "flvWidth": 0,
  "walkingPeopleFlvPath": "",
  "thumbnail": "",
  "nodes": [
    {
      "selections": [],
      "bgImage": "",
      "y": 222,
      "x": 351,
      "label": null,
      "name": null,
      "id": -1,
      "type": "banner",
      "url": "",
      "width": 226,
      "height": 128
    },
    {
      "selections": [],
      "bgImage": "",
      "y": 238,
      "x": 753,
      "label": null,
      "name": null,
      "id": -1,
      "type": "banner",
      "url": "",
      "width": 169,
      "height": 99
    },
    {
      "selections": [],
      "bgImage": "",
      "y": 240,
      "x": 948,
      "label": null,
      "name": null,
      "id": -1,
      "type": "banner",
      "url": "",
      "width": 170,
      "height": 93
    }
  ]
}
```

The template.nodes list has all the areas the Booth must have. (x,y) are the coordinates using the top-left corner of the background image as origin.



