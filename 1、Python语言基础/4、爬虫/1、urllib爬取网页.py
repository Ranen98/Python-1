import urllib.request

# 向指定的url地址发起请求，并返回服务器响应的数据（文件对象）
response = urllib.request.urlopen("http://www.baidu.com")

# 读取文件的全部内容
data = response.read()
# print(data.decode("utf-8"))
'''
读取一行
data = response.readline()
读取文件的全部内容,会把读取到的数据赋值给一个列表变量
data = response.readlines()
'''
# 将爬取到的数据写入文件
'''
with open(r"C:\学习\TempFile\爬虫.html", "wb") as f:
    f.write(data)
'''
# response 属性
# 返回当前环境的有关信息
print(response.info())
# 返回状态码
print(response.getcode())
# 200 : 成功， 304 ：有缓存， 404 ：没有发现文件， 500 ：服务器有问题
# if response.getcode() == 200 or response.getcode == 304:
#     处理网页信息
#     pass

# 返回当前正在爬取的URL地址
print(response.geturl())

# 编码
url1 = "http://www.xxsy.net/"
url2 = urllib.request.quote(url1)
print(url2)
# 解码
print(urllib.request.unquote(url2))

# 请求地址不能是解码后的地址
response2 = urllib.request.urlopen(url1)
data2 = response2.read().decode("utf-8")
print(data2)