from __Util import *
from typing import List
import json
import re
from dataclasses import dataclass, asdict

class TileIDBase:
    ...

class RPGMakerMap:
    ...

class Event:
    class Page:
        class Conditions:
            def __init__(self, conditions) -> None:
                self.actorId = conditions["actorId"]
                self.actorValid = conditions["actorValid"]
                self.itemId = conditions["itemId"]
                self.itemValid = conditions["itemValid"]
                self.selfSwitchCh = conditions["selfSwitchCh"]
                self.selfSwitchValid = conditions["selfSwitchValid"]
                self.switch1Id = conditions["switch1Id"]
                self.switch1Valid = conditions["switch1Valid"]
                self.switch2Id = conditions["switch2Id"]
                self.switch2Valid = conditions["switch2Valid"]   
                self.variableId = conditions["variableId"]        
                self.variableValid = conditions["variableValid"]    
                self.variableValue = conditions["variableValue"]   
        class Image:
            def __init__(self, data) -> None:
                self.characterIndex = data["characterIndex"]
                self.characterName = data["characterName"]
                self.direction = data["direction"]
                self.pattern = data["pattern"]
                self.tileId = data["tileId"]
        class Command:
            def __init__(self, data) -> None:
                self.code = data["code"]
                self.indent = data["indent"]
                self.parameters = data["parameters"]
                
        def __init__(self, data) -> None:
            
            self.conditions = Event.Page.Conditions(data["conditions"])
            self.directionFix = data["directionFix"]
            self.image = Event.Page.Image(data["image"])
            
            self.list : List[Event.Page.Command] = []
            for l in data["list"]:
                self.list.append(Event.Page.Command(l))
                
            self.moveFrequency = data["moveFrequency"]
            self.moveRoute = data["moveRoute"]
            self.moveSpeed = data["moveSpeed"]
            self.moveType = data["moveType"]
            self.priorityType = data["priorityType"]
            self.stepAnime = data["stepAnime"]
            self.through = data["through"]
            self.trigger = data["trigger"]
            self.walkAnime = data["walkAnime"]            
                
    def __init__(self, data) -> None:
        
        self.id = data["id"]
        self.name = data["name"]
        self.note = data["note"]
        self.x = data["x"]
        self.y = data["y"]
        
        self.pages: List[Event.Page] = list()
        for page in data["pages"]:
            self.pages.append(Event.Page(page))
        
        self.check_type()
    
    def set_pos(self, x,y):
        self.x = x
        self.y = y
    
    def check_type(self):
        type = self.name
        if type == "":
            raise ValueError('Event has no type!')
        
        match(type):
            case "NPC":
                pass
            case "SEQUENCE":
                pass
            case _:
                if re.match("Teleport.*", type):
                    pass
                else:
                     raise TypeError('Event has wrong type!')
        
    @classmethod
    def fromDic(cls, data: dict):
        if not data:
            return None
        return cls(data)

class RPGMakerMap:
    
    @staticmethod
    def load_maps(min: int, max:int) -> List[RPGMakerMap]:
        maps : List[RPGMakerMap] = []
        for id in range(min,max):
            
            map = RPGMakerMap(id)
            # Parent folder map should only have one letter
            if len(map.name) == 1:
                continue
            if map._data:
                maps.append(map)
            else:
                print(f'ID {id} not loadable')
        return maps
    
    def __init__(self, id) -> None:
        self._data: dict = None
        self.id = id
        self.file_name = MAP_PREFIX + padZero(id)
        self.file_full_path = DATA_PATH + self.file_name + ".json"
        self.load() 
        
        self.tilesetId = self._data["tilesetId"] 
        self.name = self._data["displayName"]
        
        self.data_tiles: List[int] = self._data["data"]
        
        self.width = self._data["width"]
        self.height = self._data["height"]
        
        self.events = self.get_events()
        
        self.map_tiles_count = self.width * self.height
        
        self.layer_0_first_offset = self.map_tiles_count * 0
        self.layer_0_last_offset = self.layer_0_first_offset + self.map_tiles_count - 1

        self.layer_1_first_offset = self.map_tiles_count * 1
        self.layer_1_last_offset = self.layer_1_first_offset + self.map_tiles_count - 1

        self.layer_2_first_offset = self.map_tiles_count * 2
        self.layer_2_last_offset = self.layer_2_first_offset + self.map_tiles_count - 1

        self.layer_3_first_offset = self.map_tiles_count * 3
        self.layer_3_last_offset = self.layer_3_first_offset + self.map_tiles_count - 1

        self.layer_4_first_offset = self.map_tiles_count * 4
        self.layer_4_last_offset = self.layer_4_first_offset + self.map_tiles_count - 1

        self.layer_5_first_offset = self.map_tiles_count * 5
        self.layer_5_last_offset = self.layer_5_first_offset + self.map_tiles_count - 1
        
        self.layer0 = self.data_tiles[self.layer_0_first_offset : self.layer_0_last_offset +1]
        self.layer1 = self.data_tiles[self.layer_1_first_offset : self.layer_1_last_offset +1]
        self.layer2 = self.data_tiles[self.layer_2_first_offset : self.layer_2_last_offset +1]
        self.layer3 = self.data_tiles[self.layer_3_first_offset : self.layer_3_last_offset +1]
        self.layer4 = self.data_tiles[self.layer_4_first_offset : self.layer_4_last_offset +1]
        self.layer5 = self.data_tiles[self.layer_5_first_offset : self.layer_5_last_offset +1]
        pass
        
    def load(self):
        with open(self.file_full_path, 'r') as data: 
          json_string = data.read()
          self._data = json.loads(json_string)
          assert(self._data)
          
    def save(self):
        json_dict = {}
        json_dict["tilesetId"] = self.tilesetId
        json_dict["displayName"] = self.name
        json_dict["width"] = self.width
        json_dict["height"] = self.height
        json_dict["data"] = self.layer0 + self.layer1 + self.layer2 + self.layer3 + self.layer4 + self.layer5
        json_dict["events"] = self.events
        
        with open(self.file_full_path, 'w') as data: 
            json_string = toJson(json_dict)
            data.write(json_string)
    
    def clear_shadows(self):
        for i in range(self.map_tiles_count):
            self.layer4[i] = 0
    
    def fill_shadows(self, value: TileIDBase = 15):
        for i in range(self.map_tiles_count):
            # Shadow Value bet. 1-15
            self.layer4[i] = value
    
    def fill_layer(self, layer_id, value: TileIDBase):
        layer = getattr(self, f'layer{layer_id}')
        for i in range(self.map_tiles_count):
            layer[i] = value
            
    def clear_all_tiles(self):
        for i in range(len(self.tiles_data)):
            self.data_tiles[i] = 0
            
    def set_tile(self, layer_id, tile_id, val: TileIDBase):
        layer = getattr(self, f'layer{layer_id}')
        layer[tile_id] = val
    
    def get_events(self) -> List[Event]:
        events_dic = self._data["events"]
        events: List[Event] = []
        for event_dic in events_dic:
            event : Event = Event.fromDic(event_dic)
            events.append(event)
        return events 

    def tileId_by_local(self, x, y):
        return y * self.width + x
    
class GameOverworld:
    # add with +4, because the MapId begins with 4
    OFFSET = 4
    
    def __init__(self, maps: List[RPGMakerMap]):
        self.init_member()
        self. load_maps(maps)
        
    def init_member(self ):
        self.map_height = MAP_HEIGHT
        self.map_width = MAP_WIDTH
        self.area_count_x = AREAS_COUNT_X
        self.area_count_y = AREAS_COUNT_Y
        self.maps : dict = {}
        self.mapsByName : dict = {}
        
    def load_maps(self, maps: List[RPGMakerMap]):
        for y in range(AREAS_COUNT_Y + 26):
            for x in range(AREAS_COUNT_X):
                id = y * AREAS_COUNT_Y + x
                length = len(maps)
                if len(maps) > id:
                    self.maps[(x,y)] = maps[id]
                    self.mapsByName[maps[id].name] = maps[id]
    
    def get_map_by_global(self, x, y) -> RPGMakerMap:
        global_x = int( x / self.map_width)
        global_y = int( y / self.map_height)
        return self.maps[(global_x, global_y)]

    def get_local_by_global(self, x, y) -> dict:
        local_x =  x % self.map_width 
        local_y =  y % self.map_height 
        return {"x":local_x, "y":local_y}       
    
    def get_map(self, x, y) -> RPGMakerMap:
        return self.maps[(x, y)]
    
    def get_map_by_name(self, name) -> RPGMakerMap:
        return self.mapsByName[name]

if __name__ == "__main__":
    map = RPGMakerMap(5)
    events: List[Event] = map.events
    for event in events:
        if event:
            event.note = "Teleport"
    
    map.save()
    pass

