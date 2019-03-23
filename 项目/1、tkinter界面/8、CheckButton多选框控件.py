import tkinter

def func():
    txt = ""
    if hobby1.get() == True:
        txt += "金钱\n"
    if hobby2.get() == True:
        txt += "权力\n"
    if hobby3.get() == True:
        txt += "美女\n"

    # 清楚txt中的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, txt)

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# 绑定变量
hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="金钱", variable=hobby1, command=func)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="权力", variable=hobby2, command=func)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="美女", variable=hobby3, command=func)
check3.pack()

text = tkinter.Text(win, width=30, height=5)
text.pack()


win.mainloop()