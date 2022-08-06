import re
from typing import Union
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
import requests
import json

from yaml import load
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
#analysis_bili = on_regex(r"(b23.tv)|(bili(22|23|33|2233).cn)|(live.bilibili.com)|(bilibili.com/(video|read|bangumi))|(^(av|cv)(\d+))|(^BV([a-zA-Z0-9])+)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|(QQ小程序&#93;哔哩哔哩)", flags=re.I)
analysis_bili = on_regex(r"(b23.tv)|(bilibili.com/video)|(^BV([a-zA-Z0-9])+)", flags=re.I)
@analysis_bili.handle()
async def analysis_main(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
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
    text = str(event.get_message()).strip()
    if re.search(r"^BV([a-zA-Z0-9])+", text, re.I):
        text = r'https://www.bilibili.com/video/' + text
    resp = requests.get(text,headers=headers)
    t = resp.text
    title = re.findall(r'name="title" content="'+r'.+?'+r'_哔哩哔哩_bilibili">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall("视频作者\s[\u4E00-\u9FA5A-Za-z0-9_]+"+",\s作者简介",t)
    up = re.sub("视频作者\s",'',up[0])
    up = re.sub(",\s作者简介",'',up)
    pic = re.findall(r'itemprop="image" content="'+r'.+?'+r'><meta',t)
    pic = re.sub(r'itemprop="image" content="','',pic[0])
    pic = re.sub(r'"><meta','',pic)
    await analysis_bili.finish([MessageSegment("text", {"text": '标题：' + title + '\n' + 'up主：' + up + '\n'+text+'\n'}),MessageSegment("image", {"file" : pic})])