
EVENT_TELEPORT = {
      "id": 1,
      "name": "Teleport_Event",
      "note": "",
      "pages": [
        {
          "conditions": {
            "actorId": 1,
            "actorValid": False,
            "itemId": 1,
            "itemValid": False,
            "selfSwitchCh": "A",
            "selfSwitchValid": False,
            "switch1Id": 1,
            "switch1Valid": False,
            "switch2Id": 1,
            "switch2Valid": False,
            "variableId": 1,
            "variableValid": False,
            "variableValue": 0
          },
          "directionFix": False,
          "image": {
            "characterIndex": 0,
            "characterName": "",
            "direction": 2,
            "pattern": 0,
            "tileId": 0
          },
          "list": [
            {
              "code": 355,
              "indent": 0,
              "parameters": [
                "$gamePlayer.reserveTransforMoveMap(id, x, y);"
              ]
            },
            {
              "code": 0,
              "indent": 0,
              "parameters": []
            }
          ],
          "moveFrequency": 3,
          "moveRoute": {
            "list": [
              {
                "code": 0,
                "parameters": []
              }
            ],
            "repeat": True,
            "skippable": False,
            "wait": False
          },
          "moveSpeed": 3,
          "moveType": 0,
          "priorityType": 0,
          "stepAnime": False,
          "through": False,
          "trigger": 1,
          "walkAnime": True
        }
      ],
      "x": 0,
      "y": 1
    }

MAP_INFO = {
          "id": -1,
          "expanded": False,
          "name": "MAP006",
          "order": 6,
          "parentId": 5,
          "scrollX": 0,
          "scrollY": 0
     }