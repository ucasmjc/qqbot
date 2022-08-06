import asyncio
from typing import Union
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent,PrivateMessageEvent
from nonebot.typing import T_State
import requests,json


__zx_plugin_name__ = "一言二次元语录"
__plugin_usage__ = """
usage：
    一言二次元语录
    指令：
        语录/二次元
""".strip()
__plugin_des__ = "二次元语录给你力量"
__plugin_cmd__ = ["语录/二次元"]
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["语录", "二次元"],
}


quotations = on_fullmatch("语录",priority=5, block=True)

url = "https://international.v1.hitokoto.cn/?c=a"


@quotations.handle()
async def _(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent], state: T_State):
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!="712646893":
            mark=1
        else:
            mark=0
    except:
        mark=0
    if (event.get_event_name()=="message.private.friend")|(mark==1):
        data = requests.get(url,timeout=5).json()
        result = f'{data["hitokoto"]}\t——{data["from"]}'
        await quotations.send(result)
    else:    
        usrqq = event.get_user_id()
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if usrqq in load_dict :
                if(load_dict[usrqq]["data"]<0):
                    return
                load_dict[usrqq]["data"]-=load_dict["a"][int(load_dict[usrqq]["index"])]
                load_dict[usrqq]["index"]+=1
                load_dict[usrqq]["id"]+=1
                id=load_dict[usrqq]["id"]
            else:
                load_dict[usrqq]={}
                load_dict[usrqq]["index"]=0
                load_dict[usrqq]["id"]=0
                load_dict[usrqq]["data"] = 60
                load_dict[usrqq]["mark"] = 1
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
        data = requests.get(url,timeout=10).json()
        result = f'{data["hitokoto"]}\t——{data["from"]}'
        await quotations.send(result)
        await asyncio.sleep(1800)
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
                json.dump(load_dict,f)
