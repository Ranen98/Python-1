import win32api
import win32con
import win32gui
import pygame
import time
import threading

def music():
    while True:
        for i in ["Bad Blood - SORROW.mp3", "陈奕迅 - 几许风雨.mp3", "群星 - 不曾远走.mp3"]:
            filePath = r"C:\学习\临时文件" + "\\" + i
            # 初始化
            pygame.mixer.init()
            # 加载音乐
            track = pygame.mixer.music.load(filePath)
            # 播放
            pygame.mixer.music.play()
            # 播放时长
            time.sleep(10)
            '''
            暂停：pygame.mixer.music.pause()
            '''
            # 停止
            pygame.mixer.music.stop()

def photo(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2 拉伸  0  居中  6  适应  10填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # SPIF_SENDWININICHANGE  立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

t1 = threading.Thread(target=music)
t1.start()
while True:
    for i in ["20190309175454.jpg", "20190309175551.jpg", "20190309175623.jpg"]:
        path = r"C:\学习\临时文件" + "\\" + i
        photo(path)
        time.sleep(5)