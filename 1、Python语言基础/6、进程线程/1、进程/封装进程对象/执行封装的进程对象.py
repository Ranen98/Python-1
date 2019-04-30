from langProcess import LangProcess

if __name__ == '__main__':
    print("主进程启动")
    p = LangProcess("p")
    # 封装的类里面时 run 方法，p会自动调用此方法
    p.start()
    p.join()
    print("主进程结束")