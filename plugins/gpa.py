from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from plugins.util import SOURCELOAD,HAOGAN,hgupdate
gpa = on_fullmatch("gpa",priority=5)
@gpa.handle()
async def gpa_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await gpa.finish(MessageSegment("image",{
                "file": 'file:///'+SOURCELOAD+'gpa.jpg'
            })
)
GPA = on_fullmatch("GPA",priority=5)
@GPA.handle()
async def gpa_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await GPA.finish(MessageSegment("image",{
                "file": 'file:///'+SOURCELOAD+'gpa.jpg'
            })
)