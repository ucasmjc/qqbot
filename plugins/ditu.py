import imp
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,SOURCELOAD
from plugins.util import SOURCELOAD,init
ditu = on_fullmatch("地图", priority=5)
@ditu.handle()
async def ditu_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await ditu.send(MessageSegment("image", {
                "file": 'file:///'+SOURCELOAD+'ditu.jpg'
            }))
