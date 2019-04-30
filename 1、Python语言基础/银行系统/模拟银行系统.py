from admin import Admin
from atm import ATM
import time
import os       # 操作系统模块
import pickle   # 持久化存储模块

def main():
    # 实例化管理员对象
    admin = Admin()
    # 调用欢迎页面函数
    admin.printAdminView()
    # 管理员验证
    if admin.adminCheck():
        return -1

    # 存储文件的绝对路径
    filepath = os.path.join(os.getcwd(), "allUsers.txt")
    filepath2 = os.path.join(os.getcwd(), "userInfo.txt")

    # 打开文件
    f = open(filepath, "rb")
    f2 = open(filepath2, "rb")

    # 加载文件
    allUsers = pickle.load(f)
    userInfo = pickle.load(f2)

    # 实例化ATM对象
    atm = ATM(allUsers, userInfo)

    # 执行功能
    while True:
        admin.printFunctionView()
        option = input("请选择您要执行的选项：")
        if option == "0":
            atm.openAccount()
        elif option == "1":
            atm.usersInfo()
        elif option == "2":
            atm.withdrawMoney()
        elif option == "3":
            atm.depositMoney()
        elif option == "4":
            atm.transferMoney()
        elif option == "5":
            atm.modifyPasswd()
        elif option == "6":
            atm.lockAccount()
        elif option == "7":
            atm.unkockAcount()
        elif option == "8":
            atm.patchCard()
        elif option == "9":
            atm.cancellation()
        elif option == "EXIT":
            # 退出检查
            if not admin.adminCheck():
                # 写入文件
                with open(filepath, "wb") as f:
                    # 落地存储
                    pickle.dump(atm.allUsers, f)
                with open(filepath2, "wb") as f2:
                    # 落地存储
                    pickle.dump(atm.userInfo, f2)
                return True

        time.sleep(2)


if __name__ == '__main__':
    main()