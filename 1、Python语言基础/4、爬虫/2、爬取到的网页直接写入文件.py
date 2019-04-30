import urllib.request

# 一句话搞定，第一个参数是要爬取的网页，第二个参数是保存文件的路径
urllib.request.urlretrieve("http://www.xxsy.net/", r"C:\学习\TempFile\爬虫2.html")

# urllib.request.urlretrieve在执行的过程中，会产生一些缓存
# 清楚缓存
urllib.request.urlcleanup()