import threading

# 上了锁后，程序执行效率就会变低，但是在没有上锁的地方仍然是多线程执行
lock = threading.Lock()
num = 0
def run(n):
    global num
    for i in range(1000000):
# -------------------------------------------
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            # 一定要释放锁，不然会造成死锁
            lock.release()
    print(num)
# -------------------------------------------
    '''
    # 此段代码跟上面的效果是一样的
    with lock:
        num = num + n
        num = num - n
    print(num)
    '''
if __name__ == '__main__':
    print("主线程启动")

    t1 = threading.Thread(target=run, args=(4,))
    t2 = threading.Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束")