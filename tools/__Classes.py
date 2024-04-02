from __Common import *

class RPGMakerMap:
    def __init__(self, id) -> None:
        self._data: dict = None
        self.file_name = DATA_PATH + MAP_PREFIX + padZero(id) + ".json"
        
        self.load()
        
        self.tilesetId = self._data["tilesetId"] 
        self.name = self._data["displayName"]
        
        self.data_tiles: List[int] = self._data["data"]
        
        self.width = self._data["width"]
        self.height = self._data["height"]
        
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
        with open(self.file_name, 'r') as data: 
          json_string = data.read()
          self._data = json.loads(json_string)
          assert(self._data)
          
    def save(self):
        self._data["tilesetId"] = self.tilesetId
        self._data["displayName"] = self.name
        self._data["width"] = self.width
        self._data["height"] = self.height
        
        self._data["data"] = self.layer0 + self.layer1 + self.layer2 + self.layer3 + self.layer4 + self.layer5
        
        with open(self.file_name, 'w') as data: 
            json_string = json.dumps(self._data)
            data.write(json_string)
    
    def clear_shadows(self):
        for i in range(self.map_tiles_count):
            self.layer4[i] = 0
    
    def fill_shadows(self, value = 15):
        for i in range(self.map_tiles_count):
            # Shadow Value bet. 1-15
            self.layer4[i] = value
    
    def fill_test(self):
        for i in range(self.map_tiles_count):
            self.layer2[i] = 0
            
    def clear_tiles(self):
        for i in range(len(self.tiles_data)):
            self.data_tiles[i] = 0
    
    def get_events(self) -> dict:
        return self._data["data"] 
    
    
class NavMapData:
    def __init__(self, _map_id, name, _x, _y):
        self.map_id = _map_id
        self.map_id_pad = padZero(_map_id)
        self.file_name = f'Map{self.map_id_pad}.json'
        self.name = name
        self.x = _x
        self.y = _y
        
class Navigation:
    OFFSET = 4
    
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
                self._map[y].append(NavMapData(map_id + Navigation.OFFSET, name, x,y))
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
    
    
class Event:
    pass