import csv

def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)

path = r"C:\学习\Pycharm项目\Python学习\项目\自动化办公与鼠标键盘模拟\001.csv"
writeCsv(path, [[1, 2, 3], ["a", "b", "c"], [0, 0, 0]])

