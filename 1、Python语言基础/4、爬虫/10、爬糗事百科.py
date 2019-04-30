import urllib.request
import re

# 糗事百科爬取
def scandalCyclopediaCrawler(url):
    # 请求头
    header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"}
    # 请求体
    req = urllib.request.Request(url, headers=header)
    # 发起请求
    response = urllib.request.urlopen(req)
    # 爬到的HTML网页
    HTML = response.read().decode("utf-8")
    return HTML

# 正则过滤
def reFilter(html):
    dic = {}
    # 爬取用户名
    userNameList = re.findall(r"<h2>\n(.*?)\n</h2>", html, flags=re.S)
    # 爬取段子
    jokeList = re.findall(r'<div class="content">\n<span>\n\n\n(.*?)\n</span>', html, flags=re.S)
    # 存入字典 用户名：段子
    for i in range(len(userNameList)):
        dic[userNameList[i]] = jokeList[i]
    return dic

def main():
    for i in range(1, 5):
        url = r"https://www.qiushibaike.com/text/page/"+str(i)+"/"
        # 爬到的数据，同上面HTML
        crawData = scandalCyclopediaCrawler(url)
        # 过滤后的数据
        filterData = reFilter(crawData)
        for k, v in filterData.items():
            jokeInfo = k+"：\n"+ v
            print(jokeInfo)
            # 刚开始用w方式写入文件，结果只有最后一条。追加文件用a
            with open(r"C:\学习\Pycharm项目\Python学习\项目\爬虫\糗事百科.txt", "a") as f:
                f.write(jokeInfo)

if __name__ == '__main__':
    main()