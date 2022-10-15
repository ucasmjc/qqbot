from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from plugins.util import SOURCELOAD,init
community_use = on_fullmatch("社团清单", priority=5)
@community_use.handle()
async def community_use_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await community_use.send(MessageSegment("image", {
                "file": 'file:///'+SOURCELOAD+'community.jpg'
            }))
