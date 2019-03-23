import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("客户端发送消息：")
    client.sendto(data.encode("utf-8"), ('192.168.43.183', 8900))