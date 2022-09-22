from typing import Union
from nonebot import on_fullmatch
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
weidian = on_fullmatch("微店", priority=5)
@weidian.handle()
async def weidian_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    daily_send = '微店链接为：https://weidian.com/?userid=1299786059&spider_token=c325&wfr=c&ifr=itemdetail\n感谢小伙伴关注我们的微店~'
    
    await weidian.send(MessageSegment("image",{
                "file":'file:///'+SOURCELOAD+'weidian.jpg'}))
                   
    await weidian.send(daily_send)
    
      
      



 
 
