import os
from nonebot.params import CommandArg
from nonebot.params import CommandArg,ArgStr
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, Message,MessageSegment
from nonebot.typing import T_State
from selenium.webdriver.common.by import By
from selenium import webdriver

txt2img = on_command("draw", aliases={"dream"}, priority=5, block=True)
@txt2img.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        state["txt"] = arg.extract_plain_text().strip()
@txt2img.got("txt", prompt="Text is required to generate images")
async def _(bot: Bot, event: MessageEvent, state: T_State, txt_str: str = ArgStr("txt")):
    await txt2img.send("Trying to draw txt: " + txt_str, at_sender=True)
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
    a=1
    while(a==1):
        seed=len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/button'))
        while (seed==0):
            seed=len(driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/button'))
        a=0
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
    driver.switch_to_alert().accept()  


    




