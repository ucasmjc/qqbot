from tkinter import GROOVE
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
http1= on_fullmatch("sep",  priority=5)
@http1.handle()
async def http1_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
    address1 = 'http://sep.ucas.ac.cn/'
    await http1.finish(address1)
http2= on_fullmatch('本科教育网', priority=5)
@http2.handle()
async def http2_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    address2 = 'https://bkjy.ucas.ac.cn/'
    await http2.finish(address2)
http3=on_fullmatch("深澜软件", priority=5)
@http3.handle()
async def http3_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    address3 = 'http://124.16.81.61/'
    await http3.finish(address3)