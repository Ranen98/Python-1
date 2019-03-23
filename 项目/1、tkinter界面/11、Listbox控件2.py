import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# 绑定变量
lbv = tkinter.StringVar()
# 与 BROWSE 不同的是，SINGLE 不支持鼠标按下后滑动选中。
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()
for i in ["one", "two", "three", "four", "five"]:
    lb.insert(tkinter.END, i)

# 打印listbox中当前的选项
print(lbv.get())
# 设置listbox中的选项
lbv.set(("0", "1", "2", "3", "4"))

# 绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>", myPrint)

win.mainloop()