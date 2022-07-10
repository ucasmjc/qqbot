import re
import os
from typing import Union
from nonebot import on_regex
from pathlib import Path
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
from random import choice
try:
    import ujson as json
except ModuleNotFoundError:
    import json

CRAZY_PATH = os.path.join(os.path.dirname(__file__), 'source')

crazy = on_regex(r"(疯狂星期四)|(疯四)", flags=re.I)
@crazy.handle()
async def crazy4(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq=event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        load_dict = json.load(f)
        if usrqq not in load_dict :
            load_dict[usrqq]={}
            load_dict[usrqq]["poke"]={"index":0,"id":0}
            load_dict[usrqq]["setu1"]={"index":0,"id":0}
            load_dict[usrqq]["setu2"]={"index":0,"id":0}
            load_dict[usrqq]["haogan"]={"index":0,"id":0}
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
            data = 60
            mark=1
        else:
            if load_dict[usrqq]["mark"]==1:
                if load_dict[usrqq]["data"]>50:
                    load_dict[usrqq]["data"]=100
                else:
                    load_dict[usrqq]["data"]+=50 
                load_dict[usrqq]["mark"]=0
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
    path = Path(CRAZY_PATH) / 'post.json'
    with open(path, 'r', encoding='utf-8') as f:
        kfc = json.load(f).get('post')
    text=choice(kfc)
    await crazy.finish(MessageSegment("text", {"text": text}))