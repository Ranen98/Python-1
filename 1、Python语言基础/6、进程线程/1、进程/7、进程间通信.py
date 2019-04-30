from multiprocessing import Process, Queue
import time, os

def pWrite(q):
    print("子进程<%s>启动" % (os.getpid()))
    for i in ["A", "B", "C", "D", "E", "F"]:
        q.put(i)
        time.sleep(1)
    print("子进程<%s>结束" % (os.getpid()))
def pRead(q):
    print("子进程<%s>启动" % (os.getpid()))
    while True:
        v = q.get(True)
        print("value = ",v)


if __name__ == '__main__':
    print("主进程启动")
    q = Queue()
    pw = Process(target=pWrite, args=(q,))
    pr = Process(target=pRead, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # pw进程完成后强制结束pr进程
    pr.terminate()
    print("主进程结束")
