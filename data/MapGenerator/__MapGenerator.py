import json
import os 

def padZero(value):
    value_str = str(value)
    while len(value_str) < 3:
        value_str = '0' + value_str
    return value_str

def create_parent_map(letter):
    global map_id
    global save_path
    global order
    
    map_file_name = "Map" + padZero(map_id)
    map_name = letter
    map_file_name_full = str(save_path +"\\"+ map_file_name +".json")
    with open(map_file_name_full, 'w+') as data:
        data.write(map_data) 
        
    map_info = map_info_template.copy()
    map_info["name"] = map_name
    map_info["id"] = map_id
    map_info["parentId"] = 2
    map_info["order"] = order
    
    map_info_data_dic.append(map_info)
            
        
map_info_template = {
          "id": -1,
          "expanded": False,
          "name": "MAP006",
          "order": 6,
          "parentId": 5,
          "scrollX": 0,
          "scrollY": 0
     }

path = "F:\\MyGame\\RPGMAKER_MV_GAME\\data\\"
save_path = path 

map_data = ""
with open(path + "Map003.json", 'r') as data:
        map_data = data.read()
map_data_dic = json.loads(map_data)

map_info_data = ""
with open(path + "MapInfosTemplate.json", 'r') as data:
        map_info_data = data.read()
map_info_data_dic = json.loads(map_info_data)

map_id = 4
map_parent_id = map_id
order = 4
for l in range(ord('A'), ord('Z')+1):
    create_parent_map(chr(l))
    map_id += 1
    order += 1
    for i in range(26):
        map_file_name = "Map" + padZero(map_id)
        map_name = chr(l) + str(i)
        map_file_name_full = str(save_path +"\\"+ map_file_name +".json")
        map_data_dic["note"] = map_name
        map_data = json.dumps(map_data_dic)
        with open(map_file_name_full, 'w+') as data:
            data.write(map_data)
            
        map_info = map_info_template.copy()
        map_info["name"] = map_name
        map_info["order"] = order
        map_info["id"] = map_id
        map_info["parentId"] = map_parent_id
       
        map_info_data_dic.append(map_info)
        
        order += 1
        map_id += 1
        
    map_parent_id = map_id
        

#  Generate Parent Letter 

map_info_data = json.dumps(map_info_data_dic, indent=5)
with open(path + "MapInfos.json", 'w+') as data:
    data.write(map_info_data)
