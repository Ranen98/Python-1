import tkinter

def func():
    print(r.get())

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# 绑定变量，如果值是字符串类型，那么变量就要用 StringVar
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="金钱", value=1, variable=r, command=func)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="地位", value=2, variable=r, command=func)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="美女", value=3, variable=r, command=func)
radio3.pack()

win.mainloop()