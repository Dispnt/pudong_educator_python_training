'''
简答题：
一、类中的继承是指什么？
二、发生继承后的父类和子类，有哪些共通点？

编程题：
使用turtle完成以下两种图案的绘制（分别是第一题和第二题）
提示：查看资料中的函数用来进行编程，可以参考菜鸟教程，也可以百度函数的使用方法
'''


# 一、类中的继承是指什么？
'''
指一个类可以从另一个类中继承属性和方法。通过继承，子类可以重用已有的代码，在子类中添加新的属性和方法，或者覆盖父类中已有的属性和方法。
'''


# 二、发生继承后的父类和子类，有哪些共通点？
'''
子类可以继承父类的属性和方法并访问
子类的实例也可以被视为父类的实例。
子类可以通过调用父类中的方法。
'''

# 编程题

## 一

import turtle as t 
t.pensize(3) #画笔粗细
t.speed(0)

def draw_star(size):
    t.pendown() #落笔
    t.pencolor('yellow') #画笔颜色
    t.fillcolor('yellow') #填充颜色
    t.begin_fill() #开始填充
    for i in range(5):
        t.forward(size) #直线
        t.left(144)
    t.end_fill() #结束填充
    t.penup()


def draw_stars(start_x,start_y,heading,star_size):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    draw_star(star_size)


# 红色
t.penup()
t.goto(-400, 300)
t.pendown()
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(600)
    t.right(90)
t.end_fill()



draw_stars(-350,100,0,200) # 大星

draw_stars(-100,200,-30,100) # 小星
draw_stars(-100,50,30,100)
draw_stars(-200,0,0,100)
draw_stars(-300,-30,-30,100)



## 二


t.penup()
t.goto(60, -100)
t.pendown()
t.circle(100)

# 绘制勾
t.penup()
t.goto(70, -30)
t.pendown()
t.setheading(-45)
t.forward(40)
t.setheading(45)
t.forward(90)




t.done()