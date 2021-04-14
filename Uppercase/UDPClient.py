from socket import * 
serverName = "127.0.0.1" #设置要访问的服务器属性
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #创建套接字，使用IPv4和UDP
message = input("Input a lowercase sentense:")
clientSocket.sendto(message.encode(),(serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #设置有2048长度的收取缓存的套接字
print(modifiedMessage.decode())
clientSocket.close() #关闭套接字
