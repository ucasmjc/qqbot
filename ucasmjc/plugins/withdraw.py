import asyncio
from nonebot.adapters.onebot.v11 import Bot
from nonebot.log import logger
import json

async def add_withdraw_job(bot: Bot, qq,id,name):
    logger.info(f'添加定时任务，间隔：10秒')
    await asyncio.sleep(1800)
    with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","r+") as f:
        load_dict = json.load(f)
        if load_dict[qq][name]["id"] != id:
            return
        load_dict[qq][name]["index"] = 0
        load_dict[qq][name]["id"] = 0
        with open("C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/haogan.json","w") as f:
            json.dump(load_dict,f)
    
    

