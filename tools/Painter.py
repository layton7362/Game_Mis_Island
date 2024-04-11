from typing import List
import copy 
from __Classes import *
from __Util import MAP_WIDTH

class TileIDBase:
    ID_NONE = 0

class TileId01(TileIDBase):
    ID_WATER = 2048
    ID_GRAS = 2816
    ID_SAND = 3584
    ID_PATH = 3296
    
    ID_SIGN = 1
    ID_BRIDGE_H = 2
    ID_BRIDGE_V = 3
    
    ID_TREE = 11
    ID_TREE_SNOW = 12
    
    ID_ENTRY_STONE_1 = 16
    ID_ENTRY_STONE_2 = 17
    ID_ENTRY_STONE_3 = 18
    ID_ENTRY_WOOD = 19
    ID_ENTRY_BRICK = 20

class TileId02(TileIDBase):
    ID_WATER = 2048
    ID_GRAS = 2816

class Draw:
    
    @staticmethod
    def rect(pos_x, pos_y, width, height, world: GameOverworld, value: TileIDBase = TileIDBase.ID_NONE, layer_id: int = 2):
        __maps: set[RPGMakerMap]  = set()
        for w in range(width):
            for h in range(height):
                _x = pos_x + width
                _y = pos_y + height
                if _x >= 0 and _x < MAP_WIDTH * AREAS_COUNT_X and _y >= 0 and _y < MAP_HEIGHT * AREAS_COUNT_Y:
                    gamemap = world.get_map_by_global(pos_x + w, pos_y + h)
                    if gamemap not in __maps:   
                        __maps.add(gamemap)
                    local_coord = world.get_local_by_global(pos_x + w, pos_y + h)
                    tile_id = gamemap.tileId_by_local(local_coord["x"], local_coord["y"])
                    gamemap.set_tile(layer_id, tile_id, value)
        for __map in __maps:
            __map.save()
        

maps = RPGMakerMap.load_maps(AREA_OFFSET, AREAS_COUNT + AREA_OFFSET)

for map in maps:
    print(map.name + " from " + map.file_name)
# world = GameOverworld(maps)

# for x in range(0,3):
#     for y in range(3,5):
#         map: RPGMakerMap = world.get_map(x,y)
#         map.fill_layer(0, TileId01.ID_GRAS)
#         map.save()

# Draw.rect(4,4,50,1, world,TileId01.ID_GRAS)

# for x in range(0, 10):
#     map = nav.get_map_by_global(x,0)
#     local_coord = nav.get_local_by_global(x,0)
#     tileid = map.tileId_by_local(local_coord["x"], local_coord["y"])
#     # map.set_tile(1, tileid, TileId01.ID_WATER)
#     map.fill_layer(2,TileId01.ID_NONE)
#     map.save()
    
