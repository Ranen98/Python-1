import sympy
import numpy as np
import math
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import matplotlib.pyplot as plt
import matplotlib

# 随机产生3个参考点坐标
max_width = 100
max_height = 100
cx = max_width * np.random.rand(3)
cy = max_height * np.random.rand(3)
dot1 = plot(cx, cy, 'k^')
plt.title('Trilateration')
# 生成目标节点坐标
mtx = max_width * np.random.rand()
mty = max_height * np.random.rand()

# 计算出目标节点与参考点之间的距离
da = math.sqrt(np.square(mtx - cx[0]) + np.square(mty - cy[0]))
db = math.sqrt(np.square(mtx - cx[1]) + np.square(mty - cy[1]))
dc = math.sqrt(np.square(mtx - cx[2]) + np.square(mty - cy[2]))


# 计算定位坐标，坐标节点通过locx，locy返回
def triposition(xa, ya, da, xb, yb, db, xc, yc, dc):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    # print(type(x))查看x类型
    # print(type(x))
    f1 = (xa - x)**2 + (ya - y)**2 - da**2
    f2 = (xb - x)**2 + (yb - y)**2 - db**2
    f3 = (xc - x)**2 + (yc - y)**2 - dc**2

    i = sympy.solve([f3-f1, f3-f2], [x, y])

    print(i)
    return [i[x], i[y]]


# 解算得到目标点坐标
[locx, locy] = triposition(cx[0], cy[0], da, cx[1], cy[1], db, cx[2], cy[2], dc)
dot2 = plot(locx, locy, 'r*')

# 显示误差
derror = math.sqrt(np.square(locx - mtx) + np.square(locy - mty))
plt.xlabel('derror:' + str(derror))

# 显示距离连线
x = [[locx, cx[0]], [locx, cx[1]], [locx, cx[2]]]
y = [[locy, cy[0]], [locy, cy[1]], [locy, cy[2]]]
for i in range(len(x)):
    plt.plot(x[i], y[i], linestyle='--', color='g')

print(derror)

plt.show()