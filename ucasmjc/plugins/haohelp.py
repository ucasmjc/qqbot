from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,PrivateMessageEvent
from typing import Union
haohelp = on_fullmatch("好感度帮助", priority=5)
@haohelp.handle()
async def haohelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    daily_send = '好感度系统：\n每个人的初始好感度为60，每日第一次使用臻果姬时（下述功能除外），好感度会增长50点\n发送“好感度”即可查询当前好感度，不同好感度可能有彩蛋哦，频繁查询也会降低臻果姬对你的好感度~\n\n频繁使用“涩图”，“色图”，“戳一戳”功能时，臻果姬会生气哦\n\n当你在30分钟内第二次使用上述功能时，好感度会-20，第三次使用时，好感度会-40，第四次会-80……30分钟的计时会也随好感度减少而刷新（即重新计时）\n不同功能的计时是相互独立的哦\n\n当你的好感度小于0，臻果姬将关闭对你的一些功能哦\n防止刷屏，保护臻果姬从现在做起~'
    await haohelp.finish(daily_send)
qahelp = on_fullmatch("QA帮助", priority=5)
@qahelp.handle()
async def qahelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    daily_send = 'QA系统\n为了帮助新的果壳er熟悉校园生活，臻果姬来帮助大家记录水群期间的问答\n-当你想提问时，在问题前加个"Q "，臻果姬便会记录下来此问题，并告诉你问题编号（如Q1)，例如“Q B班线代老师选谁好？”(Q后边的空格很重要哦！)\n-当你想回答问题时，只需在消息开头加个前缀，例如，想回答问题Q1时，可以发送“A1 李子明老师好，blabla"(A1后边的空格很重要哦！)，A后的数字和你要回答的问题编号是一致的。打错字了也没关系，重新发送会覆盖你之前的回答。\n\nPS:回答问题还可以提高臻果姬对你的好感度，一次50点！\n\n以下功能也支持私聊臻果姬获取：\n-发送“问题清单”可以查询当前存在的问题\n-发送“查询”+问题编号,可以查看该问题的回答，例如“查询Q1”\n-发送“查询”+问题编号+回答编号可查询对应的回答者，如“查询Q1A1"\n\n希望大家在提问前先查看问题列表（也可以通过私聊查看），避免重复提问，也希望回答者不要恶意作答哦，这将会是22级同学与大家的共同作品'
    await qahelp.finish(daily_send)
   