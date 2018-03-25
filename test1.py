from linepy import *
import timeit
from datetime import datetime
from time import strftime
import time,random,sys,os
#======================================================================================================
#client = LineClient()
client = LineClient(id='top511324@gmail.com', passwd='zaswdc12')
#client = LineClient(authToken='')
#client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))
#======================================================================================================
cl = client
poll = LinePoll(client)
#======================================================================================================
mid = cl.getProfile().mid
Bots=[mid]
admin=["u2b37602c4f9f8d54917de47b09749130","u67f1283db3cb9a8d694b2b0746cea56e"]
owner=["u2b37602c4f9f8d54917de47b09749130"]
whitelist=["u2b37602c4f9f8d54917de47b09749130","u67f1283db3cb9a8d694b2b0746cea56e"]
#======================================================================================================
wait = {
    'autoJoin':True,
    'leaveRoom':True,
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
setTime = {}
setTime = wait2['setTime']
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
while True:
  try:
    ops=poll.singleTrace(count=50)
    if ops != None:
      for op in ops:
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print ("自動進群關閉")
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
          msg = op.message
          msg.from_ = msg._from
          sender = msg._from
          receiver = msg.to
#======================================================================================================
          if msg.text in ["Sp"]:
            if msg.from_ in admin:
                time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                str1 = str(time0)
                cl.sendText(msg.to, str1 + "秒")
          if msg.text in ["啊嘶","啊嘶","啊嘶嘶","啊嘶嘶嘶","啊嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶","啊嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶"]:
              cl.sendText(msg.to, "啊嘶")
          if msg.text in ["Rebot"]:
            if msg.from_ in admin:
              print ("===================================重新啟動===================================")
              cl.sendText(msg.to, "重啟中")
              restart_program()
              cl.sendText(msg.to,van)
          if msg.text in ["Tagall"]:
            if msg.from_ in admin:
              group = client.getGroup(receiver)
              nama = [contact.mid for contact in group.members]
              nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
              if jml <= 100:
                  client.mention(receiver, nama)
              if jml > 100 and jml < 200:
                  for i in range(0, 100):
                      nm1 += [nama[i]]
                  client.mention(receiver, nm1)
                  for j in range(101, len(nama)):
                      nm2 += [nama[j]]
                  client.mention(receiver, nm2)
              if jml > 200 and jml < 300:
                  for i in range(0, 100):
                      nm1 += [nama[i]]
                  client.mention(receiver, nm1)
                  for j in range(101, 200):
                      nm2 += [nama[j]]
                  client.mention(receiver, nm2)
                  for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                  client.mention(receiver, nm3)
              if jml > 300 and jml < 400:
                  for i in range(0, 100):
                      nm1 += [nama[i]]
                  client.mention(receiver, nm1)
                  for j in range(101, 200):
                      nm2 += [nama[j]]
                  client.mention(receiver, nm2)
                  for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                  client.mention(receiver, nm3)
                  for l in range(301, len(nama)):
                      nm4 += [nama[l]]
                  client.mention(receiver, nm4)
              if jml > 400 and jml < 501:
                  for i in range(0, 100):
                      nm1 += [nama[i]]
                  client.mention(receiver, nm1)
                  for j in range(101, 200):
                      nm2 += [nama[j]]
                  client.mention(receiver, nm2)
                  for k in range(201, len(nama)):
                      nm3 += [nama[k]]
                  client.mention(receiver, nm3)
                  for l in range(301, len(nama)):
                      nm4 += [nama[l]]
                  client.mention(receiver, nm4)
                  for m in range(401, len(nama)):
                      nm5 += [nama[m]]
                  client.mention(receiver, nm5)
          if msg.text in ["Clear"]:
            if msg.from_ in admin:
              if msg.toType == 2:
                  group = cl.getGroup(msg.to)
                  gMembMids = [contact.mid for contact in group.invitee]
                  for _mid in gMembMids:
                      cl.cancelGroupInvitation(msg.to,[_mid])
                  cl.sendText(msg.to,"已清除")
          elif msg.text in ["S"]:
            if msg.from_ in admin:
              cl.sendText(msg.to, "已設置已讀點")
              try:
                del wait2['readPoint'][msg.to]
                del wait2['readMember'][msg.to]
              except:
                pass
              now2 = datetime.now()
              wait2['readPoint'][msg.to] = msg.id
              wait2['readMember'][msg.to] = ""
              wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
              wait2['ROM'][msg.to] = {}
          elif msg.text in ["R"]:
            if msg.from_ in admin:
                  if msg.to in wait2['readPoint']:
                      if wait2["ROM"][msg.to].items() == []:
                          chiya = ""
                      else:
                          chiya = ""
                          for rom in wait2["ROM"][msg.to].items():
                              chiya += rom[1] + "\n"

                      cl.sendText(msg.to, "☆已讀順序☆%s\n\n☆已讀者☆\n%s\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                  else:
                      cl.sendText(msg.to, "請先輸入S")
          elif msg.text in ["Creator"]:
            cl.sendMessage(receiver, None, contentMetadata={"mid":"u2b37602c4f9f8d54917de47b09749130"}, contentType=13)
#======================================================================================================
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[☆]" + Name
                wait2['ROM'][op.param1][op.param2] = "[☆]" + Name
                print (time.time() + name)
            else:
              cl.sendText
          except:
             pass
        poll.setRevision(op.revision)
  except Exception as e:
      client.log("[SINGLE_TRACE] ERROR : " + str(e))
