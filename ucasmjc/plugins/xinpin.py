from pyexpat.errors import XML_ERROR_FINISHED
from typing import Union
from nonebot import on_fullmatch
import json
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
xinpin = on_fullmatch("文创",priority=5)
@xinpin.handle()
async def xinpin_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
    text_1 = '果壳文创上新啦\n果壳四季金属书签！\n'
    text_2='\n手绘明信片！只有果壳人才懂的梗！'
    await xinpin.send([MessageSegment("text",{
                "text":text_1
            }),MessageSegment("image",{
                "file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/shuqian.jpg'
            }),MessageSegment("text",{
                "text":text_2
            }),MessageSegment("image",{
                "file": 'file:///C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/mingxinpian.jpg'
            })]
                
)
