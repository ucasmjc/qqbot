
import json
import re
def ab():
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
    for id in load_dict.keys():
            load_dict[id]["mark"]=1
            if load_dict[id]["data"]<0:
                load_dict[id]["data"]=0
            load_dict[id]["poke"]={"index":0,"id":0}
            load_dict[id]["setu1"]={"index":0,"id":0}
            load_dict[id]["setu2"]={"index":0,"id":0}
            load_dict[id]["haogan"]={"index":0,"id":0}
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
