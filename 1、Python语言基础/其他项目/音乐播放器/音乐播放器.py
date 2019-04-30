import tkinter
from mainWindows import MainWindows

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Python Music")
# 设置大小
# win.geometry("800x600+350+70")

path = r""
mainWin = MainWindows(win)


win.mainloop()