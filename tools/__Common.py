import json
from typing import List
 
data_path = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
map_prefix = "Map"
map_height = 17
map_width = 13
map_tiles_count = map_height * map_width

areas_count_x = 26
areas_count_y = ord('Z') - ord('A') + 1
areas_count = areas_count_x * areas_count_y

def padZero(value, size = 3):
    value_str = str(value)
    while len(value_str) < size:
        value_str = '0' + value_str
    return value_str

class RPGMakerMap:
    
    # Shadow Value bet. 1-15
    
    layer_1_first_offset = map_tiles_count * 0
    layer_1_last_offset = layer_1_first_offset + map_tiles_count - 1
    
    layer_2_first_offset = map_tiles_count * 1
    layer_2_last_offset = layer_2_first_offset + map_tiles_count - 1
    
    layer_3_first_offset = map_tiles_count * 2
    layer_3_last_offset = layer_3_first_offset + map_tiles_count - 1
    
    layer_4_first_offset = map_tiles_count * 3
    layer_4_last_offset = layer_4_first_offset + map_tiles_count - 1
    
    shadow_first_offset = map_tiles_count * 4
    shadow_last_offset = shadow_first_offset + map_tiles_count - 1
    
    layer_6_first_offset = map_tiles_count * 5
    layer_6_last_offset = layer_6_first_offset + map_tiles_count - 1
    
    def __init__(self, id) -> None:
        self._data: dict = None
        self.file_name = data_path + map_prefix + padZero(id) + ".json"
    
    def load(self):
        with open(self.file_name, 'r') as data: 
          json_string = data.read()
          self._data = json.loads(json_string)
          assert(self._data)
          
    def save(self):
        with open(self.file_name, 'w') as data: 
            json_string = json.dumps(self._data)
            data.write(json_string)
    
    def get_tiles_data(self) -> List[int]:
        data_tiles: List[int] = self._data["data"]
        return data_tiles
    
    def set_tiles_data(self, data: List[int]):
        if data:
            self._data["data"] = data

    def clear_shadows(self):
        tiles_data = self.get_tiles_data()
        for i in range(map_tiles_count):
            tiles_data[i+ self.shadow_first_offset] = 0
    
    def fill_shadows(self, value = 15):
        tiles_data = self.get_tiles_data()
        for i in range(map_tiles_count):
            tiles_data[i+ self.shadow_first_offset] = value
    
    def fill_test(self):
        tiles_data = self.get_tiles_data()
        for i in range(map_tiles_count):
            tiles_data[i+ self.layer_6_first_offset] = 2
            
    def clear_tiles(self):
        tiles_data = self.get_tiles_data()
        for i in range(len(tiles_data)):
            tiles_data[i] = 0
    
if __name__ == '__main__':
    mapData = RPGMakerMap(12)
    mapData.load()
    mapData.clear_shadows()
    mapData.fill_test()
    mapData.save()
    pass
            

