import turtle as t
import time

t.pensize(4)    # 笔粗细
t.hideturtle()
t.colormode(255)
t.color((255, 155, 192), "pink")    # 颜色
t.setup(340, 500)   # 画布大小
t.speed(10)     # 画的速度

t.pu()
t.goto(-200, 100)   # 画的开始位置
t.pd()
t.seth(-90)
t.begin_fill()

a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
t.end_fill()

time.sleep(3)

