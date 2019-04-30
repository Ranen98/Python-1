import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

'''
框架控件
在屏幕上显示一个矩形区域，一般作为容器控件
'''
frame = tkinter.Frame(win)
frame.pack()

frame_l = tkinter.Frame(win)
tkinter.Label(frame_l, text="左上", bg="black").pack(side=tkinter.BOTTOM)
tkinter.Entry(frame_l, text="左下", bg="blue").pack(side=tkinter.TOP)
frame_l.pack(side=tkinter.LEFT)

#Right
frame_r = tkinter.Frame(win)
tkinter.Text(frame_r, bg="grey").pack(side=tkinter.TOP)
tkinter.Button(frame_r, text="右下", bg="yellow").pack(side=tkinter.BOTTOM)
frame_r.pack(side=tkinter.RIGHT)

win.mainloop()