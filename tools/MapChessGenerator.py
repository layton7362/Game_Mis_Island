# Generate all Chess Maps. 
# WARNING: DELETE EVERYTHING OF THE MAPS, IF THEY ALREARY EXIST !!!!!!!!!!!!!!!!

import json
from tools.__Util import padZero, MAP_PREFIX
from tools.__Util import DATA_PATH as data_path
from __DataTemplate import MAP_INFO

def create_parent_map(letter):
    
    map_file_name = MAP_PREFIX + padZero(map_id)
    map_name = letter
    map_file_name_full = str(data_path + map_file_name +".json")
    with open(map_file_name_full, 'w+') as data:
        data.write(map_data) 
        
    map_info = MAP_INFO.copy()
    map_info["name"] = map_name
    map_info["id"] = map_id
    map_info["parentId"] = 2
    map_info["order"] = order
    
    map_info_data_dic.append(map_info)    

map_data = ""
with open(data_path + "Map003.json", 'r') as data:
        map_data = data.read()
map_data_dic = json.loads(map_data)

map_info_data = ""
with open(data_path + "MapInfosTemplate.json", 'r') as data:
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
        map_file_name_full = str(data_path +"\\"+ map_file_name +".json")
        map_data_dic["note"] = map_name
        map_data_dic["displayName"] = map_name
        map_data = json.dumps(map_data_dic)
        with open(map_file_name_full, 'w+') as data:
            data.write(map_data)
            
        map_info = MAP_INFO.copy()
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
with open(data_path + "MapInfos.json", 'w+') as data:
    data.write(map_info_data)
