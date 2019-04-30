import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
win.geometry("1024x768+240+20")

'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
就像一个目录
'''
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for i in ["one", "two", "three", "four", "five"]:
    lb.insert(tkinter.END, i)

# 添加元素，ACTIVE是在开始添加，END是在结尾添加。
lb.insert(tkinter.ACTIVE, "zero")
lb.insert(tkinter.END, "six")

# 删除元素，删除索引位置的元素。
# lb.delete(2)
# lb.delete(2,4)

# 选中
lb.select_set(3, 5)
lb.select_set(1)

# 清除选中
lb.select_clear(3, 4)
lb.select_clear(1)

# 获取listbox中的元素个数
print(lb.size())
# 从listbox中取值
# print(lb.get(2, 5))
# print(lb.get(1))

# 返回当前选中的索引
print(lb.curselection())

# 判断一个元素是否被选中
print(lb.select_includes(2))
print(lb.select_includes(5))

win.mainloop()