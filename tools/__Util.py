# import json
# # from typing import List
 
DATA_PATH = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
MAP_PREFIX = "Map"
 
MAP_HEIGHT = 13
MAP_WIDTH = 17
MAP_TILES_COUNT = MAP_HEIGHT * MAP_WIDTH

AREA_OFFSET = 5
AREAS_COUNT_X  = AREAS_COUNT_Y = 26
AREAS_COUNT = AREAS_COUNT_X * AREAS_COUNT_Y

def padZero(value, size = 3):
    value_str = str(value)
    while len(value_str) < size:
        value_str = '0' + value_str
    return value_str

