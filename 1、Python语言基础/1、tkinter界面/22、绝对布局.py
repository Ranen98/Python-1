import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")
'''
绝对布局
窗口的变化对位置没有影响
'''
label1 = tkinter.Label(win, text="Python")
label2 = tkinter.Label(win, text="C++")
label3 = tkinter.Label(win, text="Java")

label1.place(x=20, y=20)
label2.place(x=60, y=60)
label3.place(x=100, y=100)

win.mainloop()