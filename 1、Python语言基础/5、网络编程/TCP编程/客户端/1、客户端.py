import socket

'''
客户端：创建TCP链接时，主动发起连接的叫做客户端
服务端：接收客户端的连接
'''
# 1、创建一个客户端
# 参数1：指定协议  AF_INET(IPV4)  或 AF_INET6(IPV6)
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、建立连接
# 参数时一个元组，第一个元素是要连接的服务器的IP地址，第二个元素是端口号
sk.connect(("www.baidu.com", 80))

# 这就相当于请求访问一个网址，请求头，请求体什么的都在里面
sk.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# 等待接收数据
data = []
while True:
    # 每次接收2k数据
    tempData = sk.recv(2048)
    if tempData:
        data.append(tempData)
    else:
        break

# 接收到的数据是字节，所以需要我们解码
dataStr = (b"".join(data)).decode("utf-8")

# 断开连接
sk.close()

headers, Html = dataStr.split("\r\n\r\n", 1)
print(Html)