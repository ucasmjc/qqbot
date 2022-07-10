from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import random
import json

from yaml import load
from ucasmjc.plugins.util import init
from ucasmjc.plugins.withdraw import add_withdraw_job
import asyncio
from nonebot.log import logger
setu = on_fullmatch("美少女", priority=5)
@setu.handle()
async def setu_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!='647564271':
            return
        usrqq=event.get_user_id()
    except:
        usrqq=event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        load_dict = json.load(f)
        if usrqq in load_dict :
            load_dict[usrqq]["data"] -= load_dict[usrqq]["setu1"]["index"]
            if load_dict[usrqq]["setu1"]["index"]==0:
                load_dict[usrqq]["setu1"]["index"]=20
            else:
                load_dict[usrqq]["setu1"]["index"] *=2
            load_dict[usrqq]["setu1"]["id"]+=1
            id = load_dict[usrqq]["setu1"]["id"]
        else:
            load_dict[usrqq]={}
            load_dict[usrqq]["poke"]={"index":0,"id":0}
            load_dict[usrqq]["setu1"]={"index":0,"id":0}
            load_dict[usrqq]["setu2"]={"index":0,"id":0}
            load_dict[usrqq]["haogan"]={"index":0,"id":0}
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    if(load_dict[usrqq]["data"]<0):
        return
    args = str(event.get_message()).strip()
    if ('r18' in args)|('R18' in args):
        await setu.finish('不可以色色！')
    tu=random.randint(1,386)
    await setu.send(MessageSegment("image",{"file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1萌图/%s.jpg'%tu}))
    logger.info(f'添加定时任务，间隔：10秒')
    await asyncio.sleep(1800)
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        load_dict = json.load(f)
        if load_dict[usrqq]["setu1"]["id"] != id:
            return
        load_dict[usrqq]["setu1"]["index"] = 0
        load_dict[usrqq]["setu1"]["id"] = 0
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)