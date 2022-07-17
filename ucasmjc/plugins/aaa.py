
import json
import re
import requests
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
text="https://www.bilibili.com/video/BV1GK4y1V7yG"
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
print(up)

