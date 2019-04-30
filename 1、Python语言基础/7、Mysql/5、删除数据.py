import pymysql

# 连接数据库
# 参数一：mysql服务所在的主机IP；参数二：用户名；参数三：密码；参数四：要连接的数据库名称
db = pymysql.connect("192.168.43.99", "root", "1010", "ranen")

# 创建一个cursor对象
cursor = db.cursor()
sql = "delete from bandcard where id=3"
# 执行sql语句
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 断开
cursor.close()
db.close()