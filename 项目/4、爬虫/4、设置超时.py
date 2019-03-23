import urllib.request
'''
如果网页长时间未响应，系统判断超市，无法爬取
'''

for i in range(1, 100):
    try:
        respones = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)
        print(respones.read())
    except:
        print("超时，爬取失败")