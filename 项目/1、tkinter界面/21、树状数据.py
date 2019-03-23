import tkinter
from tkinter import ttk
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
# win.geometry("800x600+350+70")

# 创建树
tree = ttk.Treeview(win)
tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 滚动条
scroll = tkinter.Scrollbar()
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scroll.config(command=tree.yview)
tree.config(yscrollcommand=scroll.set)

# 添加一级树枝
treeA1 = tree.insert("", 0, "雅州", text="雅安", values=("treeA1"))
treeA2 = tree.insert("", 1, "攀枝花", text="攀枝花", values=("treeA2"))
treeA3 = tree.insert("", 2, "自贡", text="自贡", values=("treeA3"))

# 添加二级树枝
treeA11 = tree.insert(treeA1, 0, "若水", text="荥经县", values=("treeA11"))
treeA12 = tree.insert(treeA1, 1, "雨城", text="雨城区", values=("treeA12"))
treeA13 = tree.insert(treeA1, 2, "天全", text="天全县", values=("treeA13"))
treeA14 = tree.insert(treeA1, 3, "石棉", text="石棉县", values=("treeA14"))
treeA15 = tree.insert(treeA1, 4, "汉源", text="汉源县", values=("treeA15"))
treeA16 = tree.insert(treeA1, 5, "宝兴", text="宝兴县", values=("treeA16"))
treeA17 = tree.insert(treeA1, 6, "名山", text="名山区", values=("treeA17"))
treeA18 = tree.insert(treeA1, 7, "庐山", text="芦山县", values=("treeA18"))

treeA21 = tree.insert(treeA2, 0, "东区", text="东区", values=("treeA21"))
treeA22 = tree.insert(treeA2, 1, "西区", text="西区", values=("treeA22"))
treeA23 = tree.insert(treeA2, 2, "仁和", text="仁和区", values=("treeA23"))
treeA24 = tree.insert(treeA2, 3, "盐边", text="盐边县", values=("treeA24"))
treeA25 = tree.insert(treeA2, 4, "米易", text="米易县", values=("treeA25"))

treeA31 = tree.insert(treeA3, 0, "自流井", text="自流井区", values=("treeA31"))
treeA32 = tree.insert(treeA3, 1, "贡井", text="贡井区", values=("treeA32"))
treeA33 = tree.insert(treeA3, 2, "大安", text="大安区", values=("treeA33"))
treeA34 = tree.insert(treeA3, 3, "沿滩", text="沿滩区", values=("treeA34"))
treeA35 = tree.insert(treeA3, 4, "荣县", text="荣县", values=("treeA35"))
treeA36 = tree.insert(treeA3, 5, "富顺", text="富顺县", values=("treeA36"))

# 添加三级树枝
treeA111 = tree.insert(treeA11, 0, "宝峰", text="宝峰乡", values=("treeA111"))
treeA112 = tree.insert(treeA11, 1, "严道", text="严道镇", values=("treeA112"))
treeA113 = tree.insert(treeA11, 2, "天凤", text="天凤乡", values=("treeA113"))
treeA114 = tree.insert(treeA11, 3, "荥河", text="荥河乡", values=("treeA114"))

# 添加四级树枝
treeA1111 = tree.insert(treeA111, 0, "田坝村", text="田坝村")
win.mainloop()