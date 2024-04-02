import json
import os 

class NavMapData:
    def __init__(self, _map_id, name):
        self.map_id = _map_id
        self.name = name

class Navigation:
    def __init__(self):
        self.init_member()

    def init_member(self):
        self.map_height = 17
        self.map_width = 13
        self.area_count_x = 26
        self.area_count_y = ord('Z') - ord('A') + 1

        map_id = 0  # add with +4, because the MapId Begins with 4
        self._map = []
        letter = ord('A') - 1
        for y in range(self.area_count_y):
            map_id += 1
            letter += 1
            self._map.append([])
            for x in range(self.area_count_x):
                name = chr(letter) + str(x)
                self._map[y].append(NavMapData(map_id + 4, name))
                map_id += 1

    def get(self, x, y):
        if x < 0 or x > self.area_count_x or y < 0 or y > self.area_count_y:
          return None
        return self._map[x][y]

nav = Navigation()
res = nav.get(2,2)

teleport_event = {
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
                "$gamePlayer.reserveTransferMoveMap(id, x, y);"
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

def remove_teleport_events(__events):
  for event in __events:
    if event and "Teleport_Event" in event["name"]:
      __events.remove(event)
      pass
    else:
      pass
  pass

def set_events_positions(events):
    global height
    global width
    
    i = 0
    for y in range(1,height-1):
        set_event_position(0,y, events[i])
        events[i]["name"] += "_LeftToRight"
        # set_event_params()
        i += 1
        
    for y in range(1,height-1):
        set_event_position(width-1,y, events[i])
        events[i]["name"] += "_RightToLeft"
        i += 1
    
    for x in range(1,width-1):
        set_event_position(x,0, events[i])
        events[i]["name"] += "_TopToBottom"
        i += 1
        
    for x in range(1,width-1):
        set_event_position(x,height-1, events[i])
        events[i]["name"] += "_BottomToTop"
        i += 1
                
def set_event_position(x,y, event):
    event["x"] = x
    event["y"] = y

def set_event_params(map_id, x, y, event):
    code = f'$gamePlayer.reserveTransferMoveMap({map_id},{x},{y});'
    event["pages"][0]["list"][0]["parameters"] = code

def top(_map_id):
  _map_id += 1
  if _map_id < width:
    return _map_id
  return None

def bottom(_map_id):
  _map_id -= 1
  if _map_id >= 0:
    return _map_id
  return None

def right(_map_id):
  pass

def left(_map_id):
  _map_id -= 1
  if _map_id >= 0:
    return _map_id
  return None

def ignore(_map_id):
  pass

width = 17
height = 13

# A = 4, B = 31
start_map_id = 5
end_map_id = 30
diff = end_map_id - start_map_id

events_count = width * 2 + height * 2
events_count -= 4
# left- right- up- down

events = [teleport_event.copy() for i in range(events_count)]
set_events_positions(events)
events.insert(0,None)

path = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
json_data = None

file = path + "Map004.json"

with open(file, 'r') as data: 
    json_string = data.read()
    json_data = json.loads(json_string)
    
    remove_teleport_events(json_data["events"])
    
    for event in events:
      json_data["events"].append(event)
  
with open(file, 'w') as data:
    json_string = json.dumps(json_data, indent=5)
    data.write(json_string)

