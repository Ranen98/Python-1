'''
import tkinter
from treeWindows import TreeWindows
from infoWindows import InfoWindows
import os

# 创建主窗口
win = 1、tkinter界面.Tk()
# 设置标题
win.title("树状目录层级")
# 设置大小
win.geometry("880x460+350+70")

path = r"C:\\学习"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)

win.mainloop()
'''
import tkinter
import os

from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("sunck")
win.geometry("600x400+200+50")

path = r"C:\软件"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)




win.mainloop()