from typing import Union
from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
help = on_fullmatch("help",rule = to_me(), priority=5)
@help.handle()
async def help_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    daily_send = '小伙伴你好~这里是臻果姬！现有的功能如下,直接发送相应指令即可~（部分功能只在特定群生效哦）\nV2.0:更新了好感度系统，发送“好感度帮助”获得更多信息~\nV2.1:更新了QA系统，发送“QA帮助”获得更多信息~\nV2.2：几乎所有功能均支持私聊实现\nV2.3：取消色图/涩图功能，加入“果壳文化”板块，发送“果壳文化”获得更多信息\n-“gpa”/“社团清单”/“地图”/“食堂”，获得相应校园信息\n-“猫猫”，获得随机猫猫图（比较慢，请稍等）\n-“果壳文化”，获得果壳文化视频清单，如“新生晚会”、“音乐之夜”……\n-“sep”/“本科教育网”/“深澜软件”，获得相应网址\n-“美少女”、“涩图”，获得随机美少女，高质量哦（无R18）\n-“x+x”，x为emoji表情，获得合成后的emoji表情\n-“文创新品”/“微店”/“取货”，获得良品文创相关信息~\n-“天气 玉泉路/雁栖湖”，获得今明两天天气\n-BV号，返回相应B站视频信息\n-“点歌 歌名”，返回网易云相应音乐\n-私聊发送“抽签”获得每日一签，在群聊中需发送”抽签 公屏“哦，发送“抽签帮助”可以查看更多功能哦\n-私聊发送“运势”查一查吉凶，在群聊中需发送”运势 公屏“，封建迷信哦\n-“每日一句”，获得双语名言\n-“占卜”，让占卜师可可给你随机占卜一下吧（延迟半分钟）\n-“二次元”，获得随机二次元图片，臻果姬也不知道会发出来什么哦\n-“help”，获得帮助菜单，需要先@臻果姬哦\n彩蛋：“疯狂星期四”，戳一戳，“语录”……\n大家还想加入什么功能可以告诉良品的可可~'
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
    await help.send(MessageSegment("image", {
                "file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/help.jpg'
            }))

