import re
'''
5位数到10位数
开头不能为0
第一个QQ号是10001
全为数字构成
'''
def judgeQQ(str):
    r = re.findall(r"[1-9]\d{4,9}", str)
    print(r)
    return r

str = r"10000、1000、10001、908647907、1460931460、1007718951、101020102010230098080980、09878917、9086469O7"
judgeQQ(str)
