from socket import *
from threading import Thread

#使用同样的序号来关联用户和连接(UID?)
connectDict = {} #连接socket字典，注册字典

def multiSending(message : str, exclude : socket = None): #多播函数，向所有客户端发送信息，exclude是忽略用户
    global connectDict
    destiny = connectDict.keys()
    #预处理发送目标与信息
    if exclude == None: #没有忽略用户，信息前加系统
        message = "system\\" + message
    else: #有忽略用户，不发送给忽略用户并将忽略用户名加在前面
        destiny = list(destiny)
        destiny.remove(exclude)
        message = connectDict.get(exclude) + "\\" + message
    for connect in destiny: #遍历发送
        connect.send(message.encode())

def messageProcess(connect:socket): #信息处理，接受、分析、多播
    while True:
        message = connect.recv(2048).decode()
        print(message)
        if not message: #如果断开，则跳出循环，结束线程
            connect.shutdown(2)
            connect.close()
            break
        else: #没有断开，进行多播
            multiSending(message, connect)

if __name__ == "__main__":
    serverPort = 60262 
    serverSocket = socket(AF_INET, SOCK_STREAM) #使用IPv4和TCP协议
    serverSocket.bind(('',serverPort)) #绑定到60262端口
    serverSocket.listen(10) #监听，允许10个并发连接
    #处理连接
    while True:
        connectionSocket, addr = serverSocket.accept() #接受一个连接
        username = connectionSocket.recv(2048).decode() #收取一个信息，默认第一条信息为用户名
        connectDict[connectionSocket] = username #将连接加入连接字典中
        newThread = Thread(target=lambda : messageProcess(connectionSocket)) #创建新进程用于之后的处理
        newThread.start()
    