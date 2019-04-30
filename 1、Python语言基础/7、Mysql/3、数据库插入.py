import pymysql

# 连接数据库
# 参数一：mysql服务所在的主机IP；参数二：用户名；参数三：密码；参数四：要连接的数据库名称
db = pymysql.connect("192.168.43.99", "root", "1010", "ranen")

# 创建一个cursor对象
cursor = db.cursor()
sql = "insert into bandcard values(0, 200),(0, 300),(0, 400),(0, 600),(0, 700),(0, 800),(0, 900)"
# 执行sql语句
try:
    cursor.execute(sql)
    # 提交
    db.commit()
except:
    # 如果提交失败，回滚到上一次数据
    db.rollback()

# 断开
cursor.close()
db.close()