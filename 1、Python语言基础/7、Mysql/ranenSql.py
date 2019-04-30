import pymysql

class RanenSql():
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    # 链接
    def connet(self):
       self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName)
       self.cursor = self.db.cursor()
    # 关闭
    def close(self):
        self.cursor.close()
        self.db.close()

    '''
    查询模块的两种方法
    1、fetchone
    2、fetchall
    '''
    def get_one(self, sql):
        res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("No results were found")
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("No results were found")
        return res

    '''
    下面三个方法功能一样只是sql语句不一样
    所以另写一个方法，分别用这三个方法去调用此方法
    '''
    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    '''
    增、删、改的实现
    '''
    def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("Invalid operation")
            self.db.rollback()
        return count