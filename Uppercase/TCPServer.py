from socket import *
serverPort = 24000 #设置服务器属性
serverSocket = socket(AF_INET, SOCK_STREAM) #创建套接字，使用IPv4和UDP
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive!")
while True:
    connectionSocket, addr = serverSocket.accept() #接受套接字
    sentense = connectionSocket.recv(1024).decode()
    print("received message: " + sentense)
    modifiedSentense = sentense.upper()
    connectionSocket.send(modifiedSentense.encode()) #发送套接字
    connectionSocket.close()