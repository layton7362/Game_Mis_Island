from typing import List, Tuple, Set
import copy 
from __Classes import *
from __Util import MAP_WIDTH
import json 
from __Factory import * 
 
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
    def circle(pos: Tuple[int,int], rad, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2):
        pos_x = pos[0]
        pos_y = pos[1]
        used_maps: set[RPGMakerMap] = set[RPGMakerMap]()
        rad_sq = rad * rad
        for x in range(pos_x - rad, pos_x + rad + 1):
            for y in range(pos_y - rad, pos_y + rad + 1):
                if not Draw.is_in_range(x,y):
                    continue
                distance = ((x - pos_x) ** 2 + (y - pos_y) ** 2)
                if distance <= rad_sq:
                    game_map = world.get_map_by_global(x, y)
                    if game_map not in used_maps:   
                        used_maps.add(game_map)
                    local_coord = world.get_local_by_global(x, y)
                    tile_id = game_map.tileId_by_local(local_coord["x"], local_coord["y"])
                    game_map.set_tile(layer_id, tile_id, value)
        for used_map in used_maps:
            used_map.save()
            
    @staticmethod             
    def line(_from: Tuple[int,int], _to: Tuple[int,int], width, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2):
        __maps: set['RPGMakerMap'] = set()
        
        from_x = _from[0]
        from_y = _from[1]    
            
        dx = _to[0] - _from[0]
        dy = _to[1] - _from[1]

        if dx == 0 and dy == 0:
            return 
        
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
        
        for __map in __maps:
            __map.save()
            
    @staticmethod
    def is_in_range(x,y):
        return 0 <= x < MAP_WIDTH * AREAS_COUNT_X and 0 <= y < MAP_HEIGHT * AREAS_COUNT_Y
    
    @staticmethod
    def lines(points: List[Tuple[int,int]], width, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2, fill = False):
        if len(points) <= 1:
            print("Not enough points to draw a polygon.")
            return
        prev_point = points[0]
        for point in points:
            if prev_point == point:
                continue
            Draw.line(prev_point, point, width, world, value, layer_id)
            prev_point = point
        
    @staticmethod
    def poly(points: List[Tuple[int,int]], width, world: 'GameOverworld', value: 'TileIDBase' = TileIDBase.ID_NONE, layer_id: int = 2, fill = False):
        if len(points) <= 1:
            print("Not enough points to draw a polygon.")
            return
        prev_point = points[0]
        Draw.lines(points, width, world, value, layer_id)
        # End point connnect to the first one
        Draw.line(points[-1], points[0], width, world, value, layer_id)
    
    @staticmethod
    def point_in_polygon(point: Tuple[float, float], polygon: List[Tuple[float, float]]) -> bool:
        inside = False
        p1x, p1y = polygon[0]
        for i in range(len(polygon) + 1):
            p2x, p2y = polygon[i % len(polygon)]
            if point[1] > min(p1y, p2y) and point[1] <= max(p1y, p2y) and point[0] <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or point[0] <= xinters:
                        inside = not inside
            p1x, p1y = p2x, p2y
        return inside

class Stamp():
    
    pass

if __name__ == "__main__":
    
    maps = RPGMakerMap.load_maps(AREA_OFFSET, AREAS_COUNT_AND_LETTER + AREA_OFFSET)
    world =  GameOverworld(maps)
    # center = (22,22)
    # Draw.circle(center,5,world,TileId01.ID_GRAS)
    # Draw.circle(center,4,world,TileId01.ID_SAND)
    # Draw.circle(center,3,world,TileId01.ID_GRAS)
    # Draw.circle(center,2,world,TileId01.ID_SAND)
    
    # Draw.rect(0,
    #           AREAS_COUNT_Y * MAP_HEIGHT - 2, 
    #           AREAS_COUNT_X * MAP_WIDTH,  
    #           AREAS_COUNT_Y * MAP_HEIGHT, 
    #           world,
    #           TileId01.ID_WATER,
    #           0
    #           )
    
    # for x in range(4, 26):
    #     map = world.get_map(x, 0)
    #     map.fill_layer(0, TileId01.ID_GRAS)
    #     map.save()
        
    event = createNPC((10,8),"Ich    bin ein Test")
    map = world.get_map(0,0)
    map.events.append(event)
    map.save()
    