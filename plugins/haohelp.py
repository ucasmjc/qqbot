from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
from typing import Union
import json
from plugins.util import SOURCELOAD,HAOGAN, hgdown,hgupdate,hgget
haohelp = on_fullmatch("好感度帮助", priority=5)
@haohelp.handle()
async def haohelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    daily_send = '好感度系统V2.0：\nPS:好感度系统仅在22官方群生效\n每个人的初始好感度为60，每日第一次使用臻果姬的非娱乐功能时，好感度会增长50点\n\n如果频繁使用娱乐功能，臻果姬（管理员）会生气哦\n当你在30分钟内第二次使用娱乐功能时，好感度会-40，第三次使用时，好感度会-80，第四次会-120……30分钟的计时会也随好感度减少而刷新（即重新计时）\n娱乐功能主要包括：运势，抽签，emoji合成，crazy4，猫猫，戳一戳，占卜，好感度查询……\n\n不同功能的计时是互通的哦\n发送“好感度”即可查询当前好感度,当好感度为负数时，可以私聊查询哦\n\n当你的好感度小于0，臻果姬将关闭对你的娱乐功能哦\n防止刷屏，保护臻果姬从现在做起~'
    await haohelp.finish(daily_send)
qahelp = on_fullmatch("QA帮助", priority=5)
@qahelp.handle()
async def qahelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    await qahelp.send(MessageSegment("image", {
                "file": 'file:///'+SOURCELOAD+'qahelp.jpg'
            }))
    daily_send = 'QA系统\n为了帮助新的果壳er熟悉校园生活，臻果姬来帮助大家记录水群期间的问答\n-当你想提问时，在问题前加个"Q "，臻果姬便会记录下来此问题，并告诉你问题编号（如Q1)，例如“Q B班线代老师选谁好？”(Q后边的空格很重要哦！)\n-当你想回答问题时，只需在消息开头加个前缀，例如，想回答问题Q1时，可以发送“A1 李子明老师好，blabla"(A1后边的空格很重要哦！)，A后的数字和你要回答的问题编号是一致的。打错字了也没关系，重新发送会覆盖你之前的回答。如果不小心回答岔了问题，可以联系管理员删除回答\n\nPS:回答问题还可以提高臻果姬对你的好感度，一次50点！\n\n以下功能也支持私聊臻果姬获取：\n-发送“问题列表”可以查询当前存在的问题\n-发送“查询”+问题编号,可以查看该问题的回答，例如“查询Q1”\n-发送“查询”+问题编号+回答编号可查询对应的回答者，如“查询Q1A1"\n\n希望大家在提问前先查看问题列表（也可以通过私聊查看），避免重复提问，也希望回答者不要恶意作答哦，这将会是22级同学与大家的共同作品'
culturehelp = on_fullmatch("果壳文化", priority=5)
@culturehelp.handle()
async def culturehelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    daily_send = '果壳的校园虽小，活动却不少，直接发送下列活动的名字获得相应视频，领略果壳的校园文化吧！\n草地音乐节\n军训vlog\n迎新晚会\n音乐之夜\n元旦晚会\n社团文化节\nFREE舞蹈节\n（下面是私货）\n美式霸凌\n果壳迷踪\n果壳良品设计集'
    await culturehelp.finish(daily_send)
   