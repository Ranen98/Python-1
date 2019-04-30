import random
import string
# 随机整数
print(random.randint(1, 10))

# 随机选取0-100的偶数
print(random.randrange(0, 101, 2))

# 随机浮点数
print(random.random()) # 0-1之间的实数
print(random.uniform(1,10))

# 随机字符
print(random.choice("Ranen is a gentelman!"))

# 多个字符中生成指定数量的随机字符
print(random.sample("Ranen is a gentelman!", 10))

# 从a-zA-Z0-9生成指定数量的随机字符，可以作为验证码
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
print(ran_str)

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 在items上打乱顺序，结果返回none
print(random.shuffle(items))
print(items)


res = random.sample(range(1, 101), 100)
res1 = [i*2 for i in res]
print(res1)