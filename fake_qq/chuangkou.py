import tkinter as tk
import time
from client import receiveMessage,sendMessage,disconnect
from threading import Thread
 
# 发送消息
def sendMsg():
    t1_Msg.configure(state=tk.NORMAL)
    strMsg = time.strftime("%Y-%m-%d %H:%M:&S".center(88), time.localtime())+'我:'.rjust(88)+'\n'
    t1_Msg.insert("end", strMsg, 'green')
    sendMsg = t2_sendMsg.get('0.0', 'end')
    t1_Msg.insert("end", sendMsg)
    t2_sendMsg.delete('0.0', "end")
    t1_Msg.config(state=tk.DISABLED)
    sendMessage(sendMsg)
    #print(strMsg + sendMsg)
 
# 创建窗口
app = tk.Tk()
app.title('俺是聊天框')
 
#
w = 800
h = 700
sw = app.winfo_screenwidth()
sh = app.winfo_screenheight()
x = 200
y = (sh - h) / 2
app.geometry("%dx%d+%d+%d" % (w, h, x, y))
app.resizable(0, 0)
 
 
# 聊天消息预览窗口
t1_Msg = tk.Text(width=88, height=30)
t1_Msg.insert("end","欢迎使用！请发送第一条信息作为用户名".center(88))
t1_Msg.tag_config('green', foreground='#008C00') 
t1_Msg.place(x=2, y=35)
t1_Msg.config(state=tk.DISABLED)
 
# 聊天消息发送
t2_sendMsg = tk.Text(width=80, height=8)
t2_sendMsg.place(x=2, y=540)

# 发送按钮
sendMsg_btn = tk.Button(text="发送（Send）", command=sendMsg, width=14,height=5)
sendMsg_btn.place(x=680, y=570)

# 处理关闭
def closing():
    global app,recvThread
    disconnect()

    app.quit()
app.protocol("WM_DELETE_WINDOW", closing)

# 接收信息函数与线程
def recvWhile():
    global t1_Msg
    while True:
        user,sendMsg = receiveMessage()
        print((user,sendMsg))
        strMsg = time.strftime("%Y-%m-%d %H:%M:&S".center(88), time.localtime())+ user.rjust(88)+'\n'
        t1_Msg.config(state=tk.NORMAL)
        t1_Msg.insert("end", strMsg, 'green')
        t1_Msg.insert("end", sendMsg)
        t1_Msg.config(state=tk.DISABLED)

recvThread = Thread(target= lambda : recvWhile(),daemon=True)
recvThread.start()

# 主事件循环
app.mainloop()
