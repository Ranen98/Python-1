'''
在子进程中修改全局变量对父进程中的全局变量没有影响
在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的num是完全不同的两个变量
'''
from multiprocessing import Process
from time import sleep

num = 0

def process1():
    print("子进程启动")
    global num
    num += 1
    print("num = ", num)
    print("子进程结束")

def process2():
    print("子进程启动")
    global num
    num += 10
    print("num = ", num)
    print("子进程结束")

if __name__ == '__main__':
    print("主进程启动")

    p1 = Process(target=process1)
    p1.start()
    p1.join()

    p2 = Process(target=process2)
    p2.start()
    p2.join()

    print("num = ", num)
    print("主进程结束")