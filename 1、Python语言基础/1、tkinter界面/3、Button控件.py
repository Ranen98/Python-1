import tkinter

def func():
    print("Python")

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# 创建按钮
button = tkinter.Button(win, text="按钮", command=func)
button.pack()


win.mainloop()