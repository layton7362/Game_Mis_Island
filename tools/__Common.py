# import json
# # from typing import List
 
DATA_PATH = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
MAP_PREFIX = "Map"
 
MAP_HEIGHT = 17
MAP_WIDTH = 13
MAP_TILES_COUNT = MAP_HEIGHT * MAP_WIDTH

areas_count_x = 26
areas_count_y = ord('Z') - ord('A') + 1
areas_count = areas_count_x * areas_count_y

def padZero(value, size = 3):
    value_str = str(value)
    while len(value_str) < size:
        value_str = '0' + value_str
    return value_str


