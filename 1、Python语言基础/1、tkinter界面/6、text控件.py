import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

'''
文本控件
用于显示多行文本
'''
# height：显示的行数
text = tkinter.Text(win, width=30, height=4)
text.pack()
str = "忠诚于自己的选择，不为向任何人证明什么，只为了给自己一个交代。"
text.insert(tkinter.INSERT, str)

win.mainloop()