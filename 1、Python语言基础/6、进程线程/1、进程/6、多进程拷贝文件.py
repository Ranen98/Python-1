from multiprocessing import Pool
import os
import time

def copyFile(path, toPath):
    with open(path, "rb") as f1:
        temp = f1.read()
    with open(toPath, "wb") as f2:
        f2.write(temp)

path = r"C:\学习\TempFile"
toPath = r"C:\学习\ToFile"

# 读取path下的所有文件
fileList = os.listdir(path)

if __name__ == '__main__':
    start = time.time()
    pp = Pool(2)
    for fileName in fileList:
        pp.apply_async(copyFile, args=(os.path.join(path, fileName), os.path.join(toPath, fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("copy成功，耗时：%.2f 秒" % (end-start))

'''
Pool中的参数不是越大越好，我的是两个核心的CPU，默认参数是2，如果写成4，一个核心上就交替执行两个进程。而创建进程和销毁进程
会消耗大量的资源，所以在执行小文件时不需要用多进程，执行特别大的文件时，Pool的参数为核心的2-3倍最好
'''