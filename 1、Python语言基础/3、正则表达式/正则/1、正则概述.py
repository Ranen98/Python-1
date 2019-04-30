import re
r'''
Python1.5以后增加了re模块，提供了正则表达式模式
re模块使Python语言拥有了全部的正则表达式功能

re.match函数
原型：match(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，控制正则表达式的方式
re.I: 忽略大小写
re.L: 做本地户识别
re.M: 多行匹配，影响^和$
re.S: 使.匹配包括换行符在内的所有字符
re.U: 根据Unicode字符集解析字符，影响\w, \W, \b, \B
re.X: 使我们以更灵活的格式理解正则表达式
功能：尝试从字符串的起始位置匹配一个模式，匹配成功函数返回，不再继续往下匹配如果不是从起始位置匹配，成功的话，返回None
'''
m1 = re.match("www", "www.baidu.comwww")
m2 = re.match("www", "http://www.baidu.com")
m3 = re.match("www", "wWw.baidu.com", flags=re.I)
# print(m1) # .span():打印位置
# print(m2)
# print(m3)

# **********************************************************************************************

'''
re.search函数
原型(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，控制正则表达式的方式
功能：扫描整个字符串，并返回第一个匹配成功的
'''
s1 = re.search("www", "www.baidu.comwww")
s2 = re.search("www", "http://www.baidu.com")
s3 = re.search("www", "wWw.baidu.com", flags=re.I)
# print(s1)
# print(s2)
# print(s3)

# match 函数与 search 函数的区别就是match从头开始匹配，search从任意位置开始匹配
# **********************************************************************************************

'''
re.findall函数
原型(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，控制正则表达式的方式
功能：扫描整个字符串，并返回结果列表
'''
f1 = re.findall("www", "www.baidu.comwwwhelloWWWww", re.I)
print(f1)