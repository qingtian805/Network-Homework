from socket import *
serverName = "127.0.0.1" #设置要访问的服务器属性
serverPort = 24000
clientSocket = socket(AF_INET, SOCK_STREAM) #创建套接字，使用IPv4和TCP
clientSocket.connect((serverName, serverPort)) #建立连接

sentence = input("Input a lowercase sentense:")
clientSocket.send(sentence.encode()) 

modifiedSentense = clientSocket.recv(1024) 
print(modifiedSentense.decode()) 
clientSocket.close() 