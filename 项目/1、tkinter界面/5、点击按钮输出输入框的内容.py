import tkinter

def showInfo():
    print(entry.get())
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

entry = tkinter.Entry(win)
entry.pack()
button = tkinter.Button(win, text="按钮", command=showInfo)
button.pack()

win.mainloop()