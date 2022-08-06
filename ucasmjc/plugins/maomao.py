import asyncio
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import requests
import json
maomao = on_fullmatch("猫猫",priority=5)
@maomao.handle()
async def maoamao_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!="712646893":
            mark=1
        else:
            mark=0
    except:
        mark=0
    if (event.get_event_name()=="message.private.friend")|(mark==1):
        urle = 'https://api.thecatapi.com/v1/images/search'
        res = requests.get(urle)
        content = res.json()[0]['url']
        await maomao.send(MessageSegment("image",{
                    "file": content
                })
    )
    else:        
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if usrqq in load_dict :
                if(load_dict[usrqq]["data"]<0):
                    return
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
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
        urle = 'https://api.thecatapi.com/v1/images/search'
        res = requests.get(urle)
        content = res.json()[0]['url']
        await maomao.send(MessageSegment("image",{
                    "file": content
                })
    )
        await asyncio.sleep(1800)
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
                json.dump(load_dict,f)

