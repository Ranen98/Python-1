import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
# win.geometry("1024x768+240+20")

# 与之前不同的是，EXTENDED 支持 shift 连选和 ctrl 多选
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED, height=7, width=20)
for i in ["one", "two", "three", "four", "five", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    lb.insert(tkinter.END, i)

# 创建滚动条
scroll = tkinter.Scrollbar(win)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# 关联
scroll.config(command=lb.yview)
lb.config(yscrollcommand=scroll.set)

win.mainloop()