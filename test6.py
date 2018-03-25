# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import Message
import json,sys,atexit,datetime
#======================================================================================================
#cl = LineClient()
cl = LineClient("top511324@gmail.com","zaswdc12")
#cl = LineClient(authToken='')
#cl.log("Auth Token : " + str(cl.authToken))
print ("================================Success================================")
#======================================================================================================
tracer = LinePoll(cl)
msg_dict = {}
bl = [""]
#======================================================================================================
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def RECEIVE_MESSAGE(op):
    try:
        msg = op.message
        if msg.toType == 0:
            cl.log("[%s]"%(msg._from)+msg.text)
        else:
            cl.log("[%s]"%(msg.to)+msg.text)
        if msg.contentType == 0:
            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
    except Exception as e:
        print(e)
tracer.addOpInterrupt(26, RECEIVE_MESSAGE)
def NOTIFIED_DESTROY_MESSAGE(op):
    try:
        at = op.param1
        msg_id = op.param2
        if msg_id in msg_dict:
            if msg_dict[msg_id]["from"] not in bl:
                cl.sendMessage(at,"«%s»\n======================\n收回了:\n\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
            del msg_dict[msg_id]
    except Exception as e:
        print(e)
tracer.addOpInterrupt(65, NOTIFIED_DESTROY_MESSAGE)
#======================================================================================================
while True:
    tracer.trace()