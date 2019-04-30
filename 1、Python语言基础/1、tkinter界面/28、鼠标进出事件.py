import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")
'''
Enter：当鼠标光标进入控件时触发事件
Leave：当鼠标光标离开控件时触发事件
'''
def func(event):
    print("鼠标光标进入了控件！")

def func1(event1):
    print("鼠标光标离开了控件！")

label = tkinter.Label(win, text="Button", bg="grey")
label.place(x=200, y=200)
label.bind("<Enter>", func)
label.bind("<Leave>", func1)

win.mainloop()