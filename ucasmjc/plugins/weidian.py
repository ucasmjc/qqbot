from typing import Union
from nonebot import on_fullmatch
import json
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
weidian = on_fullmatch("微店", priority=5)
@weidian.handle()
async def weidian_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        
        load_dict = json.load(f)
        if usrqq in load_dict :
            if load_dict[usrqq]["mark"]==1:
                if load_dict[usrqq]["data"]>50:
                    load_dict[usrqq]["data"]=100
                else:
                    load_dict[usrqq]["data"]+=50 
                load_dict[usrqq]["mark"]=0
        else:
            load_dict[usrqq]={}
            load_dict[usrqq]["index"]=0
            load_dict[usrqq]["id"]=0
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
        json.dump(load_dict,f)
    daily_send = '微店链接为：https://weidian.com/?userid=1299786059&spider_token=c325&wfr=c&ifr=itemdetail\n感谢小伙伴关注我们的微店~'
    
    await weidian.send(MessageSegment("image",{
                "file":'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/weidian.jpg'}))
                   
    await weidian.send(daily_send)
    
      
      



 
 
