from tkinter import GROOVE
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
http1= on_fullmatch("sep",  priority=5)
@http1.handle()
async def http1_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        
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
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    address1 = 'http://sep.ucas.ac.cn/'
    await http1.finish(address1)
http2= on_fullmatch('本科教育网', priority=5)
@http2.handle()
async def http2_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        
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
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    address2 = 'https://bkjy.ucas.ac.cn/'
    await http2.finish(address2)
http3=on_fullmatch("深澜软件", priority=5)
@http3.handle()
async def http3_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        
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
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    address3 = 'http://124.16.81.61/'
    await http3.finish(address3)
qa1= on_fullmatch('提问的智慧', priority=5)
@qa1.handle()
async def http2_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        
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
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    address2 = '提问的智慧\nhttps://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md\n别像弱智一样提问\nhttps://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md'
    await qa1.finish(address2)