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

start = time.time()
for fileName in fileList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))
end = time.time()
print("copy成功，耗时%s" %(end-start))
# copy成功，耗时0.05001401901245117
