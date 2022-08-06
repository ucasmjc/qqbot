from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
fetch = on_fullmatch("取货",  priority=5)
@fetch.handle()
async def fetch_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
    address1 = '时间：每周六下午至晚上\n地点：教学楼519\n会有同学在那里等着你哦~'
    await fetch.finish(address1)