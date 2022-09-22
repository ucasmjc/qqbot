from pyexpat.errors import XML_ERROR_FINISHED
from typing import Union
from nonebot import on_fullmatch
import json
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
xinpin = on_fullmatch("文创新品",priority=5)
@xinpin.handle()
async def xinpin_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    text_1 = '果壳文创上新啦\n果壳四季金属书签！\n'
    text_2='\n手绘明信片！只有果壳人才懂的梗！'
    await xinpin.send([MessageSegment("text",{
                "text":text_1
            }),MessageSegment("image",{
                "file": 'file:///'+SOURCELOAD+'shuqian.jpg'
            }),MessageSegment("text",{
                "text":text_2
            }),MessageSegment("image",{
                "file": 'file:///'+SOURCELOAD+'mingxinpian.jpg'
            })]
                
)
