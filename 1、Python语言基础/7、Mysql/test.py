from ranenSql import RanenSql

db = RanenSql("192.168.43.99", "root", "1010", "ranen")
sql = "delete from bandcard where money>500"
db.delete(sql)
