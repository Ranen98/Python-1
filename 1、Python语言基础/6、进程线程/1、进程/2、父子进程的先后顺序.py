from multiprocessing import Process
from time import sleep

def process1():
    print("子进程启动")
    sleep(3)
    print("子进程结束")

if __name__ == '__main__':
    print("主进程启动")

    p1 = Process(target=process1)
    p1.start()
    p1.join()

    print("主进程结束")

'''
主进程的开始与结束不受子进程的影响，但是一般我们在主进程里面添加子进程时，我们会等待子进程结束后再结束主进程
'''