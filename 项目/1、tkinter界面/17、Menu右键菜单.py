import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("800x600+350+70")

# 创建菜单条
menubar = tkinter.Menu(win)

# 菜单
menu = tkinter.Menu(menubar, tearoff=True)
for i in ["撤销", "剪切", "复制", "粘贴", "删除"]:
    menu.add_command(label=i)

menubar.add_cascade(label="功能", menu=menu)
menubar.add_cascade(label="模块")

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
win.bind("<Button-3>", showMenu)

win.mainloop()