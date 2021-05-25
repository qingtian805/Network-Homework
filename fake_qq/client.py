from socket import *
from threading import Thread

serverName = "127.0.0.1"
serverPort = 60262

def sendMessage(message : str):
    global clientSocket
    clientSocket.send(message.encode())

def receiveMessage():
    global clientSocket
    rec = clientSocket.recv(2048).decode()
    ls = rec.split("\\")
    username = ls[0]
    ls.pop(0)
    rec = '\\'.join(ls)
    return (username, rec)
def disconnect():
    global clientSocket
    clientSocket.shutdown(2)
    clientSocket.close()

clientSocket = socket(AF_INET, SOCK_STREAM) #创建客户端套接字
clientSocket.connect((serverName,serverPort)) #连接服务器

