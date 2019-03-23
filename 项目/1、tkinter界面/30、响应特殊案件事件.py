import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")
'''
<Shift-L>   左Shift
<Shift-R>   右Shift
<F5>            
<Return>    回车
<BackSpace> 返回
'''
def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)

e = tkinter.Variable()
# show="*"：密文显示
entry = tkinter.Entry(win, textvariable=e)
# 设置焦点
entry.focus_set()
entry.pack()
entry.bind("<BackSpace>", func)


win.mainloop()