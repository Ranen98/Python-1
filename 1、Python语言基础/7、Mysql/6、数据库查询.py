import pymysql
'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接受全部返回的行

rowcount：是一个只读属性，返回execute()方法影响的行数
'''
db = pymysql.connect("192.168.43.99", "root", "1010", "ranen")

# 创建一个cursor对象
cursor = db.cursor()
# 查询money大于300的
sql = "select * from bandcard where money>300"
# 执行sql语句
try:
    cursor.execute(sql)
    reslist = cursor.fetchall()
    for row in reslist:
        print(row[0], row[1])
except:
    db.rollback()

# 断开
cursor.close()
db.close()