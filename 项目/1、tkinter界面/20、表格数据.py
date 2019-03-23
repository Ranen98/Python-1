import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

# 创建表格
tree = ttk.Treeview(win)
tree.pack()

# 定义列
tree["columns"] = ("姓名", "年龄", "学号", "班级")

# 设置列
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("学号", width=100)
tree.column("班级", width=100)

# 设置表头
tree.heading("姓名", text="姓名-Name")
tree.heading("年龄", text="年龄-Age")
tree.heading("学号", text="学号-Sno")
tree.heading("班级", text="班级-Class")

# 添加数据
tree.insert("", 0, text="1", value=("黄锐浪", "20", "201610803060", "网络工程二班"))
tree.insert("", 1, text="2", value=("秦丹梅", "20", "201610803060X", "四年级三班"))

win.mainloop()