from __Classes import *
from __Factory import createTeleportChessEvent
from __Util import *

detect_names = ["Teleport_Event_LeftToRight", "Teleport_Event_RightToLeft","Teleport_Event_TopToBottom","Teleport_Event_BottomToTop"]

def remove_teleport_events(events: List[Event]):
  to_delete = []
  for event in events:
    if event and event.name in detect_names:
      to_delete.append(event)
  for event in to_delete:
    events.remove(event)
  if len(events) == 1:
    events.clear()

def set_events_data(map: RPGMakerMap, world: GameOverworld):
    i = 0
    
    map_left = world.get_map(map.x + 1, map.y)
    map_right = world.get_map(map.x - 1, map.y)
    map_top = world.get_map(map.x, map.y + 1)
    map_bottom = world.get_map(map.x, map.y - 1)
    
    for event_y in range(1, MAP_HEIGHT-1):
        events[i].set_pos(0, event_y)
        events[i].name += "_LeftToRight"
        set_event_params(map_right, MAP_WIDTH - 2, event_y, events[i].id)
        i += 1
        
    event_x = MAP_WIDTH
    for event_y in range(1,MAP_HEIGHT-1):
        events[i].set_pos(MAP_WIDTH - 1, event_y)
        events[i].name += "_RightToLeft"
        set_event_params(map_left, 1, event_y, events[i].id)
        i += 1
    
    for event_x in range(1, MAP_WIDTH - 1):
        events[i].set_pos(event_x,0)
        events[i].name += "_TopToBottom"
        set_event_params(map_bottom, event_x, MAP_HEIGHT-1, events[i].id)
        i += 1
    
    event_y = MAP_HEIGHT
    for event_x in range(1,MAP_WIDTH - 1):
        events[i].set_pos(event_x,MAP_HEIGHT-1)
        events[i].name += "_BottomToTop"
        set_event_params(map_top, event_x,0, events[i].id)
        i += 1
                
def set_event_params(map: RPGMakerMap, x, y, new_map_id):
  tele_event = createTeleportChessEvent((x,y), new_map_id)
  map.events.append(tele_event)

def get_code(event: Event):
   return event.pages[0].list[0].parameters[0]
 
maps: List[RPGMakerMap] = RPGMakerMap.load_maps(AREA_OFFSET, AREAS_COUNT_AND_LETTER + AREA_OFFSET)
world =  GameOverworld(maps)

for map in maps:
  # left- right- up- down
  # teleport_event = [copy.deepcopy(teleport_event) for _ in range(MAP_TILES_COUNT)]
  
  remove_teleport_events(map.events)
  # remove_empty_teleport_events(teleport_event)
  
  set_events_data(map)
  
  # events.insert(0,None)

    
  # map.save()
