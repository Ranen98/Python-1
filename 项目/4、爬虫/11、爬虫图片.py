import urllib.request
import re
import os

# toPath:爬下来的图片放在这里
def imageCrawler(url, toPath):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    # with open("C:\学习\Pycharm项目\Python学习\项目\爬虫\糗事百科.html", "wb") as f:
    #     f.write(html)
    pat = r'data-lazy-src="(.*?)" alt'
    re_image = re.compile(pat, flags=re.S)
    imageList = re_image.findall(html)
    # print(imageList)
    # 声明num使全局变量，使二次循环后num可以一直加下去
    global num
    for imageUrl in imageList:
        # 图片的保存路径
        path = os.path.join(toPath, str(num)+".jpg")
        # 下载图片
        urllib.request.urlretrieve(imageUrl, path)
        num += 1

num = 1
for i in range(1,11):
    url = "http://www.qiumeimei.com/page/"+str(i)
    toPath = "C:\学习\Pycharm项目\Python学习\项目\爬虫\image"
    imageCrawler(url, toPath)