import csv

def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
    return infoList

path = r"C:\学习\第1章  Python语言基础\15、2、自动化办公与鼠标键盘模拟\2、读写csv文件\000001.csv"
info = readCsv(path)