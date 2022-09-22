import asyncio
import re
from typing import Union
import emoji
from nonebot.adapters.onebot.v11 import GroupMessageEvent,PrivateMessageEvent
import json
from ucasmjc.plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
from nonebot import logger, on_regex
from nonebot.params import RegexDict
from nonebot.adapters.onebot.v11 import MessageSegment

from .data_source import mix_emoji


__help__plugin_name__ = "emojimix"
__des__ = "emoji合成器"
__cmd__ = "{emoji1}+{emoji2}"
__short_cmd__ = __cmd__
__example__ = "😎+😁"
__usage__ = f"{__des__}\nUsage:\n{__cmd__}\nExample:\n{__example__}"


emojis = filter(lambda e: len(e) == 1, emoji.unicode_codes.UNICODE_EMOJI["en"])
pattern = "(" + "|".join(re.escape(e) for e in emojis) + ")"
emojimix = on_regex(
    rf"^\s*(?P<code1>{pattern})\s*\+\s*(?P<code2>{pattern})\s*$",
    block=True,
    priority=13,
)


@emojimix.handle()
async def _(event:Union[PrivateMessageEvent,GroupMessageEvent],msg: dict = RegexDict()):
    usrqq = event.get_user_id()
    try:
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id!="712646893":
            mark=1
        else:
            mark=0
    except:
        mark=0
    if (event.get_event_name()=="message.private.friend")|(mark==1):
        emoji_code1 = msg["code1"]
        emoji_code2 = msg["code2"]
        result = await mix_emoji(emoji_code1, emoji_code2)
        if isinstance(result, str):
            await emojimix.send(result)
        else:
            await emojimix.send(MessageSegment.image(result))
    else:        
        hgdown(usrqq)
        emoji_code1 = msg["code1"]
        emoji_code2 = msg["code2"]
        result = await mix_emoji(emoji_code1, emoji_code2)
        if isinstance(result, str):
            await emojimix.send(result)
        else:
            await emojimix.send(MessageSegment.image(result))
        logger.info(f'添加定时任务')
        await asyncio.sleep(1800)
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
                json.dump(load_dict,f)
