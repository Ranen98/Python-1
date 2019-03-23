import re
'''
总结出的主流邮箱的命名规则：
3-18位
字母或数字开头
不能全为数字
可用字母、数字、英文句点、减号、下划线。
英文字母或者数字结尾
常见邮箱：qq.com, sina.com, sohu.com, 126.com,163.com, gmail.com, hotmail.com
'''
def judgeMail(str):
    r = re.findall(r"([0-9a-zA-Z]([\w|\.|_]{2,16})[0-9a-zA-Z]@(qq|sina|sohu|126|163|gmail|hotmail|)\.com)", str)
    print(r)
    return r

str = "908647907@qq.com、hjhad6312897@hj.com、你好呀Python，ruilang98@outlook.com,1007718951@sina.com,_908647907@qq.com;9908_9087217jkd@126.com,874jhcsf1749xksjfhkj295@sohu.com_"
judgeMail(str)