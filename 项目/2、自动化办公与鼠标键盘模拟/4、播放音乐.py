import pygame
import time

filePath = r"C:\Users\Farusea\Music\Bad Blood - SORROW.mp3"

# 初始化
pygame.mixer.init()
# 加载音乐
track = pygame.mixer.music.load(filePath)
# 播放
pygame.mixer.music.play()
# 播放时长
time.sleep(30)
'''
暂停：pygame.mixer.music.pause()
'''
# 停止
pygame.mixer.music.stop()
