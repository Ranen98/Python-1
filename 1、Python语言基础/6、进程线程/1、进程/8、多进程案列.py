from multiprocessing import Pool,Queue
import os, time

'''
需求分析：处理500个文件，分配给5个进程完成，每个进程完成100个
首先要创建5个进程，我们此时需要知道有多少文件 使用（os.Listdir），每个进程平均分配下来在主进程中执行。

问题是如何才能给进程分配多少任务？
'''
def func(name, path, toPath):
    pass

path = r"C:\学习\File"
toPath = r"C:\学习\ToFile"
fileList = os.listdir(path)
fileNum = len(fileList)

if __name__ == '__main__':
    print("父进程启动")
    # 在进程池里面放入多个进程
    pp = Pool(4)
    for i in range(5):
        pp.apply_async(func, args=(i,))
    pp.close()
    pp.join()
    print("父进程结束")