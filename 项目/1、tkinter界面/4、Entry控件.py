import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

'''
输入控件
用于显示文本内容
'''
# 绑定变量
e = tkinter.Variable()
# show="*"：密文显示
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

e.set("Python")
print(e.get())

win.mainloop()