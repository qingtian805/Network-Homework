# 计算机网络课程作业存储库
## Network-uppercase
客户端发送一个包含字符串的数据包，服务器将所有字符全部取大写后返回，客户端回显
### TCPClient.py TCPServer.py 
    使用TCP协议的实现
### UDPClient.py UDPServer.py
    使用UDP协议的实现
## Fake-qq
实现一个简单的聊天软件，并且带有简易GUI。服务器可以管理所有连入的客户端并向所有记录客户端进行多播
### chuangkou.py
    简易GUI，由一个目前没有Github帐号的人主持编写，后来由我连接加入了网络功能
### client.py server.py
    网络功能实现模块，client作为一个模块使用，server是服务端需要运行的唯一代码
### clientX.py
    测试使用的三个超简易客户端，调用client.py但没有GUI
