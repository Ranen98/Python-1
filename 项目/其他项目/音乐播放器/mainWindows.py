import tkinter
from tkinter import ttk
import os
from PIL import Image
from PIL import ImageTk
from mutagen.mp3 import MP3
import time

class MainWindows(tkinter.Frame):
    def __init__(self, master):
        self.imgDict = {}
        # 创建Frame容器
        self.frameL = tkinter.Frame(master, width=204, height=300, bg="BlanchedAlmond")
        self.frameLD = tkinter.Frame(master, width=204, height=100, bg="white")
        self.frameRU = tkinter.Frame(master, width=500, height=400, bg="BlanchedAlmond")
        self.frameD = tkinter.Frame(master, width=706, height=100, bg="white")

        self.frameL.grid(row=0, column=0, padx=1, pady=1)
        self.frameLD.grid(row=1, column=0, padx=1, pady=1)
        self.frameRU.grid(row=0, column=1, rowspan=2, padx=1, pady=1, ipady=1)
        self.frameD.grid(row=2, column=0, columnspan=2, padx=1, pady=1)

        # 固定容器大小
        self.frameL.grid_propagate(0)
        self.frameLD.grid_propagate(0)
        self.frameRU.grid_propagate(0)
        self.frameD.grid_propagate(0)

        # 在frameL容器中放置控件
        self.label = tkinter.Label(self.frameL, text="我的音乐", bg="white", width=25, font=("楷体"))
        self.label.grid(sticky=tkinter.W)
        self.button1 = tkinter.Button(self.frameL, text="搜  索", bg="white", width=25, font=("楷体"))
        self.button1.grid(sticky=tkinter.W)
        self.button2 = tkinter.Button(self.frameL, text="本地音乐", bg="white", width=25, font=("楷体"))
        self.button2.grid(sticky=tkinter.W)
        self.button3 = tkinter.Button(self.frameL, text="MV", bg="white", width=25, font=("楷体"))
        self.button3.grid(sticky=tkinter.W)
        self.button4 = tkinter.Button(self.frameL, text="最近播放", bg="white", width=25, font=("楷体"))
        self.button4.grid(sticky=tkinter.W)
        self.button5 = tkinter.Button(self.frameL, text="我的收藏", bg="white", width=25, font=("楷体"))
        self.button5.grid(sticky=tkinter.W)

        # 在frameLD容器中放置控件
        '''
        放一个头像进去，插入图片
        '''
        # 插入头像
        imgPath1 = "C:\学习\临时文件\图片4.png"
        img1 = self.getImgWidget(imgPath1)
        self.label2 = tkinter.Label(self.frameLD, image=img1)
        self.label2.grid(row=0, column=0, pady=5)
        # 插入昵称
        self.label3 = tkinter.Label(self.frameLD, text="远方有海", width=10, font=("楷体", 10), bg="white")
        self.label3.grid(row=1, column=0)

        # 在frameRU容器中放置控件
        '''
        放一个搜索框和一个listbox
        将listbox中的歌曲存放在搜索框中
        '''
        musicName = tkinter.StringVar()
        self.combobox = ttk.Combobox(self.frameRU, width=66, textvariable=musicName)
        self.combobox.grid(padx=7, pady=7)

        self.listbox = tkinter.Listbox(self.frameRU, width=69, height=19)
        self.listbox.grid(padx=6, pady=4, ipady=4)

        # 在feameD容器中放置控件
        '''
        第一列显示歌曲图片信息
        第二三四列显示上一首，暂停，下一首
        第五列显示歌曲进度条
        第六列显示收藏
        第七列显示音量控制
        '''
        self.label4 = tkinter.Label(self.frameD, width=13, height=6, bg="yellow", text="图片显示区域")
        self.label4.grid(row=0, column=0, rowspan=3)
        # 插入上一首，暂停，下一首
        imgPath2 = r"C:\学习\临时文件\1.png"
        img2 = self.getImgWidget(imgPath2)
        self.label5 = tkinter.Label(self.frameD, image=img2)
        self.label5.grid(row=0, column=1, padx=10, rowspan=3)

        imgPath3 = r"C:\学习\临时文件\3.png"
        img3 = self.getImgWidget(imgPath3)
        self.label6 = tkinter.Label(self.frameD, image=img3)
        self.label6.grid(row=0, column=2, rowspan=3)

        imgPath4 = r"C:\学习\临时文件\2.png"
        img4 = self.getImgWidget(imgPath4)
        self.label7 = tkinter.Label(self.frameD, image=img4)
        self.label7.grid(row=0, column=3, padx=10, rowspan=3)

        # 显示歌曲名字和歌手的Label控件
        self.label8 = tkinter.Label(self.frameD, text="未播放音乐", font=("楷体", 8), bg="white")
        self.label8.grid(row=0, column=4, sticky=tkinter.W+tkinter.S, padx=20)

        # 歌曲时长显示
        self.label9 = tkinter.Label(self.frameD, text="0.00", font=("楷体", 6), bg="white")
        self.label9.grid(row=0, column=7, sticky=tkinter.S)

        # 歌曲进度条显示
        # 设置一个画布
        self.canvas = tkinter.Canvas(self.frameD, width=300, height=5, bg="grey")
        self.canvas.grid(row=1, column=4, columnspan=4, padx=20)
        self.out_rec = self.canvas.create_rectangle(5, 5, 105, 25, outline="red", width=1)
        self.fill_rec = self.canvas.create_rectangle(5, 5, 5, 25, outline="red", width=0, fill="red")
        for i in range(300):
            time.sleep(0.1)
            self.progressBar(i, 300)



    # 将图像数据引用保存下来，防止被回收导致只显示一个box
    def getImgWidget(self, filePath):
        if os.path.exists(filePath) and os.path.isfile(filePath):
            if filePath in self.imgDict and self.imgDict[filePath]:
                return self.imgDict[filePath]
            img = Image.open(filePath)
            # print(img.size)
            img = ImageTk.PhotoImage(img)
            self.imgDict[filePath] = img
            return img
        return None

    # 获取音频时长
    def getAudioLength(self, musicPath):
        audioLength = MP3(musicPath)
        return audioLength

    # 歌曲进度条加载
    def progressBar(self, nowProgress, allProgress):
        self.canvas.coords(self.fill_rec, (5, 5, 6 + (nowProgress/allProgress)*300, 25))
        self.frameD.update()