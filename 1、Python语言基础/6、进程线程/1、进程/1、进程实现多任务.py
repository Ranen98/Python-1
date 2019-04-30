'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''
from multiprocessing import Process
from time import sleep
import os

def process1():
    while True:
        print("子进程<{0}>正在执行,其父进程为<{1}>".format(os.getpid(), os.getppid()))
        sleep(1)

def process2():
    while True:
        print("子进程<{0}>正在执行,其父进程为<{1}>".format(os.getpid(), os.getppid()))
        sleep(0.5)

if __name__ == '__main__':
    # os.getpid()获取当前进程id号
    print("主进程<{0}>开始执行".format(os.getpid()))

    p1 = Process(target=process1)
    p1.start()

    p2 = Process(target=process2)
    p2.start()

    while True:
        print("HUANGRUILANG YES！")
        sleep(2)
