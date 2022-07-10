from typing import Union
from nonebot import on_fullmatch
import json
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
shitang = on_fullmatch("食堂", priority=5)
@shitang.handle()
async def shitang_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!='647564271'&group_id!='712646893'&group_id!='712646893':
            return
        usrqq=event.get_user_id()
    except:
        usrqq=event.get_user_id()
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        load_dict = json.load(f)
        if usrqq not in load_dict :
            load_dict[usrqq]={}
            load_dict[usrqq]["poke"]={"index":0,"id":0}
            load_dict[usrqq]["setu1"]={"index":0,"id":0}
            load_dict[usrqq]["setu2"]={"index":0,"id":0}
            load_dict[usrqq]["haogan"]={"index":0,"id":0}
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
            data = 60
            mark=1
        else:
            if load_dict[usrqq]["mark"]==1:
                if load_dict[usrqq]["data"]>50:
                    load_dict[usrqq]["data"]=100
                else:
                    load_dict[usrqq]["data"]+=50 
                load_dict[usrqq]["mark"]=0
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
    await shitang.send(MessageSegment("image",{
                "file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/shitang.jpg'
            })
)