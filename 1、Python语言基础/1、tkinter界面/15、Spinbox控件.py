import tkinter

def func():
    print(sp.get())
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

'''
数值范围控件
'''
# 绑定变量
v = tkinter.StringVar()
# increment:步长， value=(0, 2, 4, 6) 不与 from_=0, to=20, increment=2 同时使用
sp = tkinter.Spinbox(win, from_=0, to=20, increment=2, textvariable=v, command=func)
sp.pack()

# 设置初始值
v.set(10)

win.mainloop()