from socket import *
serverPort = 12000 #设置服务器属性
serverSocket = socket(AF_INET, SOCK_DGRAM) #创建套接字，使用IPv4和UDP
serverSocket.bind(('', serverPort)) #将端口12000绑定
print("The server is ready to receive!")
while True:
    message, clientAddress = serverSocket.recvfrom(2048) #2048大小的接受缓存
    print("received message: " + message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) #发送modified到客户端
