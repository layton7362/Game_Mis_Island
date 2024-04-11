import json
import copy
from tools.__Util import MAP_TILES_COUNT, DATA_PATH 
from __Classes import Navigation, NavMapData
from __DataTemplate import EVENT_TELEPORT as teleport_event

def remove_teleport_events(__events: list):
  to_delete = []
  detect_names = ["Teleport_Event_LeftToRight", "Teleport_Event_RightToLeft","Teleport_Event_TopToBottom","Teleport_Event_BottomToTop"]
  for event in __events:
    if event and event["name"] in detect_names:
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
 
json_data = None
navigation = Navigation()

for navData in navigation:
  # left- right- up- down
  events = [copy.deepcopy(teleport_event) for _ in range(MAP_TILES_COUNT)]
  set_events_data(events, navData)
  events.insert(0,None)

  file = DATA_PATH + navData.file_name

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

