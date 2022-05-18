from threading import Thread
import random
import time
import os
import signal
import sys
import wx

from library import encrypt, decrypt, ConvertToStr, ConvertToInt
#Script.py "name", "n", "e", "d"
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.Show(True)
        def OnExit(event):
            done=False
            while not done:
                try:
                    os.remove(MY_FILE)
                    os.rmdir(MY_LOCATION)
                    done=True
                except:
                    pass
            os._exit(0)
        self.Bind(wx.EVT_CLOSE, OnExit)

app = wx.App(False)

MY_FILE = ""
OTHER_FILE = ""
MY_LOCATION = ""
OTHER_LOCATION = ""
BASE = "./users"
OTHER=""
other_n=''
other_e=''
user_name = sys.argv[1]
user_n = int(sys.argv[2])
user_e = int(sys.argv[3])
user_d = int(sys.argv[4])
#!--------------------------------------------------
#intialization
if not os.path.exists(BASE):
    os.mkdir(BASE)
MY_LOCATION = BASE+"/"+user_name+"/"
if not os.path.exists(MY_LOCATION):
    os.makedirs(MY_LOCATION)
    MY_FILE = MY_LOCATION+user_name+".txt"
    file = open(MY_FILE, "w")
else:
    print("User already exists")
    sys.exit(0)
file.write(str(user_n)+'\n'+str(user_e)+'\n')
file.close()
#!--------------------------------------------------
frame1 = MyFrame(None, user_name)
frame1.control.AppendText("Welcome to the chat room, " + user_name)

def Frame1_select_user_IO(_):
	global OTHER
	string=frame1.control.GetValue()
	lines=string.split('\n')
	if len(lines)>0:
		val=lines[-1]
		OTHER=val
		frame1.control.AppendText('\n')

def Frame1_sending_routine_IO(_):
	string=frame1.control.GetValue()
	lines=string.split('\n')
	if len(lines)>0:
		val=lines[-1]
		message=val
		frame1.control.AppendText('\n')
		file = open(OTHER_FILE, "a")
		#?---------------------
		#logic
		enc_message = encrypt(other_n, other_e, message)[0]
		#?---------------------
		for item in enc_message:
			print(str(ConvertToInt(item)))
			file.write(str(ConvertToInt(item))+'\n')
			file2=open(MY_FILE, "static\channel-in.txt")
			file2.write(str(ConvertToInt(item))+'\n')
			file2.close()
		file.close()

def select_user():
	global OTHER,other_n,other_e,OTHER_ID,OTHER_FILE
	frame1.Bind(wx.EVT_TEXT_ENTER, Frame1_select_user_IO)
	correct_other_user = False
	while not correct_other_user:
		frame1.control.AppendText("\n")
		dir_list = os.listdir(BASE)
		frame1.control.AppendText("Those are the Avalible users:\n")
		for item in dir_list:
			if item != user_name:
				frame1.control.AppendText(item+'\n')
		frame1.control.AppendText("Select the user you want to chat with, (Enter r to refresh): \n")
		while OTHER=='':
			pass
		if OTHER == "r":
			frame1.control.Clear()
			OTHER=""
			continue
		OTHER_LOCATION = BASE+"/"+OTHER+"/"
		if not os.path.exists(OTHER_LOCATION):
			frame1.control.AppendText("User does not exist\n")
			OTHER=""
		else:
			correct_other_user = True
	frame1.control.AppendText("_______________________________________\n")
	dir_list = os.listdir(OTHER_LOCATION)
	OTHER_ID = dir_list[0]
	OTHER_FILE = OTHER_LOCATION+dir_list[0]
	file = open(OTHER_FILE, "r")
	lines = file.readlines()
	file.close()
	file = open(OTHER_FILE, "w")
	file.close()
	other_n=int(lines[0][:-1])
	other_e=int(lines[1][:-1])
	frame1.Bind(wx.EVT_TEXT_ENTER, Frame1_sending_routine_IO)

Thread(target=select_user, args=()).start()
#!--------------------------------------------------
def reciving_routine():
    while 1:
        file = open(MY_FILE, "r")
        lines = file.readlines()
        file.close()
        if len(lines) > 0:
            data = []
            for line in lines:
                if line[-1] == '\n':
                    data.append(line[:-1])
                else:
                    data.append(line)
            if data[0]==str(user_n):
                continue
            #?---------------------
			#logic
            for item in data:
                item = ConvertToStr(int(item))
                message = decrypt(user_n, user_d, item)[0]
                frame1.control.AppendText(OTHER+": "+message+'\n')
            #? --------------------
            file = open(MY_FILE, "w")
            file.close()
        time.sleep(0.1)

Thread(target=reciving_routine, args=()).start()
#!--------------------------------------------------
app.MainLoop()