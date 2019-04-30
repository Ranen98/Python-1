from card import Card
from user import User
import random
import time

class ATM(object):

    def __init__(self, allUsers, userInfo):
        self.allUsers = allUsers
        self.userInfo = userInfo

    # 验证密码，输入错误次数达到3次，锁定账户！
    def checkPasswd(self, correctPasswd):
        for i in range(3):
            tempPasswd = input("密码：")
            if tempPasswd == correctPasswd:
                return True
            else:
                print("密码错误,请重新输入！")
        return False

    # 获得卡号，用户信息存在文本文档里，也可以存在数据库里（以后实现）
    def getCardID(self):
        cardID_list = random.sample(range(6228484109500000000, 6228484109599999999), 100)
        cardID_list.sort(reverse=True)
        # print(cardID_list)
        cardID = str(cardID_list.pop())
        print("卡号：{}".format(cardID))
        # print(cardID_list)
        # print(type(cardID))
        return cardID

    # 开户
    def openAccount(self):
        print("业务办理中，请稍后...")
        time.sleep(2)
        cardHolder = input("姓名：")
        # 身份证号码
        IDnumber = input("身份证号码：")
        while len(IDnumber) != 18:
            print("请输入正确的身份证号码！")
            IDnumber = input("身份证号码：")
        # 电话号码
        phoneNumber = input("手机号码：")
        while len(phoneNumber) != 11:
            print("请输入正确的手机号码！")
            phoneNumber = input("手机号码：")
        # 预存金额
        prepaidMoney = int(input("预存金额："))
        while prepaidMoney <= 0:
            print("预存金额必须大于0元，请重新输入预存金额！")
            prepaidMoney = int(input("预存金额："))
        # 密码
        cardPasswd = input("设置密码：")
        while len(cardPasswd) != 6:
            print("密码格式有误，请输入6位数字密码！")
            cardPasswd = input("设置密码：")
        if not self.checkPasswd(cardPasswd):
            print("密码错误达到上限，开户失败！")
            return False

        print("业务办理中请稍后...")
        time.sleep(2)
        # 获得卡号
        cardID = self.getCardID()

        # 实例化卡对象和用户对象
        card = Card(cardID, cardPasswd, prepaidMoney)
        user = User(cardHolder, IDnumber, phoneNumber, card)
        # 存入字典，卡号-用户
        self.allUsers[cardID] = user
        # 存入字典，身份证-银行卡
        self.userInfo[IDnumber] = card
        print("业务办理成功，请选择您要执行的操作。")

    # 查询
    def usersInfo(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        print("账户：{0}       余额：{1}".format(user.card.cardID, user.card.cardMoney))

    # 取款
    def withdrawMoney(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        money = int(input("请输入取款金额："))
        if money <= 0 or money > user.card.cardMoney:
            print("您的余额不足或输入金额有误！")
            return False
        user.card.cardMoney -= money
        print("取款成功！")
        # print("卡号：{0}       余额：{1}".format(user.card.cardID, user.card.cardMoney))

    # 存款
    def depositMoney(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        # 进行存款操作
        money = int(input("请输入存款金额："))
        if money <= 0:
            print("输入金额有误！")
            return False
        user.card.cardMoney += money
        # print("卡号：{0}       余额：{1}".format(user.card.cardID, user.card.cardMoney))
        print("存款成功！")

    # 转账
    def transferMoney(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        # 输入收款人卡号，验证是否存在该卡号
        payeeCardID = input("收款人卡号：")
        payee = self.allUsers.get(payeeCardID)
        if not payee:
            print("收款人卡号不存在！")
            return False
        # 如果存在收款人卡号，再输入姓名，核对信息是否正确
        payeeName = input("收款人姓名：")
        if payeeName != payee.cardHolder:
            print("收款人姓名错误，请核对后再进行转账！")
            return False
        transferAmount = int(input("转账金额："))
        # 再次验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        # 验证完成后，进行转账操作，判断用户的余额是否大于转账金额
        if transferAmount <= 0 or transferAmount > user.card.cardMoney:
            print("您的账户余额不足或输入有误！")
            return False

        user.card.cardMoney -= transferAmount
        payee.card.cardMoney += transferAmount

        print("转账成功！")

    # 改密
    def modifyPasswd(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        select = input("是否记得原密码？是（Y/y）；否（N/n)\n")
        if select == "Y" or select == "y":
            print("请输入密码！")
            if not self.checkPasswd(user.card.cardPasswd):
                user.card.cardLock = True
                print("密码输入错误超过3次，此卡已锁定！")
                return False
            # 新密码
            newPasswd = input("新密码：")
            if not self.checkPasswd(newPasswd):
                print("密码错误达到上限，更改失败！")
                return False
            # 将新密码赋值给 user.card.cardPasswd 变量
            user.card.cardPasswd = newPasswd
            print("修改密码成功！")
            return True
        elif select == "N" or select == "n":
            IDnumber = input("请输入您的身份证号码：")
            phoneNumber = input("请输入您的手机号码：")
            if IDnumber != user.IDnumber or phoneNumber != user.phoneNumber:
                print("身份信息验证未通过，操作失败！")
                return False
            newPasswd = input("新密码：")
            if not self.checkPasswd(newPasswd):
                print("密码错误达到上限，更改失败！")
                return False
            # 将新密码赋值给 user.card.cardPasswd 变量
            user.card.cardPasswd = newPasswd
            print("修改密码成功！")
            return True

    # 锁定
    def lockAccount(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        tempCardID = input("请输入您的身份证号码：")
        if tempCardID != user.IDnumber:
            print("身份证号码有误，锁定失败！")
            return False
        # 上锁
        user.card.cardLock = True
        print("此卡已被锁定！")

    # 解锁
    def unkockAcount(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)
        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == False:
            print("此卡未被锁定！")
            return False
        tempCardID = input("身份证号码：")
        if tempCardID != user.IDnumber:
            print("身份证号码有误，解锁失败！")
            return False
        tempCardPasswd = input("银行卡密码：")
        if tempCardPasswd != user.card.cardPasswd:
            print("输入密码错误，解锁失败！")
            return False
        # 解锁
        user.card.cardLock = False
        print("解锁成功！")

    # 补卡
    def patchCard(self):
        IDnumber = input("身份证号码：")
        person = self.userInfo.get(IDnumber)
        # 验证是否存在该用户
        if not person:
            print("该用户不存在")
            return False
        print("补卡成功！")
        # 通过 userInfo 字典中的 key（身份证号码）找到 value（原来的卡号）
        oldCardID = person.cardID
        # 得到新卡号
        newCardID = self.getCardID()
        # 修改 userInfo 里 IDnumber 对应的 value
        self.userInfo[IDnumber] = newCardID
        # 因为字典里的 key 是 hash值，不可修改，这里间接修改其 key。
        self.allUsers[newCardID] = self.allUsers.pop(oldCardID)

    # 销户
    def cancellation(self):
        cardID = input("卡号：")
        user = self.allUsers.get(cardID)

        # 验证是否存在卡号
        if not user:
            print("无此卡信息！")
            return False
        # 验证该卡的锁定状况
        if user.card.cardLock == True:
            print("此卡已被锁定，请解锁后再执行其它操作。")
            return False
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码输入错误超过3次，此卡已锁定！")
            return False
        # 验证身份证信息
        ID = input("身份证号码：")
        if ID != user.IDnumber:
            print("身份信息有误，销户失败！")
            return False
        print("身份信息验证通过，销户后不可恢复。确认销户（Y/y）;返回（N/n）。")
        select = input("")
        if select == "Y" or select == "y":
            # 删除字典里的 key 即销户
            self.allUsers.pop(cardID)
            self.userInfo.pop(ID)
            time.sleep(2)
            print("操作成功")
            return True
        elif select == "N" or select == "y":
            return False