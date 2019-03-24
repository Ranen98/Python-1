import threading
import time

def run():
    print("子线程<%s>启动" % (threading.current_thread().name))
    time.sleep(2)
    print("这是子线程<%s>" % (threading.current_thread().name))
    time.sleep(2)
    print("子线程<%s>结束" % (threading.current_thread().name))

if __name__ == '__main__':
    print("主线程启动")

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束")