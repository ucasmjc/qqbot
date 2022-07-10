from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
FAQ = on_fullmatch("FAQ",priority=5)
@FAQ.handle()
async def FAQ_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    await FAQ.finish("【腾讯文档】2022级果壳本科新生报到民间FAQ\nhttps://docs.qq.com/doc/DU0hKTk5VZHhOZnRU")