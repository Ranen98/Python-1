'''
特点：把参数进行打包，单独传输
优点：数量大，安全（当对服务器进行数据修改时用Post）
缺点：速度慢
'''

import urllib.request
import urllib.parse # 对参数进行打包

url = "https://mail.qq.com/"
# 将要发送的数据合成一个字典
data = {"inputstyle":"908647907", "inputstyle password":" "}
# 将数据打包
postData = urllib.parse.urlencode(data).encode("utf-8")
# 请求体
req = urllib.request.Request(url, data=postData)
req.add_header("User-Agent", "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36")
# 发起请求
response = urllib.request.urlopen(req)
ms = response.read().decode("gbk")
print(ms)