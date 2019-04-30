import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('192.168.43.183', 8900))

while True:
    data, addr = udpServer.recvfrom(1024)
    print("客户端发来消息：", data.decode("utf-8"))