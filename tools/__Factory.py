from typing import List, Tuple, Set
from __DataTemplate import *

def createTeleportChessEvent(goal_pos: Tuple[int,int], goal_id):
    event: Event = Event(EVENT_TEMPLATE)
    event.name = "Teleport_Event"
    event.note = "Teleport"
    ev0 = Event.Page.Command({
        "code": 355,
        "indent": 0,
        "parameters": [
            f"$gamePlayer.reserveTransforMoveMap({goal_id}, {goal_pos[0]}, {goal_pos[1]});"    
        ]
    })
    evEnd = Event.Page.Command({
        "code": 0,
        "indent": 0,
        "parameters": []
    })
    event.pages[0].list.append(ev0)
    event.pages[0].list.append(evEnd)
    return event 

def createNPC(msgs: List[str]):
    event: Event = Event(EVENT_TEMPLATE)
    event.name = "NPC_NAME"
    event.note = "NPC"
    
    for msg in msgs:
        addMessageCommand(event.pages[0], msg)
        
    evEnd = Event.Page.Command({
        "code": 0,
        "indent": 0,
        "parameters": []
    })
    event.pages[0].list.append(ev0)
    event.pages[0].list.append(ev1)
    event.pages[0].list.append(evEnd)
    
    event.pages[0].image.tileId = 0
    event.pages[0].image.characterName = "People3"
    event.pages[0].image.direction = 2
    event.pages[0].image.pattern = 2
    event.pages[0].image.characterIndex = 4
    
    event.pages[0].priorityType = 1 
    event.pages[0].trigger = 0 
    
    return event 


def addMessageCommand(page: Event.Page, msg):
    ev0 = Event.Page.Command({
        "code": 101,
        "indent": 0,
        "parameters": [
            "",0,0,2    
        ]
    })
    ev1 = Event.Page.Command({
        "code": 401,
        "indent": 0,
        "parameters": [msg]
    })
    page.list.append(ev0)
    page.list.append(ev1)