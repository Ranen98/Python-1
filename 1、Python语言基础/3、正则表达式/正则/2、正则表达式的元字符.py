import re

# 匹配单个字符与数字
r'''
.  ：匹配出换行符以外的任意字符
[] ：[] 是字符集合，表示匹配方括号中所包含的任意一个字符
     [Python] 匹配'P', 'y', 't', 'h', 'o', 'n'
     [a-z] 匹配任意小写字母
     [A-Z] 匹配任意大写字母
     [0-9] 匹配任意数字
     [0-9a-zA-Z] 匹配任意数字和字母
     [0-9a-zA-Z_] 匹配任意数字、字母和下划线
     [^Python] 匹配除了'P', 'y', 't', 'h', 'o', 'n'这几个字母以外的所有字符，^ 称为脱字符，表示不匹配集合中的字符
     [^0-9] 匹配所有的非数字字符  
\d ：匹配所有的数字，等同 [0-9]
\D ：匹配非数字字符，等同 [^0-9]
\w ：匹配数字、字母和下划线，等同 [0-9a-zA-Z_]
\W ：匹配非数字、字母和下划线，等同 [^0-9a-zA-Z_]
\s ：匹配任意的空白符(空格、换行、回车、换页、制表、)，等同[ \f\n\r\t]
\S ：匹配任意非空白符，等同 [^ \f\n\r\t]

'''
r1 = re.findall(".y", "5iPython, study python make me happy")
# print(r1)
r2 = re.findall("[a-z]", "5iPython, study python make me happy")
# print(r2)

# 锚字符（边界字符）
'''
^  ：行首匹配，和 [] 里的 ^ 不是一个意思
$  ：行尾匹配
\A ：匹配字符串开始，与 ^ 的区别是， \A 只匹配整个字符串的开头，即使再re.M模式下也不会匹配其它行的行首
\Z ：匹配字符串结尾，与 $ 的区别是， \Z 只匹配整个字符串的结尾，即使再re.M模式下也不会匹配其它行的行尾
\b ：匹配一个单词的边界，即单词和空格间的位置
\B ：匹配非单词边界

'''
r3 = re.search("py$", "5iPython, study python make me happy")
# print(r3)
r4 = re.findall("\A5iPython", "5iPython, study python make me happy\n5iPython", flags=re.M)
r5 = re.findall("^5iPython", "5iPython, study python make me happy\n5iPython", flags=re.M)
# print(r4)
# print(r5)
r6 = re.search(r"dy\b", " 5iPython, study python make me happy")
# <re.Match object; span=(14, 16), match='dy'>
# print(r6)
r7 = re.findall(r"th\B", " 5iPython, study python make me happy,both ")
# print(r7)

# 匹配多个字符
'''
(xyz) ：匹配小括号里的xyz
x?    ：匹配0个或一个x
x*    ：匹配0个或任意多个x
.*    ：匹配0个或任意多个字符
x+    ：匹配至少一个x
x{n}  ：匹配确定的n个x（n>=0）
x{n,} ：匹配至少n个x
x{n, m}：匹配至少n个最多m个x（n<=m）
x|y   ：匹配 x 或 y 
'''
r8 = re.findall("(Python)", "5iPython, study python make me happy", flags=re.I)
# print(r8)
r9 = re.findall("p?", "5iPython, study python make me happy")
# print(r9)
r10 = re.findall("A*", "5iPython, study python make me happy，AAABAABAAA")
# print(r10)
r11 = re.findall(".*", "5iPython, study python make me happy，AAABAABAAA")
# print(r11)
r12 = re.findall("A+", "5iPython, study python make me happy，AAABAABAAA")
# print(r12)
r13 = re.findall("A{3}", "5iPython, study python make me happy，AAABAABAAABBAAAAA")
# print(r13)
r14 = re.findall("A{3,}", "5iPython, study python make me happy，AAABAABAAABBAAAAA")
# print(r14)
r15 = re.findall("A{3,5}", "5iPython, study python make me happy，AAABAABAAABBAAAAABBaAAAAAAAAA")
# print(r15)
r16 = re.findall("((P|p)ython)", "5iPython, study python make me happy")
# print(r16)

# 需求，提取5iPython......happy
str = "5iPython, study python make me happy,i am very happy"
r17 = re.findall("(5iPython.*?happy)", str)
print(r17) # 非贪婪匹配

# 特殊匹配
'''
*?  / +?  / x?  ：最小匹配（非贪婪匹配）
'''