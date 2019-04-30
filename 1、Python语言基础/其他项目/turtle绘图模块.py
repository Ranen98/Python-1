import turtle
from datetime import *
class mapping:
    def rectangle():
        # 绘制长方形
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

        turtle.done()
    def cube():
        # 绘制正方体
        turtle.goto(100, 0)
        turtle.goto(100, -100)
        turtle.goto(0, -100)
        turtle.goto(0, 0)
        turtle.goto(45, 45)
        turtle.goto(145, 45)
        turtle.goto(100, 0)
        turtle.up()
        turtle.goto(145, 45)
        turtle.down()
        turtle.goto(145, -45)
        turtle.goto(100, -100)
        turtle.up()
        turtle.goto(45, 45)
        turtle.down()
        turtle.goto(45, -45)
        turtle.goto(0, -100)
        turtle.up()
        turtle.goto(45, -45)
        turtle.down()
        turtle.goto(145, -45)
        turtle.goto(100, -100)

        turtle.done()
    def fivePointStar():
        # 绘制五角星
        turtle.forward(100)
        turtle.right(-216)
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.goto(0, 0)

        turtle.done()
    def theOlympicRings():
        # 绘制奥运五环
        turtle.pensize(10)
        turtle.pencolor("blue")
        turtle.circle(100)

        turtle.up()
        turtle.setx(220)
        turtle.down()

        turtle.pencolor("black")
        turtle.circle(100)

        turtle.up()
        turtle.setx(440)
        turtle.down()

        turtle.pencolor("red")
        turtle.circle(100)

        turtle.up()
        turtle.goto(105, -105)
        turtle.down()

        turtle.pencolor("yellow")
        turtle.circle(100)

        turtle.up()
        turtle.goto(325, -105)
        turtle.down()

        turtle.pencolor("green")
        turtle.circle(100)
        turtle.done()

    def circle():

        turtle.speed(9) # 绘图速度，1-10 越来越快，0 最快
        turtle.circle(50) # 画圆
        turtle.clear()
        turtle.dot(10, "red") # 画圆点
        print(turtle.position()) # 获取海龟当前位置坐标
        print(round(turtle.xcor(), 5))
        turtle.done()

    def sunFllower():
        # 画一个太阳花
        turtle.speed(0)
        turtle.color("red", "yellow")
        turtle.begin_fill()
        for _ in range(50):
            turtle.forward(200)
            turtle.left(170)
        turtle.end_fill()
        turtle.mainloop()

    def clock():
        # 抬起画笔，向前运动一段距离放下
        def Skip(step):
            turtle.penup()
            turtle.forward(step)
            turtle.pendown()
        def mkHand(name, length):
            # 注册Turtle形状，建立表针Turtle
            turtle.reset()
            Skip(-length * 0.1)
            # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
            turtle.begin_poly()
            turtle.forward(length * 1.1)
            # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
            turtle.end_poly()
            # 返回最后记录的多边形。
            handForm = turtle.get_poly()
            turtle.register_shape(name, handForm)
        def Init():
            global secHand, minHand, hurHand, printer
            # 重置Turtle指向北
            turtle.mode("logo")
            # 建立三个表针Turtle并初始化
            mkHand("secHand", 135)
            mkHand("minHand", 125)
            mkHand("hurHand", 90)
            secHand = turtle.Turtle()
            secHand.shape("secHand")
            minHand = turtle.Turtle()
            minHand.shape("minHand")
            hurHand = turtle.Turtle()
            hurHand.shape("hurHand")
            for hand in secHand, minHand, hurHand:
                hand.shapesize(1, 1, 3)
                hand.speed(0)
            # 建立输出文字Turtle
            printer = turtle.Turtle()
            # 隐藏画笔的turtle形状
            printer.hideturtle()
            printer.penup()
        def SetupClock(radius):
            # 建立表的外框
            turtle.reset()
            turtle.pensize(7)
            for i in range(60):
                Skip(radius)
                if i % 5 == 0:
                    turtle.forward(20)
                    Skip(-radius - 20)
                    Skip(radius + 20)
                    if i == 0:
                        turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
                    elif i == 30:
                        Skip(25)
                        turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                        Skip(-25)
                    elif (i == 25 or i == 35):
                        Skip(20)
                        turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                        Skip(-20)
                    else:
                        turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                    Skip(-radius - 20)
                else:
                    turtle.dot(5)
                    Skip(-radius)
                turtle.right(6)
        def Week(t):
            week = ["星期一", "星期二", "星期三",
                    "星期四", "星期五", "星期六", "星期日"]
            return week[t.weekday()]
        def Date(t):
            y = t.year
            m = t.month
            d = t.day
            return "%s %d%d" % (y, m, d)
        def Tick():
            # 绘制表针的动态显示
            t = datetime.today()
            second = t.second + t.microsecond * 0.000001
            minute = t.minute + second / 60.0
            hour = t.hour + minute / 60.0
            secHand.setheading(6 * second)
            minHand.setheading(6 * minute)
            hurHand.setheading(30 * hour)
            turtle.tracer(False)
            printer.forward(65)
            printer.write(Week(t), align="center",
                          font=("Courier", 14, "bold"))
            printer.back(130)
            printer.write(Date(t), align="center",
                          font=("Courier", 14, "bold"))
            printer.home()
            turtle.tracer(True)
            # 100ms后继续调用tick
            turtle.ontimer(Tick, 100)
        def main():
            # 打开/关闭龟动画，并为更新图纸设置延迟。
            turtle.tracer(False)
            Init()
            SetupClock(160)
            turtle.tracer(True)
            Tick()
            turtle.mainloop()
        if __name__ == "__main__":
            main()


exa = mapping()
# mapping.cube()
# mapping.theOlympicRings()
# mapping.rectangle()
# mapping.fivePointStar()
# mapping.circle()
# mapping.sunFllower()
mapping.clock()