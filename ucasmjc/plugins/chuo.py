from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent
import random
from nonebot.adapters.onebot.v11 import Bot,MessageSegment
import os

from yaml import load

from ucasmjc.plugins.util import init
from ucasmjc.plugins.withdraw import add_withdraw_job
import json
__zx_plugin_name__ = "戳一戳"

__plugin_usage__ = """
usage：
    戳一戳随机掉落语音或美图萝莉图
""".strip()
__plugin_des__ = "戳一戳发送语音美图萝莉图不美哉？"
__plugin_type__ = ("其他",)
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["戳一戳"],
}

poke__reply = [
    "lsp你再戳？",
    "连个可爱美少女都要戳的肥宅真恶心啊。",
    "你再戳！",
    "？再戳试试？",
    "别戳了别戳了再戳就坏了555",
    "我爪巴爪巴，球球别再戳了",
    "你戳你🐎呢？！",
    "那...那里...那里不能戳...绝对...",
    "(。´・ω・)ん?",
    "有事恁叫我，别天天一个劲戳戳戳！",
    "欸很烦欸！你戳🔨呢",
    "?",
    "再戳一下试试？",
    "???",
    "正在关闭对您的所有服务...关闭成功",
    "啊呜，太舒服刚刚竟然睡着了。什么事？",
    "正在定位您的真实地址...定位成功。轰炸机已起飞",
]
poke_ = on_notice(priority=5, block=False)
@poke_.handle()
async def poke_event(bot: Bot,event: PokeNotifyEvent):
    if event.self_id == event.target_id:
        usrqq = event.get_user_id()
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
        if usrqq in load_dict :
            load_dict[usrqq]["data"] -= load_dict[usrqq]["poke"]["index"]
            if load_dict[usrqq]["poke"]["index"]==0:
                load_dict[usrqq]["poke"]["index"]=20
            else:
                load_dict[usrqq]["poke"]["index"]*=2 
            load_dict[usrqq]["poke"]["id"]+=1
        else:
            load_dict[usrqq]={}
            load_dict[usrqq]["poke"]={"index":0,"id":0}
            load_dict[usrqq]["setu1"]={"index":0,"id":0}
            load_dict[usrqq]["setu2"]={"index":0,"id":0}
            load_dict[usrqq]["haogan"]={"index":0,"id":0}
            load_dict[usrqq]["data"] = 60
            load_dict[usrqq]["mark"] = 1
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
        if(load_dict[usrqq]["data"]<0):
            return
        if random.random() < 0.3:
            rst = ""
            if random.random() < 0.15:
                rst = "气死我了！"
            await poke_.finish(rst + random.choice(poke__reply), at_sender=True)
        rand = random.random()
        if rand < 0.2:
            voice = random.choice(os.listdir("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1"))
            result = MessageSegment("record",{
                "file":"file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1/"+voice})
            text =os.listdir("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/dinggong")
            text.sort()
            index = voice.split('.')[0]
            await poke_.send(result)
            await poke_.send(text[int(index)-1].split("_")[1])
        elif rand > 0.7:
            img = "file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/pa/" + str(random.randint(0,46)) + ".jpg"
            await poke_.send(MessageSegment("image",{"file" : img}))
        else :
            await poke_.send(MessageSegment("poke", {"qq": event.user_id}))
        await add_withdraw_job(bot,usrqq,load_dict[usrqq]["poke"]["id"],"poke")


