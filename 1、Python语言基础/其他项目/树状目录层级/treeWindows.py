'''
import tkinter
from tkinter import ttk
import os

# 一个框架，控件都写在这个框架里
class TreeWindows(1、tkinter界面.Frame):
    def __init__(self, master, path, otherWin):
        frame = 1、tkinter界面.Frame(master)
        frame.grid(row=0, column=0, padx=15, pady=15)

        self.otherWin = otherWin

        self.tree = ttk.Treeview(frame, height=20)
        self.tree.pack(side=1、tkinter界面.LEFT, fill=1、tkinter界面.Y)

        tempPath = self.getLastPath(path)
        root = self.tree.insert("", "end", text=tempPath, open=True, values=(path))
        # print(path)
        # 加载树枝
        self.loadTree(root, path)

        # 添加滚动条
        self.sc = 1、tkinter界面.Scrollbar(frame)
        self.pack(side=1、tkinter界面.RIGHT, fill=1、tkinter界面.Y)

        self.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sc.set)

        # 绑定鼠标点击事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    # 事件
    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)["values"][0]
            print(apath)


    # 用递归把树枝全部加载上去
    def loadTree(self, parentName, parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)
            # 插入树枝
            tree_ = self.tree.insert(parentName, "end", text=self.getLastPath(absPath), open=True, values=(absPath))
            if os.path.isdir(absPath):
                self.loadTree(tree_, absPath)

    # 得到路径的最后一个名称
    def getLastPath(self, path):
        pathList = os.path.split(path)
        lastPath = pathList[-1]
        return lastPath
'''

import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        self.otherWin = otherWin

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        #print(os.path.splitext(path))
        tempPath = self.getLastPath(path)
        root = self.tree.insert("","end",text=tempPath,open=True,values=(path))
        self.loadTree(root, path)

        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self,event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)["values"]
            print(apath)



    def loadTree(self, parent, parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)
            #插入树枝
            treey = self.tree.insert(parent, "end", text=self.getLastPath(absPath), values=(absPath))
            #判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath)


    def getLastPath(self, path):
        pathList = os.path.split(path)
        return pathList[-1]