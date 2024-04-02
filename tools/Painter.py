from typing import List
import copy 

# Generate the overworld tilemap

class Canvas:
    def __init__(self,x,y,w,h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.board : List[CanvasData] = [CanvasData() for _ in range(w*h)]
    
    def map_to_field():
        pass
    pass


class CanvasData:
    pass

class DrawGraphic:
    def __init__(self) -> None:
        pass
    
    def draw(self, x,y, id):
        pass
    

class DrawTilemap(DrawGraphic):
    def __init__(self) -> None:
        super.__init__()





class DrawSprite(DrawGraphic):
    def __init__(self) -> None:
        super.__init__()
        
        
