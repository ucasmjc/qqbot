import json
import re
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment
import requests
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
async def init(usrqq,index,name):
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
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
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
        return load_dict[usrqq]["id"]
async def BV(bili):
    text = str(bili)
    if re.search(r"^BV([a-zA-Z0-9])+", text, re.I):
        text = r'https://www.bilibili.com/video/' + text
        resp = requests.get(text,headers=headers)
    t = resp.text
    title = re.findall(r'name="title" content="'+r'.+?'+r'_哔哩哔哩_bilibili">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall(r'","name":"'+r'.+?'+r'","approve":',t)
    up = re.sub(r'","name":"','',up[0])
    up = re.sub(r'","approve":','',up)
    pic = re.findall(r'itemprop="image" content="'+r'.+?'+r'><meta',t)
    pic = re.sub(r'itemprop="image" content="','',pic[0])
    pic = re.sub(r'"><meta','',pic)
    return [MessageSegment("text", {"text": '标题：' + title + '\n' + 'up主：' + up + '\n'+text+'\n'}),MessageSegment("image", {"file" : pic})]