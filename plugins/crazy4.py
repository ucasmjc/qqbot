import asyncio
import re
import os
from typing import Union
from nonebot import on_fullmatch, on_regex
from pathlib import Path
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
from random import choice
try:
    import ujson as json
except ModuleNotFoundError:
    import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from requests_html import HTMLSession

CRAZY_PATH = os.path.join(os.path.dirname(__file__), 'source')

crazy = on_fullmatch("疯狂星期四")
@crazy.handle()
async def crazy4(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
        path = Path(CRAZY_PATH) / 'post.json'
        with open(path, 'r', encoding='utf-8') as f:
            kfc = json.load(f).get('post')
        text=choice(kfc)
        await crazy.send(MessageSegment("text", {"text": text}))
    else:
        [data,id]=hgdown(usrqq)
        if data < 0:
          return
        session = HTMLSession()
        '''data = session.get("https://kfc-crazy-thursday.vercel.app/api/index")'''
        path = Path(CRAZY_PATH) / 'post.json'
        with open(path, 'r', encoding='utf-8') as f:
            kfc = json.load(f).get('post')
        text=choice(kfc)
        await crazy.send(MessageSegment("text", {"text": text}))
        await asyncio.sleep(1800)
        with open(HAOGAN,"r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open(HAOGAN,"w") as f:
                json.dump(load_dict,f)