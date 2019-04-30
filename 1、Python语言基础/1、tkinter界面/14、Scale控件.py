import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

'''
用户通过拖拽指示器改变变量的值
可以水平，可以竖直
HORIZONTAL   : 水平 
VERTICAL     : 竖直
length       : 水平时表示宽度，竖直时表示高度
tickinterval : 值的间隔
'''

scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=50, length=200)
scale.pack()

# 设置初始值
scale.set(20)

# 取值
def func():
    print(scale.get())
tkinter.Button(win, text="值", command=func).pack()

win.mainloop()