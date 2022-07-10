
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from ucasmjc.plugins.util import BV
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
design = on_fullmatch("果壳良品设计集", priority=5)
@design.handle()
async def design_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1ah411X7Pt")
    await bully.send(messages)
bully = on_fullmatch("美式霸凌", priority=5)
@bully.handle()
async def bully_(bot: Bot,event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV195411m7S1")
    await bully.send(messages)
interact = on_fullmatch("果壳迷踪", priority=5)
@interact.handle()
async def interact_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1uf4y1N7Kw")
    await interact.send(messages)

