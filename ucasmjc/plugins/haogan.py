from typing import Union
from nonebot import  on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import json
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
import asyncio
from sqlalchemy import true
from yaml import load
from ucasmjc.plugins.util import SOURCELOAD,init
haogan = on_fullmatch("好感度", priority=5)
@haogan.handle()
async def get_data(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
        usrqq = event.get_user_id()
        try:
            _, group_id, user_id = event.get_session_id().split("_")
            if group_id!="712646893":
                mark=1
            else:
                mark=0
        except:
            mark=0
        if (event.get_event_name()!="message.private.friend")&(mark==0):
            [data,id]=hgdown(usrqq)
            if data < -100:
                return
        data = hgget(usrqq)
        if data < 0 :
            impression="讨厌，请离我远一些（嫌弃的眼神）"
        elif data < 45:
            impression="陌生，我和你很熟吗？不要和我说话了"
        elif data < 70:
            impression="谢谢你，你是一个好人（真诚的眼神）"
        elif data<90:
            impression="是臻果姬的朋友！今天也要开心哦"
        else:
            impression="主人来找臻果姬玩，臻果姬好开心"
        await haogan.send(MessageSegment("text", {
                    "text":"好感度"+str(data) +"\n"+impression
                }))
        await asyncio.sleep(1800)
        with open(HAOGAN,"r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open(HAOGAN,"w") as f:
                json.dump(load_dict,f)