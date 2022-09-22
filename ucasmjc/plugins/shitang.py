from typing import Union
from nonebot import on_fullmatch
import json
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
shitang = on_fullmatch("食堂", priority=5)
@shitang.handle()
async def shitang_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!='647564271'&group_id!='712646893'&group_id!='712646893':
            return
        usrqq=event.get_user_id()
    except:
        usrqq=event.get_user_id()
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await shitang.send(MessageSegment("image",{
                "file": 'file:///'+SOURCELOAD+'shitang.jpg'
            })
)