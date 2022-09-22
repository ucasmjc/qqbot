import asyncio
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import requests
import json
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
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
        if (event.get_event_name()!="message.private.friend")&(mark==0):
            [data,id]=hgdown(usrqq)    
        if data < 0:
          return
        urle = 'https://api.thecatapi.com/v1/images/search'
        res = requests.get(urle)
        content = res.json()[0]['url']
        await maomao.send(MessageSegment("image",{
                    "file": content
                })
    )
        await asyncio.sleep(1800)
        with open(HAOGAN,"r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open(HAOGAN,"w") as f:
                json.dump(load_dict,f)

