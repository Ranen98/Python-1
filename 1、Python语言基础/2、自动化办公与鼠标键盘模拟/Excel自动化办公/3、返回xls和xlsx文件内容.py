#有序字典
from collections import OrderedDict
#读取数据
from pyexcel_xls import get_data
def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = r"C:\学习\Python语言基础\15、2、自动化办公与鼠标键盘模拟\5、excel自动化办公\sunck.xlsx"
dic = readXlsAndXlsxFile(path)
print(dic["安力博发"])

