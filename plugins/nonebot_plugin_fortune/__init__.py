import asyncio
from nonebot import require
from nonebot import logger
from nonebot import on_command, on_regex,on_fullmatch
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, GROUP, GROUP_ADMIN, GROUP_OWNER, GroupMessageEvent, MessageSegment,PrivateMessageEvent
from .data_source import fortune_manager
from .utils import MainThemeList
import re
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
__fortune_vsrsion__ = "v0.4.3"
plugin_notes = f'''
今日运势 
当在群里抽签时，需在命令后加“公屏”两字，如“指定向晚签 公屏”
[抽签] 抽签
[指定xx签] 指定特殊角色签底，需要自己尝试哦~（目前可指定的签包括原神、明日方舟和asoul的部分角色，数量有限，请大家不要在官方群中试验）
[设置xx签] 设置群抽签主题
[重置抽签] 重置群抽签主题
[主题列表] 查看可选的抽签主题
[抽签设置] 查看群抽签主题'''.strip()

plugin_help = on_command("抽签帮助", permission=GROUP, priority=8, block=True)
divine = on_fullmatch("抽签 公屏", permission=GROUP, priority=8, block=True)
divine1 = on_fullmatch("抽签", priority=8, block=True)
limit_setting = on_regex(r"指定(.*?)签", priority=8, block=True)
limit_setting1 = on_regex(r"指定(.*?)签 公屏", permission=GROUP, priority=8, block=True)
theme_setting = on_regex(r"设置(.*?)签", permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=8, block=True)
reset = on_command("重置抽签", permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER, priority=8, block=True)
theme_list = on_command("主题列表", permission=GROUP, priority=8, block=True)
show = on_command("抽签设置", permission=GROUP, priority=8, block=True)

'''
    超管功能
'''
refresh = on_command("刷新抽签", permission=SUPERUSER, priority=8, block=True)

scheduler = require("nonebot_plugin_apscheduler").scheduler

@plugin_help.handle()
async def show_help(bot: Bot, event: GroupMessageEvent):
    await plugin_help.finish(plugin_notes)

@show.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    theme = fortune_manager.get_setting(event)
    show_theme = MainThemeList[theme][0]
    await show.finish(f"当前群抽签主题：{show_theme}")

@theme_list.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    msg = fortune_manager.get_main_theme_list()
    await theme_list.finish(msg)

@divine.handle()
async def _(bot: Bot, event: GroupMessageEvent):
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
        image_file, status = fortune_manager.divine(spec_path=None, event=event)
        if not status:
            msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(image_file)
        else:
            logger.info(f"User {event.user_id} | Group {event.group_id} 占卜了今日运势")
            msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(image_file)
        
        await divine.send(message=msg, at_sender=True)        
    else:
        hgdown(usrqq)
        image_file, status = fortune_manager.divine(spec_path=None, event=event)
        if not status:
            msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(image_file)
        else:
            logger.info(f"User {event.user_id} | Group {event.group_id} 占卜了今日运势")
            msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(image_file)
        
        await divine.send(message=msg, at_sender=True)        
        await asyncio.sleep(1800)
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
            load_dict = json.load(f)
            if load_dict[usrqq]["id"] != id:
                return
            load_dict[usrqq]["index"] = 0
            load_dict[usrqq]["id"] = 0
            with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
                json.dump(load_dict,f)
@divine1.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    image_file, status = fortune_manager.divine(spec_path=None, event=event)
    if not status:
        msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(image_file)
    else:
        logger.info(f"User {event.user_id}占卜了今日运势")
        msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(image_file)
    
    await divine1.finish(message=msg)        

@theme_setting.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    is_theme = re.search(r"设置(.*?)签", event.get_plaintext())
    setting_theme = is_theme.group(0)[2:-1] if is_theme is not None else None

    if setting_theme is None:
        await theme_setting.finish("指定抽签主题参数错误~")
    else:
        for theme in MainThemeList.keys():
            if setting_theme in MainThemeList[theme]:
                if not fortune_manager.divination_setting(theme, event):
                    await theme_setting.finish("该抽签主题未启用~")
                else:
                    await theme_setting.finish("已设置当前群抽签主题~")
    
        await theme_setting.finish("还没有这种抽签主题哦~")

@reset.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    fortune_manager.divination_setting("random", event)
    await reset.finish("已重置当前群抽签主题为随机~")

@limit_setting.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    is_specific_type = re.search(r'指定(.*?)签', event.get_plaintext())
    limit = is_specific_type.group(0)[2:-1] if is_specific_type is not None else None

    if limit is None:
        await limit_setting.finish("指定签底参数错误~")

    if limit == "随机":
        image_file, status = fortune_manager.divine(spec_path=None, event=event)
    else:
        spec_path = fortune_manager.limit_setting_check(limit)
        if not spec_path:
            await limit_setting.finish("还不可以指定这种签哦，请确认该签底对应主题开启或图片路径存在~")
        else:
            image_file, status = fortune_manager.divine(spec_path=spec_path, event=event)
        
    if not status:
        msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(image_file)
    else:
        logger.info(f"User {event.user_id} | Group {event.group_id} 占卜了今日运势")
        msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(image_file)
    
    await limit_setting.finish(message=msg, at_sender=True)
@limit_setting1.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    is_specific_type = re.search(r'指定(.*?)签', event.get_plaintext())
    limit = is_specific_type.group(0)[2:-1] if is_specific_type is not None else None

    if limit is None:
        await limit_setting1.finish("指定签底参数错误~")

    if limit == "随机":
        image_file, status = fortune_manager.divine(spec_path=None, event=event)
    else:
        spec_path = fortune_manager.limit_setting_check(limit)
        if not spec_path:
            await limit_setting1.finish("还不能指定这种签哦~如果想要加入这种签，可以做好模板后发给可可（像yydz签那样）")
        else:
            image_file, status = fortune_manager.divine(spec_path=spec_path, event=event)
        
    if not status:
        msg = MessageSegment.text("你今天抽过签了，再给你看一次哦🤗\n") + MessageSegment.image(image_file)
    else:
        logger.info(f"User {event.user_id} | Group {event.group_id} 占卜了今日运势")
        msg = MessageSegment.text("✨今日运势✨\n") + MessageSegment.image(image_file)
    
    await limit_setting1.finish(message=msg, at_sender=True)

@refresh.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    fortune_manager.reset_fortune()
    await limit_setting.finish("今日运势已刷新!")

# 重置每日占卜
@scheduler.scheduled_job("cron", hour=0, minute=0)
async def _():
    fortune_manager.reset_fortune()
    logger.info("今日运势已刷新！")