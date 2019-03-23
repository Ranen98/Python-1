import urllib.request
import os
import re
import ssl
from collections import deque


# 将要爬取的网站
def imageCrawler(url, toPath):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    htmlStr = response.read().decode("gbk")
    # with open(r"C:\学习\Pycharm项目\Python学习\项目\爬虫\1.html", "wb") as f:
    #     f.write(htmlStr)
    # 爬取当前网页下所有的图片网址
    pat1 = r'(tag/\d{0,}\.html|ent/meinvtupian/\d{0,}/\d{0,}\.html)'
    re_url = re.compile(pat1, re.S)
    urlList = re_url.findall(htmlStr)
    urlList = list(set(urlList))
    # print(urlList[0])
    print(urlList)
    print(len(urlList))

    # 爬取当前网页下所有图片
    pat2 = '<img src="((http|https)://t\d.hddhhn.com/uploads/tu/.*?)"'
    re_image = re.compile(pat2, re.S)
    imageUrlList = re_image.findall(htmlStr)
    imageUrlList = list(set(imageUrlList))
    # print(imageUrlList[0][0])
    # print(len(imageUrlList))
    # print(type(imageUrlList))

    # 一个网页一个网页慢慢爬，保存当前网页下爬到的图片
    global num
    for imageUrl in imageUrlList:
        # 图片保存的路径
        imagePath = os.path.join(toPath, str(num)+".jpg")
        urllib.request.urlretrieve(imageUrl[0], imagePath)
        num += 1
    
    return urlList

def center(url, toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()

        urlList = imageCrawler(targetUrl, toPath)
        for URL in urlList:
            queue.append("http://www.2717.com/"+URL)

num = 1
url = "https://www.2717.com/ent/meinvtupian/"
toPath = "C:\学习\Pycharm项目\Python学习\项目\爬虫\image2"
center(url, toPath)


'''
问题出在进入第二个网页时爬不到网址，正则没有匹配上！
明天解决！
https://www.2717.com/tag/649.html
http://www.27270.com/tag/649.html

/ent/meinvtupian/2019/314363.html
https://www.2717.com/ent/meinvtupian/2019/314363.html

(tag/\d{0,}\.html|ent/meinvtupian/\d{0,}/\d{0,}\.html)

'''
