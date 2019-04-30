import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("记事本")
# 设置大小
win.geometry("800x600+350+70")

# 创建菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print('Python')

# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 在菜单选项中添加内容
for i in ["新建(N)        Ctrl+N", "打开", "保存", "另存为", "页面设置", "打印", "退出"]:
    if i == "页面设置":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=i)
    elif i == "退出":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=i, command=win.quit)
    else:
        menu1.add_command(label=i, command=func)

# 在菜单条上添加菜单选项
menubar.add_cascade(label="文件(F)", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="复制")
menu2.add_command(label="粘贴")
menubar.add_cascade(label="编辑(E)", menu=menu2)

win.mainloop()