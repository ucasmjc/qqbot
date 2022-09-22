from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
fetch = on_fullmatch("取货",  priority=5)
@fetch.handle()
async def fetch_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    address1 = '时间：每周六下午至晚上\n地点：教学楼519\n会有同学在那里等着你哦~'
    await fetch.finish(address1)