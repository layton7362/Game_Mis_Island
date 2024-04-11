from typing import List, Tuple, Set
from __DataTemplate import *

def createTeleportChessEvent(pos: Tuple[int,int], id):
    event: Event = Event(EVENT_TEMPLATE)
    ev0 = Event.Page.Command({
        "code": 355,
        "indent": 0,
        "parameters": [
            f"$gamePlayer.reserveTransforMoveMap({id}, {pos[0]}, {pos[1]});"    
        ]
    })
    ev1 = Event.Page.Command({
        "code": 0,
        "indent": 0,
        "parameters": []
    })
    event.pages[0].list.append(ev0)
    event.pages[0].list.append(ev1)
    return event 