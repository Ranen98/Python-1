import win32com
import win32com.client
import os

def makeWordFile(path, name):
    wps = win32com.client.gencache.EnsureDispatch("kwps.application")
    # 让文档可见
    wps.Visible = True
    # 创建文档
    doc = wps.Documents.Add()
    # 写内容,从头开始写
    r = doc.Range(0, 0)
    r.InsertAfter(name + "您好:\n")
    r.InsertAfter("   我是你爸爸!\n")

    # 存储文件
    doc.SaveAs(path)
    # 关闭文件
    doc.Close()
    # 退出word
    wps.Quit()

names = ["张三", "李四", "王五"]
for name in names:
    path = os.path.join(os.getcwd(), name)
    makeWordFile(path, name)