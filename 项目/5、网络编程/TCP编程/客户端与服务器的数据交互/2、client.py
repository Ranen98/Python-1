import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.43.183", 8080))

while True:
    data = input("客户端发送消息：")
    client.send(data.encode("utf-8"))
    # 接收服务器发来的消息
    recvData = client.recv(1024)
    print("服务器发来消息："+recvData.decode("utf-8"))