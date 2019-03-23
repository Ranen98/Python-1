import re
'''
字符串切割
'''

strl = "Python   is   the   best   language"
# 基础的切割方法
# print(strl.split(" "))
# 正则也有切割
# print(re.split(r" +", strl))

'''
re.finditer函数
原型(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，控制正则表达式的方式
功能：与findall类似，扫描整个字符串，并返回迭代器
'''
str2 = "Python is the best language, python is easy, python is a computer language！"
r1 = re.finditer("(python)", str2, flags=re.I)
while True:
    try:
        l = next(r1)
        # print(l)
    except StopIteration as e:
        break

'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:正则表达式
repl:   指定的用来替换的字符串
string: 目标字符串
count:  最多替换次数
flags:  标志位
功能：  在目标字符串中以正则表达式的规则匹配字符串，
再把他们替换成指定的字符串。如果不指定替换次数，则替换所有匹配的字符串

区别：sub返回被替换后的字符串，subn返回元组，第一个参数是替换后的字符串，第二个是替换的次数
'''
r2 = re.sub(r"python", "TEMP", str2, count=2, flags=re.I)
r3 = re.subn(r"python", repl="TEMP", string=str2, count=0, flags=re.I)
# print(r2) # <class 'str'>
# print(r3) # <class 'tuple'>

'''
分组
概念：除了简单的判断是否匹配之外，正则表达式还有提取字串的功能。用()表示的就是分组。
(1([358]\d|4[5679]|66|7[35678])\d{8})里面有两个组
'''
str3 = "0835-7628673"
# 分组可以取名字 ?P<name>
r4 = re.findall(r"((?P<Num>\d{4})-(\d{7}))", str3)
print(type(r4[0]))
print(r4[0])
# print(r4.groups())

'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式不合法，则报错
2、用编译后的正则表达式去匹配对象 
compile(pattern, flags=0)
'''
# 把表达式编译成正则对象
pa = r"(1([358]\d|4[5679]|66|7[35678])\d{8})"
re_telephon = re.compile(pa)
# print(re_telephon.findall(r"a18881203952、17380791998、18180006785、7231498905、12909098787、jhk、1888l203952、13981625441"))