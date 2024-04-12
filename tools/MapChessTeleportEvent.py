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

def  set_map_teleports(map: RPGMakerMap, world: GameOverworld):
    
    n = world.get_neighbours(map)
    
    map_left = n["left"]
    map_right = n["right"]
    map_top = n["top"]
    map_bottom = n["bottom"]
    
    event_id = 1
    if map_right:
      next_map_id = map_right.id
      for event_y in range(1, MAP_HEIGHT-1):
          tele_event = createTeleportChessEvent((1 , event_y), next_map_id)
          tele_event.set_pos(MAP_WIDTH - 1, event_y)
          tele_event.name += "_LeftToRight"
          tele_event.id = event_id 
          map.events.append(tele_event)
          
    if map_left: 
      event_x = MAP_WIDTH
      next_map_id = map_left.id
      for event_y in range(1,MAP_HEIGHT-1):
          tele_event = createTeleportChessEvent((MAP_WIDTH - 2, event_y), next_map_id)
          tele_event.set_pos(0, event_y)
          tele_event.name += "_RightToLeft"
          tele_event.id = event_id 
          map.events.append(tele_event)
    
    if map_bottom: 
      next_map_id = map_bottom.id
      for event_x in range(1, MAP_WIDTH - 1):
          tele_event = createTeleportChessEvent((event_x, 1), next_map_id)
          tele_event.set_pos(event_x, MAP_HEIGHT - 1)
          tele_event.name += "_TopToBottom"
          tele_event.id = event_id
          map.events.append(tele_event)
          
    if map_top: 
      next_map_id = map_top.id
      for event_x in range(1, MAP_WIDTH - 1):
          tele_event = createTeleportChessEvent((event_x, MAP_HEIGHT - 2), next_map_id)
          tele_event.set_pos(event_x, 0)
          tele_event.name += "_BottomToTop"
          tele_event.id = event_id
          map.events.append(tele_event)
           
def get_code(event: Event):
   return event.pages[0].list[0].parameters[0]
 
maps: List[RPGMakerMap] = RPGMakerMap.load_maps(AREA_OFFSET, AREAS_COUNT_AND_LETTER + AREA_OFFSET)
world =  GameOverworld(maps)

for map in maps:
  # left- right- up- down
  
  remove_teleport_events(map.events)
  set_map_teleports(map, world)
  
  # map.events.insert(0,None)

  map.save()
