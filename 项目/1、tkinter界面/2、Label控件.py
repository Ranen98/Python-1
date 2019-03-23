import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

# 进入消息循环
'''
Label：标签控件可以显示文本
'''
# win：父窗体
# txt：显示的文本信息
# bg：背景色
# fg：字体色
# wraplength：指定text文本中多宽后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北 s南 e东 w西 center居中 还有东北、东南、西南... 默认为center
label = tkinter.Label(win,
                      text="忠诚于自己的选择，不为向任何人证明什么，只为了给自己一个交代。",
                      bg="white",
                      fg="blue",
                      font=("楷体",18),
                      width=30,
                      height=10,
                      wraplength=300,
                      justify="left",
                      anchor="center"
                      )

# 显示出来，挂载。
label.pack()

win.mainloop()