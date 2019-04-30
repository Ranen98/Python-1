import threading

num = 0
def run(n):
    global num
    for i in range(10000000):
        num = num + n
        num = num - n
    print(num)

if __name__ == '__main__':
    print("主线程启动")

    t1 = threading.Thread(target=run, args=(4,))
    t2 = threading.Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束")