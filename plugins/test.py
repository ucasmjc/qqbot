import asyncio
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget, requests
from typing import Union
from numpy import imag
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import random
setu1 = on_fullmatch("二次元", priority=5)
@setu1.handle()
async def setu_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!='647564271'&group_id!='712646893':
            return
        usrqq=event.get_user_id()
    except:
        usrqq=event.get_user_id()
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!="712646893":
            mark=1
        else:
            mark=0
    except:
        mark=0
    if (event.get_event_name()=="message.private.friend")|(mark==1):
        args = str(event.get_message()).strip()
        if ('r18' in args)|('R18' in args):
            await setu1.finish('不可以色色！')
        url = 'https://api.yimian.xyz/img'
        params = {
        'type': 'moe',
        'size': '1920x1080'
    }
        res = requests.get(url, params=params)
        await setu1.send(MessageSegment("image",{"file":res.url}))
    else:        
        [data,id]=hgdown(usrqq)
        if data < 0:
          return
        args = str(event.get_message()).strip()
        if ('r18' in args)|('R18' in args):
            await setu1.finish('不可以色色！')
        url = 'https://api.yimian.xyz/img'
        params = {
        'type': 'moe',
        'size': '1920x1080'
    }
        res = requests.get(url, params=params)
        await setu1.send(MessageSegment("image",{"file":res.url}))
        print(event.get_event_name())
        await asyncio.sleep(1800)
        with open(HAOGAN,"r+") as f:
                load_dict = json.load(f)
                load_dict[usrqq]["index"] = 0
                load_dict[usrqq]["id"] = 0
                with open(HAOGAN,"w") as f:
                    json.dump(load_dict,f)

