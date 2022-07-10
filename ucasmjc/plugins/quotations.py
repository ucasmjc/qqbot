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
    data = requests.get(url,timeout=5).json()
    result = f'{data["hitokoto"]}\t——{data["from"]}'
    await quotations.send(result)
