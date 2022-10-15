import asyncio
import imp
import json
import os
from nonebot.params import CommandArg
from nonebot.params import CommandArg,ArgStr
from nonebot.plugin import on_command,on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent,PrivateMessageEvent, Message,MessageSegment
from nonebot.typing import T_State
from selenium.webdriver.common.by import By
from selenium import webdriver
from typing import Union
from plugins.util import HAOGAN, hgdown
haohelp = on_fullmatch("绘画帮助", priority=5)
@haohelp.handle()
async def culturehelp_use(bot: Bot, event:Union[GroupMessageEvent,PrivateMessageEvent]):
    usrqq = event.get_user_id()
    daily_send = 'AI绘画(txt2img)\n本功能内置Novelai模型，negative tag已自动填充\n发送"draw"+空格+tags，可获得生成的图像\n例：draw a girl, red eyes\nTIPS:1.该功能仅在群聊中生效，且消耗好感度（如果因队列拥挤而没能发出图片也会消耗哦）\n2.同一时间内只能处理一条绘画指令，生成图像过程中的其余所有指令（包括私聊）可能被忽略\n3.此功能因Novelai的爆火而产生，为限时活动，停机时间未定\n4.tags之间用“,”隔开，可参考知乎/B站，或此链接https://github.com/ucasmjc/qqbot/blob/master/plugins/tag%E8%A1%A8%20-%20%E5%85%A8%E5%B9%B4%E9%BE%84.txt\n5.可能会生成r18+++的图，希望大家不要在tags里加入奇怪的东西'
    await haohelp.finish(daily_send)
txt2img = on_command("draw",  priority=5, block=True)
@txt2img.handle()
async def _(state: T_State, event: GroupMessageEvent, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        state["txt"] = arg.extract_plain_text().strip()
@txt2img.got("txt", prompt="Text is required to generate images")
async def _(bot: Bot, event: GroupMessageEvent, state: T_State, txt_str: str = ArgStr("txt")):
    await txt2img.send("Trying to draw txt: " + txt_str, at_sender=True)
    usrqq = event.get_user_id()
    [data,id]=hgdown(usrqq)
    if data < 0:
        return
    img_out_path = r'C:\Users/24967\Desktop/novelai-naifu/novel-naifu-aki/images/'
    length=len(os.listdir( img_out_path ))
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(5)
    driver.get('http://127.0.0.1:6969/')
    driver.find_element(By.XPATH,'//*[@id="prompt-input-0"]').send_keys(txt_str)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[2]/div[5]/div[4]/textarea').send_keys('NSFW, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet')
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/button').click()
    seed=len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/button'))
    while (seed==0):
        seed=len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/button'))
    seed=driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/button').text
    for i in  os.listdir( img_out_path ):
        if i.endswith(seed+'.png'):
            image=i
    img_out_path=img_out_path+image
    msg_image = MessageSegment("image", {
                "file": 'file:///'+img_out_path
            })
    await txt2img.send(msg_image,at_sender=True)
    os.remove(img_out_path)
    driver.close()
    await asyncio.sleep(1800)
    with open(HAOGAN,"r+") as f:
        load_dict = json.load(f)
        load_dict[usrqq]["index"] = 0
        load_dict[usrqq]["id"] = 0
        with open(HAOGAN,"w") as f:
            json.dump(load_dict,f)



    




