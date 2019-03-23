import os
from collections import deque

# 队列模拟深度遍历
def getAllDirQU(path):
    queue = deque()
    queue.append(path)
    while len(queue) != 0:
        dirPath = queue.popleft()
        filesList = os.listdir(path)

        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)

            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件：" + fileName)

getAllDirQU("C:\学习\第1章  Python语言基础\9、递归与时间相关模块")

print("--"*50)

# 栈模拟广度遍历
def getAllDirDE(path):
    stack = []
    stack.append(path)

    while len(stack) != 0:
        dirPath = stack.pop()
        fileList = os.listdir(path)

        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                stack.append(fileAbsPath)
            else:
                print("文件：" + fileName)

getAllDirDE("C:\学习\第1章  Python语言基础")