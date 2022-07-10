from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
place1 = on_fullmatch("教一阶", priority=5)
@place1.handle()
async def place1_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    await place1.send('教一阶在礼堂西侧的人文楼一楼~')
