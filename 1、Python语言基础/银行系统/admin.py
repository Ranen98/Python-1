import time
class Admin(object):
    admin = "admin"
    passwd = "0"

    # 欢迎界面
    def printAdminView(self):
        print(" --------------------------------------------------------------------------- ")
        print("丨                                                                         丨")
        print("丨                                                                         丨")
        print("丨                                                                         丨")
        print("丨                          欢迎使用网上银行系统                            丨")
        print("丨                                                                         丨")
        print("丨                                                                         丨")
        print("丨                                                                         丨")
        print(" --------------------------------------------------------------------------- ")

    # 系统界面
    def printFunctionView(self):
        print(" --------------------------------------------------------------------------- ")
        print("丨                          请选择您要执行的操作                            丨")
        print("丨                                                                         丨")
        print("丨                 开户(0)                      查询(1)                    丨")
        print("丨                 取款(2)                      存款(3)                    丨")
        print("丨                 转账(4)                      改密(5)                    丨")
        print("丨                 锁定(6)                      解锁(7)                    丨")
        print("丨                 补卡(8)                      销户(9)                    丨")
        print("丨                                                                         丨")
        print("丨                               退出(EXIT)                                丨")
        print(" --------------------------------------------------------------------------- ")

    # 管理员验证
    def adminCheck(self):
        inputAdmin = input("管理员账号：")
        if inputAdmin != self.admin:
            print("账号错误！")
            return -1
        inputPasswd = input("管理员密码：")
        if inputPasswd != self.passwd:
            print("密码错误！")
            return -1
        print("操作成功，请稍后...")
        time.sleep(2)
        return 0