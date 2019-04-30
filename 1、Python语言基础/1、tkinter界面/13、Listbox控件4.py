import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# MULTIPLE：多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()
for i in ["one", "two", "three", "four", "five"]:
    lb.insert(tkinter.END, i)


win.mainloop()