from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import random
import json

from yaml import load
from ucasmjc.plugins.util import init
from ucasmjc.plugins.withdraw import add_withdraw_job
import asyncio
from nonebot.log import logger
setu = on_fullmatch("美少女", priority=5)
@setu.handle()
async def setu_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id=='712646893':
            return
        usrqq=event.get_user_id()
    except:
        usrqq=event.get_user_id()
    args = str(event.get_message()).strip()
    if ('r18' in args)|('R18' in args):
        await setu.finish('不可以色色！')
    tu=random.randint(1,386)
    await setu.send(MessageSegment("image",{"file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1萌图/%s.jpg'%tu}))