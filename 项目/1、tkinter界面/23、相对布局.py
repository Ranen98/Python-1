import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")
'''
相对布局
窗口变化对位置有影响
'''
label1 = tkinter.Label(win, text="Python", bg="blue")
label2 = tkinter.Label(win, text="C++", bg="red")
label3 = tkinter.Label(win, text="Java", bg="yellow")
label4 = tkinter.Label(win, text="Python", bg="blue")

label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack(fill=tkinter.X, side=tkinter.BOTTOM)
label4.pack(fill=tkinter.Y, side=tkinter.RIGHT)

win.mainloop()