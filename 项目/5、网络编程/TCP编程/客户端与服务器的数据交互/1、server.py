import socket
import re
# 创建一个服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 给服务器配置IP和端口
server.bind(("192.168.43.183", 8080))

# 监听
server.listen(5)
print("服务器已启动，等待接收数据...")

# 等待连接
clientSocket, clientAddress = server.accept()
pat = r"(\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})"
re_ip = re.compile(pat, re.S)
IP = re_ip.findall(str(clientSocket))
print("<%s>已连接"%IP[0])

while True:
    data = clientSocket.recv(1024)
    print("客户端发来消息：{0}".format(data.decode("utf-8")))
    sendData = input("服务器发送消息：")
    clientSocket.send(sendData.encode("utf-8"))
