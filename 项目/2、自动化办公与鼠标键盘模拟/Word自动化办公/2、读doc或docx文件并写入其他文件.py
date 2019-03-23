import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    wps = win32com.client.gencache.EnsureDispatch("kwps.application")
    doc = wps.Documents.Open(path)

    # 将word的数据保存到另一个文件
    doc.SaveAs(toPath, 2)# 2表示为txt文件

    doc.Close()
    wps.Quit()

path = r"C:\学习\临时文件\配置清单.doc"
toPath = r"C:\学习\临时文件\配置清单.txt"
readWordFileToOtherFile(path, toPath)