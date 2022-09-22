import re
from nonebot import on_command, on_fullmatch, on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,MessageSegment,Message,PrivateMessageEvent,GROUP_ADMIN
import json
from plugins.util import SOURCELOAD,HAOGAN, QA,hgupdate
from nonebot.params import CommandArg
from typing import Union
q=on_command("Q ",priority=5)
@q.handle()
async def get_Q(bot: Bot, event:GroupMessageEvent,args: Message = CommandArg()):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    args = args.extract_plain_text()
    if not args:
        return
    with open(QA,"r+",encoding='utf-8') as f:
            load_dict = json.load(f)
            index=load_dict["index"]
            load_dict["index"]+=1
    with open(QA,"w") as f:
        load_dict[index]={"index":index,"question":args,"answer":[],"length":0}
        json.dump(load_dict,f)
        await q.finish("该问题已收录~，编号为Q"+str(index))
a=on_regex("A\d+\s", flags=re.I)
@a.handle()
async def get_A(bot: Bot, event: Union[PrivateMessageEvent, GroupMessageEvent]):
    usrqq = event.get_user_id()
    with open(HAOGAN,"r+") as f:
        
        load_dict = json.load(f)
        if usrqq in load_dict :
            if load_dict[usrqq]["data"]<0:
                if load_dict[usrqq]["data"]>50:
                    load_dict[usrqq]["data"]=100
                else:
                    load_dict[usrqq]["data"]+=50 
                load_dict[usrqq]["mark"]=0
            else:
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
    with open(HAOGAN,"w") as f:
        json.dump(load_dict,f)
    id = event.get_user_id()
    args=str(event.get_message())
    arg=re.search("A\d+\s",args)
    index=re.search("\d+",arg[0])[0]
    answerdata=re.sub("A\d+\s","",args)
    with open(QA,"r+",encoding='utf-8') as f:
        load_dict = json.load(f)
        if int(index)>=load_dict["index"]:
            await a.finish("还没有这个编号的问题哦")
        for i in load_dict[index]["answer"]:
            if i["id"]==id:
                i["answer"]=answerdata
                with open(QA,"w") as f:
                    json.dump(load_dict,f)
                    await a.finish("您在Q"+str(index)+"的回答已更新")
        answer={"answer":answerdata,"id":id}
        load_dict[index]["answer"].append(answer)
        load_dict[index]["length"]+=1

        with open(QA,"w") as f:
            json.dump(load_dict,f)         
        await a.finish("该回答已收录至Q"+str(index))

qa_list=on_fullmatch("问题列表")
@qa_list.handle()
async def get_list(bot: Bot, event: Union[PrivateMessageEvent, GroupMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    with open(QA,"r+",encoding='utf-8') as f:
        load_dict1 = json.load(f)
    text="该功能建议私聊获取，避免刷屏~\n"
    for i in range(1,load_dict1["index"]):
        q=load_dict1[str(i)]
        if q["length"]==0:
            state="（尚无回答）"
        else:
            state="（已有"+str(q["length"])+"条回答）"
        text+="Q"+str(i)+"."+q["question"]+state+"\n"
    text+="发送“查询”+问题编号获得对应回答~\n例：“查询Q1”"
    await qa_list.finish(text)
a_search=on_regex("查询Q\d*\s?A\d*",priority=4)
@a_search.handle()
async def search_a(bot: Bot, event:Union[PrivateMessageEvent, GroupMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    args=str(event.get_message())
    arg=re.search("查询Q\d*",args)
    q_index=re.search("\d+",arg[0])[0]
    arg=re.search("A\d*",args)
    a_index=re.search("\d+",arg[0])[0]
    with open(QA,"r+",encoding='utf-8') as f:
        load_dict = json.load(f)
        j=1
        length=load_dict[q_index]["length"]
        if length==1:
            await a_search.finish(load_dict[q_index]["answer"][0]["id"])
        for i in load_dict[q_index]["answer"]:
            if str(j)==a_index:
                await a_search.finish(i["id"])
            j+=1
        await a_search.finish("没有查询到该回答")
            
qa_search=on_regex("查询Q\d+",priority=5)
@qa_search.handle()
async def search(bot: Bot, event: Union[PrivateMessageEvent, GroupMessageEvent]):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    args=str(event.get_message())
    arg=re.search("查询Q\d+",args)
    index=re.search("\d+",arg[0])[0]
    with open(QA,"r+",encoding='utf-8') as f:
        load_dict = json.load(f)
    length=load_dict[index]["length"]
    if length==0:
        await qa_search.finish("该提问尚未得到回答，请群里的学长学姐反思一下")
    text="Q "+load_dict[index]["question"]+"\n"
    i=1
    for answer in load_dict[index]["answer"]:
        text+="A"+str(i)+"."+answer["answer"]
        if i!=length:
            text+="\n"
        i+=1
    await qa_search.finish(text)
qa_delete=on_regex("删除Q\d*\s?A\d*",priority=5,permission=GROUP_ADMIN)
@qa_delete.handle()
async def delete(event:GroupMessageEvent):
    usrqq = event.get_user_id()
    hgupdate(usrqq)
    _, group_id, user_id = event.get_session_id().split("_")
    list=["2496767825","1532691970","676759737"]
    if (usrqq not in list)&(group_id!="712646893"):
        return
    args=str(event.get_message())
    arg=re.search("删除Q\d*",args)
    q_index=re.search("\d+",arg[0])[0]
    arg=re.search("A\d*",args)
    a_index=re.search("\d+",arg[0])[0]
    with open(QA,"r+",encoding='utf-8') as f:
        load_dict = json.load(f)
    if load_dict[q_index]["length"]>=int(a_index):
        del load_dict[q_index]["answer"][int(a_index)-1]
        load_dict[q_index]["length"]-=1
        with open(QA,"w") as f:
            json.dump(load_dict,f)    
        await qa_delete.finish("Q"+q_index+"中的第"+a_index+"条回答已被删除")
    else:
            await qa_delete.finish("未找到该回答")

