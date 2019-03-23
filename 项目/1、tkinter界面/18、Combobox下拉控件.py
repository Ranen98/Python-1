import tkinter
from tkinter import ttk
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

# 绑定变量
v = tkinter.StringVar()
combobox = ttk.Combobox(win, textvariable=v)
combobox.pack()

combobox["value"] = ["Python", "C++", "Java"]

# 设置默认值,括号里面是索引值。
combobox.current()

# 绑定事件
def func(event):
    print(v.get())
combobox.bind("<<ComboboxSelected>>", func)

win.mainloop()