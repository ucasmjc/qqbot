from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import  requests
import requests.adapters  
import random
import json

from sqlalchemy import false, true
fuqian = on_fullmatch("运势 公屏",  priority=5)
@fuqian.handle()
async def fuqian_use(bot: Bot, event: GroupMessageEvent):
    requests.adapters.DEFAULT_RETRIES = 10
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
    url = 'https://api.fanlisky.cn/api/qr-fortune/get/'+str(usrqq)
    res = requests.get(url)
    content_a = res.json()['data']['fortuneSummary']
    content_b= res.json()['data']['luckyStar']
    content_c = res.json()['data']['signText']
    文创=['果壳贴纸','果壳中性笔','果壳马克杯','果壳扑克牌','柯斯特利金小帆布袋','果壳金属书签','果壳风景明信片','柯斯特利金高端收纳袋','果壳金属校徽','“爱在果壳”帆布袋','校训帆布袋','果壳手绘明信片','柯斯特利金变色马克杯']
    msg='\n'+'您的运势为：'+str(content_a)+'\n'+str(content_b)+'\n'+'签文：'+str(content_c)+'\n\n'+str(random.choice(文创))+'和现在的你更配哦~'
    await fuqian.send([MessageSegment("at",  {
                "qq": usrqq,
                "name": ""
            }),MessageSegment("text", {
                "text":msg
            })]
    )
fuqian1 = on_fullmatch("运势",  priority=5)
@fuqian1.handle()
async def fuqian_use(bot: Bot, event: PrivateMessageEvent):
    requests.adapters.DEFAULT_RETRIES = 10
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
    url = 'https://api.fanlisky.cn/api/qr-fortune/get/'+str(usrqq)
    res = requests.get(url)
    content_a = res.json()['data']['fortuneSummary']
    content_b= res.json()['data']['luckyStar']
    content_c = res.json()['data']['signText']
    文创=['果壳贴纸','果壳中性笔','果壳马克杯','果壳扑克牌','柯斯特利金小帆布袋','果壳金属书签','果壳风景明信片','柯斯特利金高端收纳袋','果壳金属校徽','“爱在果壳”帆布袋','校训帆布袋','果壳手绘明信片','柯斯特利金变色马克杯']
    msg='\n'+'您的运势为：'+str(content_a)+'\n'+str(content_b)+'\n'+'签文：'+str(content_c)+'\n\n'+str(random.choice(文创))+'和现在的你更配哦~'
    await fuqian1.send([MessageSegment("text", {
                "text":msg
            })]
    )

