import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

def func(event):
    print(event.x, event.y)

label = tkinter.Label(win, text="Button", bg="grey")
label.place(x=200, y=200)
label.bind("<ButtonRelease-1>", func)

win.mainloop()