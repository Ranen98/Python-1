import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("TKINTER")
# 设置大小
# win.geometry("1024x768+240+20")

'''
文本控件
用于显示多行文本
'''
# 创建滚动条
scroll = tkinter.Scrollbar()
# height：显示的行数
text = tkinter.Text(win, width=50, height=5)
# side：放到窗体的某一侧
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''帝高阳之苗裔兮，朕皇考曰伯庸。 
摄提贞于孟陬兮，惟庚寅吾以降。 
皇览揆余初度兮，肇锡余以嘉名。 
名余曰正则兮，字余曰灵均。 
纷吾既有此内美兮，又重之以修能。 
扈江离与辟芷兮，纫秋兰以为佩。 
汩余若将不及兮，恐年岁之不吾与。 
朝搴阰之木兰兮，夕揽洲之宿莽。 
日月忽其不淹兮，春与秋其代序。 
惟草木之零落兮，恐美人之迟暮。 
不抚壮而弃秽兮，何不改乎此度？ 
乘骐骥以驰骋兮，来吾道夫先路！ 
昔三后之纯粹兮，固众芳之所在。 
杂申椒与菌桂兮，岂惟纫夫蕙茝！ 
彼尧、舜之耿介兮，既遵道而得路。 
何桀纣之昌披兮，夫惟捷径以窘步。 
惟夫党人之偷乐兮，路幽昧以险隘。 
岂余身之殚殃兮，恐皇舆之败绩。 
'''
text.insert(tkinter.INSERT, str)

win.mainloop()