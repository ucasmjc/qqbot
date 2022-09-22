from typing import Union
import requests,json
import re
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from nonebot.params import CommandArg
from nonebot.params import State, ArgPlainText, Arg, CommandArg
from nonebot.plugin import on_command, on_message
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, Message,PrivateMessageEvent
from nonebot.typing import T_State
weather = on_command("天气", priority=5)
@weather.handle()
async def handle_first_receive(event:Union[GroupMessageEvent,PrivateMessageEvent],state: T_State, args: Message = CommandArg()):
    args = args.extract_plain_text() # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args # 如果用户发送了参数则直接赋值
@weather.got('city', prompt="你想查询哪个校区的天气呢？（玉泉路/雁栖湖）")
async def handle_city(bot: Bot,
                   event:Union[GroupMessageEvent,PrivateMessageEvent],
                   city_name: Message = Arg("city")):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    city_name = str(city_name)
    if city_name not in ["玉泉路", "雁栖湖"]:
        await weather.finish("格式不对啦！请输入玉泉路/雁栖湖")
    if city_name =='玉泉路':
        url = f'https://www.tianqiapi.com/api?unescape=1&version=v1&appid=71217124&appsecret=ChYqiZn8&city=石景山'
    else:
        url = f'https://www.tianqiapi.com/api?unescape=1&version=v1&appid=71217124&appsecret=ChYqiZn8&city=怀柔'
    res = requests.get(url)
    array1 = res.json()['data']
    msg=city_name+'校区天气为：'
    for i in range(0,2):
        content_a = array1[i]['date']
        content_b = array1[i]['wea']
        content_c = array1[i]['tem2']
        content_d = array1[i]['tem1']
        content_e = array1[i]['air_level']
        content_f = array1[i]['air_tips']
        msg+='\n\n'+content_a+'\t\t\t'+content_b+'\n'+'气温为：'+content_c+'至'+content_d+'\n空气质量等级为'+content_e
        if i==0:
            msg+='\n'+content_f
    await weather.finish(msg)



