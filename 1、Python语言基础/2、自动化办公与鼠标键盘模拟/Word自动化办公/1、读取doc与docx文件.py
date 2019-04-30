import win32com
import win32com.client

def readWordFile(path):
    # 调用word功能，处理doc和docx两种功能
    wps = win32com.client.gencache.EnsureDispatch("kwps.application")
    # 打开文件
    doc = wps.Documents.Open(path)
    # 打印出word文本
    for paragraph in doc.Paragraphs:
        text = paragraph.Range.Text
        print(text)
    # 关闭文件
    doc.Close()
    # 退出word
    wps.Quit()


path = r"C:\学习\临时文件\配置清单.doc"
readWordFile(path)