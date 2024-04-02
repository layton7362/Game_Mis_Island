import json
import copy
import os 

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

def padZero(value):
  value_str = str(value)
  while len(value_str) < 3:
      value_str = '0' + value_str
  return value_str

class NavMapData:
    def __init__(self, _map_id, name, _x, _y):
        self.map_id = _map_id
        self.map_id_pad = padZero(_map_id)
        self.file_name = f'Map{self.map_id_pad}.json'
        self.name = name
        self.x = _x
        self.y = _y
        
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
                self._map[y].append(NavMapData(map_id + 4, name, x,y))
                map_id += 1

    def get(self, x, y)-> NavMapData:
        if x < 0 or x >= self.area_count_x or y < 0 or y >= self.area_count_y:
          return None
        return self._map[y][x]
      
    def __iter__(self):
        return NavigationIterator(self)

class NavigationIterator:
    def __init__(self, navigation):
        self.navigation = navigation
        self.x = 0
        self.y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.y >= self.navigation.area_count_y:
            raise StopIteration

        result = self.navigation.get(self.x, self.y)
        self.x += 1
        if self.x >= self.navigation.area_count_x:
            self.x = 0
            self.y += 1

        return result

def remove_teleport_events(__events: list):
  to_delete = []
  for event in __events:
    if event and "Teleport_Event" in event["name"]:
      to_delete.append(event)
  for event in to_delete:
    __events.remove(event)
  if len(__events) == 1:
    __events.clear()
  pass

def remove_empty_teleport_events(events: list):
  remove_events = []
  for event in events:
    if event and get_code(event) == "":
      remove_events.append(event)
      pass
  for event in remove_events:
    events.remove(event)
  if len(events) == 1:
    events.clear()

def set_events_data(events, nav : NavMapData):
    global height
    global width
    
    i = 0
    nav_data_left = navigation.get(nav.x+1,nav.y)  
    nav_data_right = navigation.get(nav.x-1,nav.y)  
    nav_data_top = navigation.get(nav.x,nav.y+1)  
    nav_data_bottom = navigation.get(nav.x,nav.y-1)  
    
    for event_y in range(1,height-1):
        set_event_position(0,event_y, events[i])
        events[i]["name"] += "_LeftToRight"
        set_event_params(nav_data_right,width-1,event_y, events[i])
        i += 1
        
    event_x = width
    for event_y in range(1,height-1):
        set_event_position(width-1,event_y, events[i])
        events[i]["name"] += "_RightToLeft"
        set_event_params(nav_data_left,0,event_y, events[i])
        i += 1
    
    for event_x in range(1,width-1):
        set_event_position(event_x,0, events[i])
        events[i]["name"] += "_TopToBottom"
        set_event_params(nav_data_bottom,event_x,height-1, events[i])
        i += 1
    
    event_y = height
    for event_x in range(1,width-1):
        set_event_position(event_x,height-1, events[i])
        events[i]["name"] += "_BottomToTop"
        set_event_params(nav_data_top,event_x,0, events[i])
        i += 1
                
def set_event_position(x,y, event):
    event["x"] = x
    event["y"] = y

def set_event_params(data: NavMapData, x, y, event):
  if data:
    code = f'$gamePlayer.reserveTransforMoveMap({data.map_id},{x},{y});'
    event["pages"][0]["list"][0]["parameters"][0] = code
  else:
    event["pages"][0]["list"][0]["parameters"][0] = ""
  pass

def get_code(event):
   return event["pages"][0]["list"][0]["parameters"][0]
 
width = 17
height = 13
path = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
json_data = None
navigation = Navigation()
events_count = (width * 2 + height * 2) - 8

for navData in navigation:
  # left- right- up- down
  events = [copy.deepcopy(teleport_event) for _ in range(events_count)]
  set_events_data(events, navData)
  events.insert(0,None)

  file = path + navData.file_name

  json_string = ""
  with open(file, 'r') as data: 
      json_string = data.read()
      
  json_data = json.loads(json_string)
  remove_teleport_events(json_data["events"])
  remove_empty_teleport_events(events)
  for event in events:
    json_data["events"].append(event)
    
  json_string = json.dumps(json_data, indent=5)
  with open(file, 'w') as data:
      data.write(json_string)

