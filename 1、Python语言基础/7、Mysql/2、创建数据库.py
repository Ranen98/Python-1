import pymysql

db = pymysql.connect("192.168.43.99", "root", "1010", "ranen")
cursor = db.cursor()

# 检查表是否存在，如果存在则删除
cursor.execute("drop table if exists bandcard")
# 建表
sql = "create table bandcard(id int auto_increment primary key, money int not null)"
cursor.execute(sql)

# 断开
cursor.close()
db.close()