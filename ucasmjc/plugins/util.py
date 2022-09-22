import json
import re
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment
import requests
SOURCESOURCELOAD="C:/Users/Administrator/Desktop/ucasmjc/ucasmjc/ucasmjc/plugins/source/"
HAOGAN = "C:/Users/Administrator/Desktop/ucasmjc/ucasmjc/ucasmjc/plugins/haogan.json"
QA="C:/Users/Administrator/Desktop/ucasmjc/ucasmjc/ucasmjc/plugins/qa.json"
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
def init(usrqq,index,name):
    with open(HAOGAN,"r+") as f:
        load_dict = json.load(f)
        if usrqq in load_dict :
            load_dict[usrqq]["data"] -= load_dict[usrqq]["index"]
            load_dict[usrqq][name]["index"] +=index
            load_dict[usrqq][name]["id"]+=1
        else:
            load_dict[usrqq]={}
            load_dict[usrqq]["poke"]={}
            load_dict[usrqq]["setu1"]={}
            load_dict[usrqq]["setu2"]={}
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
    with open(HAOGAN,"w") as f:
        json.dump(load_dict,f)
        return load_dict[usrqq]["id"]
def hgupdate(usrqq):
    with open(HAOGAN,"r+") as f:
        load_dict = json.load(f)
        if usrqq in load_dict :
            if load_dict[usrqq]["mark"]==1:
                if load_dict[usrqq]["data"]>50:
                    load_dict[usrqq]["data"]=100
                else:
                    load_dict[usrqq]["data"]+=50 
                load_dict[usrqq]["mark"]=0
        else:
            load_dict[usrqq]={}
            load_dict[usrqq]["index"]=0
            load_dict[usrqq]["id"]=0
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
    with open(HAOGAN,"w") as f:
        json.dump(load_dict,f)
def hgget(usrqq):
    with open(HAOGAN,"r+") as f:
        load_dict = json.load(f)
        if usrqq not in load_dict :
            load_dict[usrqq]={}
            load_dict[usrqq]["index"]=0
            load_dict[usrqq]["id"]=0
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
        return load_dict[usrqq]["data"]
def hgdown(usrqq):
    with open(HAOGAN,"r+") as f:
            load_dict = json.load(f)
            if usrqq in load_dict :
                if(load_dict[usrqq]["data"]<0):
                    return [load_dict[usrqq]["data"],0]
                load_dict[usrqq]["data"]-=load_dict["a"][int(load_dict[usrqq]["index"])]
                load_dict[usrqq]["index"]+=1
                load_dict[usrqq]["id"]+=1
                id=load_dict[usrqq]["id"]
            else:
                load_dict[usrqq]={}
                load_dict[usrqq]["index"]=0
                load_dict[usrqq]["id"]=0
                load_dict[usrqq]["data"] = 60
                load_dict[usrqq]["mark"] = 1
    with open(HAOGAN,"w") as f:
        json.dump(load_dict,f)
    return [load_dict[usrqq]["data"], id]
def BV(bili):
    text = str(bili)
    if re.search(r"^BV([a-zA-Z0-9])+", text, re.I):
        text = r'https://www.bilibili.com/video/' + text
        resp = requests.get(text,headers=headers)
    t = resp.text
    title = re.findall(r'name="title" content="'+r'.+?'+r'_哔哩哔哩_bilibili">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall("视频作者\s[\u4E00-\u9FA5A-Za-z0-9_]+"+",\s作者简介",t)
    up = re.sub("视频作者\s",'',up[0])
    up = re.sub(",\s作者简介",'',up)
    pic = re.findall(r'itemprop="image" content="'+r'.+?'+r'><meta',t)
    pic = re.sub(r'itemprop="image" content="','',pic[0])
    pic = re.sub(r'"><meta','',pic)
    print(up)
    return [MessageSegment("text", {"text": '标题：' + title + '\n' + 'up主：' + up + '\n'+text+'\n'}),MessageSegment("image", {"file" : pic})]