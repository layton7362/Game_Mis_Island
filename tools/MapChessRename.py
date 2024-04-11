from __Classes import RPGMakerMap
from __Util import *

def fix_name_parent_folger():
    old_name  = ""
    for id in range(AREA_OFFSET, AREAS_COUNT + AREAS_COUNT_Y + AREA_OFFSET):
        
        map = RPGMakerMap(id)

        if map.name ==  "Z":
            break

        if map.name == old_name:
            letter = map.name[0]
            code = ord(letter) + 1
            next = chr(code)
            map.name = next
            map.save()
    
        old_name = map.name
 
fix_name_parent_folger()