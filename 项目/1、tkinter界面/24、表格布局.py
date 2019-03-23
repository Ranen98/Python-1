import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

button1 = tkinter.Button(win, text="黄玉珠", bg="red")
button2 = tkinter.Button(win, text="黄玉枭", bg="orange")
button3 = tkinter.Button(win, text="黄锐浪", bg="yellow")
button4 = tkinter.Button(win, text="黄西卓", bg="green")
button5 = tkinter.Button(win, text="黄玉飞", bg="blue")

# 表格布局
button1.grid(row=0, column=0)
button2.grid(row=0, column=2)
button3.grid(row=1, column=1)
button4.grid(row=2, column=0)
button5.grid(row=2, column=2)

win.mainloop()