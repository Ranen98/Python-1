import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")
'''
<Button-1>鼠标左键
<Button-2>鼠标中键
<Button-3>鼠标右键
<Double-Button-1>鼠标左键双击
<Double-Button-2>鼠标中键双击
<Double-Button-3>鼠标右键双击
<Triple-Button-1>鼠标左键三击
<Triple-Button-2>鼠标中键三击
<Triple-Button-3>鼠标右键三击

所有小控件都能绑定事件
'''
def func(event):
    print(event.x, event.y)

button = tkinter.Button(win, text="Button", bg="grey")
button.place(x=200, y=200)

# 鼠标事件
button.bind("<Button-1>", func)

win.mainloop()