from typing import List, Tuple
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
                _x = pos_x + w
                _y = pos_y + h
                if Draw.is_in_range(_x,_y):
                    gamemap = world.get_map_by_global(pos_x + w, pos_y + h)
                    if gamemap not in __maps:   
                        __maps.add(gamemap)
                    local_coord = world.get_local_by_global(pos_x + w, pos_y + h)
                    tile_id = gamemap.tileId_by_local(local_coord["x"], local_coord["y"])
                    gamemap.set_tile(layer_id, tile_id, value)
        for __map in __maps:
            __map.save()
            
    @staticmethod 
    def quad(pos_x, pos_y, size, world: GameOverworld, value: TileIDBase = TileIDBase.ID_NONE, layer_id: int = 2):
        Draw.rect(pos_x, pos_y, size, size, world, value, layer_id)
    
    @staticmethod 
    def circle(pos_x, pos_y, rad, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2):
        __maps: set['RPGMakerMap'] = set()
        rad_sq = rad * rad
        for x in range(pos_x - rad, pos_x + rad + 1):
            for y in range(pos_y - rad, pos_y + rad + 1):
                distance = ((x - pos_x) ** 2 + (y - pos_y) ** 2)
                if distance <= rad_sq:
                    if Draw.is_in_range(x,y):
                        gamemap = world.get_map_by_global(x, y)
                        if gamemap not in __maps:   
                            __maps.add(gamemap)
                        local_coord = world.get_local_by_global(x, y)
                        tile_id = gamemap.tileId_by_local(local_coord["x"], local_coord["y"])
                        gamemap.set_tile(layer_id, tile_id, value)
        for __map in __maps:
            __map.save()
            
    @staticmethod             
    def line(_from: Tuple[int,int], _to: Tuple[int,int], width, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2):
        __maps: set['RPGMakerMap'] = set()
        
        from_x = _from[0]
        from_y = _from[1]    
            
        dx = _to[0] - _from[0]
        dy = _to[1] - _from[1]

        if dx == 0 and dy == 0:
            return  # The starting and ending points are the same, so no need to draw a line

        distance = max(abs(dx), abs(dy))
        delta_x = dx / distance
        delta_y = dy / distance

        for i in range(int(distance)):
            x = int(from_x + 0.5)
            y = int(from_y + 0.5)

            for j in range(-width // 2, (width + 1) // 2):
                for k in range(-width // 2, (width + 1) // 2):
                    if 0 <= x + j < MAP_WIDTH * AREAS_COUNT_X and 0 <= y + k < MAP_HEIGHT * AREAS_COUNT_Y:
                        gamemap = world.get_map_by_global(x + j, y + k)
                        if gamemap not in __maps:   
                            __maps.add(gamemap)
                        local_coord = world.get_local_by_global(x + j, y + k)
                        tile_id = gamemap.tileId_by_local(local_coord["x"], local_coord["y"])
                        gamemap.set_tile(layer_id, tile_id, value)

            from_x += delta_x
            from_y += delta_y

        def is_in_range(x,y):
            return 0 <= x + j < MAP_WIDTH * AREAS_COUNT_X and 0 <= y + k < MAP_HEIGHT * AREAS_COUNT_Y
        
        for __map in __maps:
            __map.save()
    
    @staticmethod
    def draw_poly(points: List[Tuple[int,int]], width, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2):
        if len(points) <= 1:
            print("Not enough points to draw a polygon.")
            return
        prev_point = points[0]
        for point in points:
            Draw.line(prev_point, point, width, world, value, layer_id)
            prev_point = point
            
        Draw.line(points[-1], points[0], width, world, value, layer_id)

            
maps = RPGMakerMap.load_maps(AREA_OFFSET, AREAS_COUNT_AND_LETTER + AREA_OFFSET)
world = GameOverworld(maps)

# Draw.draw_poly( [(0,0) , (5,0) ,(0,5)], 2, world,TileId01.ID_SAND,2 )



    
