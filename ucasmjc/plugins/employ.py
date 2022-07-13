
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
BV1 = on_fullmatch("草地音乐节", priority=5)
@BV1.handle()
async def BV1_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1GK4y1V7yG")
    await BV1.send(messages)   
BV2 = on_fullmatch("军训vlog", priority=5)
@BV2.handle()
async def BV2_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1vU4y1H73G")
    await BV2.send(messages) 
BV3 = on_fullmatch("迎新晚会", priority=5)
@BV3.handle()
async def BV3_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV13L4y1672F")
    await BV3.send(messages) 
BV4 = on_fullmatch("音乐之夜", priority=5)
@BV4.handle()
async def BV4_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1GS4y1X7fx")
    await BV4.send(messages) 
BV5 = on_fullmatch("元旦晚会", priority=5)
@BV5.handle()
async def BV5_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1cS4y1Q7JQ")
    await BV5.send(messages) 
BV6 = on_fullmatch("社团文化节", priority=5)
@BV6.handle()
async def BV6_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV1BF411j7nh")
    await BV6.send(messages) 
BV7 = on_fullmatch("FREE舞蹈节", priority=5)
@BV7.handle()
async def BV7_(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    messages = await BV("BV16R4y1w7Cx")
    await BV7.send(messages) 


