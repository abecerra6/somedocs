# Booth Creation in webapp

## Getting information of a Booth created by designers
 
We can use https://CLIENT.6connexlocal.com/controlpanel/EVENT/virtual-builder/room/{{roomId}}
e.g https://test.6connexlocal.com/controlpanel/MR-helpyes-rooms2/virtual-builder/room/5
 
We need to focus on settings and the template fields. 
The template.nodes list has all the elements defined by the designers for the booth
For each node:
* (x,y) are the coordinates using the top-left corner of the booth background image as origin.
* (width, height) define the size of the element
* type is (banner,doorway link, logo etc.)
 
```json
{
    "addOns": {
        "surveyAssociationList": [],
        ...
    },
    "template": {
        "bgImage": "/5/40/1611675366364_27_Booth_1.jpg",
        "fgImage": null,
        "boothSize": 0,
        "walkingPeopleFlvPath": "",
        "templateId": 4,
        "bgImageWidth": 1680,
        "bgImageHeight": 1050,
        "flvWidth": 0,
        "flvHeight": 0,
        "fgImageWidth": 0,
        "fgImageHeight": 0,
        "thumbnail": "",
        "templateThumbnail": null,
        "name": null,
        "templateType": "public",
        "nodes": [
            {
                "surveyAssociationList": [],
                "selections": [],
                "originalGraphic": "/5/40/1611675873872_31_Lobby.jpg",
                "notEntitledMessageEnabled": false,
                "notEntitledMessage": null,
                "notEntitledVisible": false,
                "areaSetIds": [
                    40
                ],
                "zoneId": 0,
                "autoplay": false,
                "linkAutoplay": false,
                "modchatAutolaunch": false,
                "webinarAutolaunch": false,
                "chatQueueTitle": null,
                "chatQueueDescriptionOnline": null,
                "chatQueueDescriptionOffline": null,
                "badgeEmailNotifyEnabled": false,
                "badgeEmailsToNotify": null,
                "webappAutoLaunchTarget": false,
                "webappIframeWidth": 0,
                "webappIframeHeight": 0,
                "tokenDataPassEnabled": false,
                "contactFileUrl": null,
                "websiteLink": "",
                "doorwayLinkType": null,
                "doorwayLinkSubtype": null,
                "doorwayLinkTarget": 0,
                "webappActionType": "none",
                "webappActionTarget": null,
                "webappActionSecondaryTarget": null,
                "graphic": "/5/40/1611675873872_31_Lobb1611675885974_cut.jpg",
                "categoryList": [],
                "webappPassUserData": false,
                "hideContentMenuWhenAutoPlay": false,
                "autoOpen": false,
                "surveyDisplayMode": 0,
                "surveyId": 0,
                "promotions": [],
                "publicChatId": null,
                "description": null,
                "order": null,
                "badgeHeader": null,
                "badgeText": null,
                "bgImage": null,
                "width": 226,
                "height": 128,
                "url": null,
                "name": null,
                "id": 2785,
                "type": "banner",
                "label": null,
                "y": 221,
                "x": 348
            },
            {
                "surveyAssociationList": [],
                "selections": [],
                "originalGraphic": "/5/40/1611675901523_22_Lobby.jpg",
                "notEntitledMessageEnabled": false,
                "notEntitledMessage": null,
                "notEntitledVisible": false,
                "areaSetIds": [
                    40
                ],
                "zoneId": 0,
                "autoplay": false,
                "linkAutoplay": false,
                "modchatAutolaunch": false,
                "webinarAutolaunch": false,
                "chatQueueTitle": null,
                "chatQueueDescriptionOnline": null,
                "chatQueueDescriptionOffline": null,
                "badgeEmailNotifyEnabled": false,
                "badgeEmailsToNotify": null,
                "webappAutoLaunchTarget": false,
                "webappIframeWidth": 0,
                "webappIframeHeight": 0,
                "tokenDataPassEnabled": false,
                "contactFileUrl": null,
                "websiteLink": "",
                "doorwayLinkType": null,
                "doorwayLinkSubtype": null,
                "doorwayLinkTarget": 0,
                "webappActionType": "none",
                "webappActionTarget": null,
                "webappActionSecondaryTarget": null,
                "graphic": "/5/40/1611675901523_22_Lobb1611675908489_cut.jpg",
                "categoryList": [],
                "webappPassUserData": false,
                "hideContentMenuWhenAutoPlay": false,
                "autoOpen": false,
                "surveyDisplayMode": 0,
                "surveyId": 0,
                "promotions": [],
                "publicChatId": null,
                "description": null,
                "order": null,
                "badgeHeader": null,
                "badgeText": null,
                "bgImage": null,
                "width": 169,
                "height": 99,
                "url": null,
                "name": null,
                "id": 2786,
                "type": "banner",
                "label": null,
                "y": 238,
                "x": 753
            },
            {
                "surveyAssociationList": [],
                "selections": [],
                "originalGraphic": null,
                "notEntitledMessageEnabled": false,
                "notEntitledMessage": null,
                "notEntitledVisible": false,
                "areaSetIds": [],
                "zoneId": 0,
                "autoplay": false,
                "linkAutoplay": false,
                "modchatAutolaunch": false,
                "webinarAutolaunch": false,
                "chatQueueTitle": null,
                "chatQueueDescriptionOnline": null,
                "chatQueueDescriptionOffline": null,
                "badgeEmailNotifyEnabled": false,
                "badgeEmailsToNotify": null,
                "webappAutoLaunchTarget": false,
                "webappIframeWidth": 0,
                "webappIframeHeight": 0,
                "tokenDataPassEnabled": false,
                "contactFileUrl": null,
                "websiteLink": "",
                "doorwayLinkType": null,
                "doorwayLinkSubtype": null,
                "doorwayLinkTarget": 0,
                "webappActionType": "none",
                "webappActionTarget": null,
                "webappActionSecondaryTarget": null,
                "graphic": null,
                "categoryList": [],
                "webappPassUserData": false,
                "hideContentMenuWhenAutoPlay": false,
                "autoOpen": false,
                "surveyDisplayMode": 0,
                "surveyId": 0,
                "promotions": [],
                "publicChatId": null,
                "description": null,
                "order": null,
                "badgeHeader": null,
                "badgeText": null,
                "bgImage": null,
                "width": 170,
                "height": 93,
                "url": null,
                "name": null,
                "id": 2787,
                "type": "banner",
                "label": null,
                "y": 240,
                "x": 948
            }
        ]
    },
    "id": 18,
    "settings": {
        "timeBracketingList": [],
        "filter1": "",
        "filter2": "",
        "builderAccountId": 0,
        "languages": [
            14
        ],
        "boothSize": 0,
        "entitlements": [
            40
        ],
        "timeBracketingType": 0,
        "disableDoorwayInfo": false,
        "enableScroll": false,
        "timeZoneId": -1,
        "description": "Booth1",
        "name": "Booth1",
        "type": "booth",
        "locationKey": "Booth1",
        "active": true
    },
    "eventConfig": {
        "learningManagementSystemEnabled": false,
        "emailInboxEnabled": true,
        "entitlementDisabled": true,
        "leaderboardEnabled": false
    }
}
```


## Creation endpoint
VirtualBuilderController.newVirtualLocation  allows creating a virtual room or space.
with a POST to https://CLIENT.6connexlocal.com/controlpanel/EVENT/virtual-builder/
e.g https://test.6connexlocal.com/controlpanel/MR-helpyes-rooms2/virtual-builder/

The body has 2 field, settings and template, and the information to fill them can be retrieved as
in the previous section

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


