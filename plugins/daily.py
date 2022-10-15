import asyncio
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
import  requests
daily = on_fullmatch("每日一句",  priority=5)
@daily.handle()
async def daily_sentence(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
        daily_send = await get_daily()
        await daily.send(daily_send[0])
        await daily.send(daily_send[1])
    else:   
        [data,id]=[data,id]=hgdown(usrqq)
    if data<0:
        return
        if data < 0:
          return
        daily_send = await get_daily()
        await daily.send(daily_send[0])
        await daily.send(daily_send[1])
        await asyncio.sleep(1800)
        with open(HAOGAN,"r+") as f:
            load_dict = json.load(f)
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open(HAOGAN,"w") as f:
                json.dump(load_dict,f)

async def get_daily():
    daily_sentence = get_content()
    return daily_sentence

def get_content():
    url = 'http://open.iciba.com/dsapi/'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]
