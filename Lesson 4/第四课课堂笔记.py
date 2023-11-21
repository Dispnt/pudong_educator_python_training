'''
class Teacher():
    def __init__(self):
        self.name = '刘老师'
        self.age = '30'
    def study(self):
        print('跟学生斗智斗勇')
        return '跟学生斗智斗勇'

teacher = Teacher()
print(teacher.study())
'''
#在同一个类中，属性和方法都是可以自由调用的
#可以在方法中调用属性，也可以在方法中调用方法
#前提是需要加上self
'''
class Student():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self,food):
        print(self.name+'中午要吃'+food)
        self.play()
    def play(self):
        print('跑步减肥')    


stu1 = Student('吴同学',15,'女')
print(stu1.name,stu1.age,stu1.gender)
stu1.eat('开封菜')
'''
#继承，分为父类与子类，也就是说想要发生继承，就需要2个类
#子类可以继承父类所有的属性和方法
#子类可以重写继承来的属性和方法，并且优先级更高
#继承的意义在于帮助我们将大部分同一类型的类变得更加简化

#驼峰命名法
#在程序中，如果有单词是由2个及以上单词组成的
#那么第二个单词开始，首字母需要大写
'''
#父类
class Student():
    def __init__(self):
        self.name = '小明同学'
        self.age = 14
    def sleep(self):
        print('睡觉')

class XiaoMing(Student):
    def sleep(self):
        print('睡觉2小时')

fulei = Student()
fulei.sleep()
xm = XiaoMing()
xm.sleep()
'''


#turtle库
#海龟，海龟画图

#标准库、第三方库、自定义库
#标准库就是python自带的，第三方库就是要下载的，自定义库就是自己创建的
'''
windows+R
cmd
pip list
'''
#想要使用库，必须先导入
#可以把库理解为一种工具包

#import turtle #可以理解为把工具包拿过来了
#from turtle import * #我获取了工具包中的所有工具

# *：通配符，可以简单地理解为全部

#import turtle
#turtle.circle(100) #像素px

#from turtle import *
#circle(100)


'''
#画笔的起点默认是(0,0)
import turtle #导入turtle工具包
import random #导入随机工具包
turtle.shape('turtle') #设置画笔形状

colors = ['pink','yellow','skyblue','lightgreen']
turtle.pensize(3) #画笔粗细
turtle.speed(0) #速度1~10，1最慢，10最快，0表示突破速度
for i in range(60): #循环
    turtle.pencolor(colors[random.randint(0,len(colors)-1)]) #画笔颜色
    turtle.circle(150,steps=2) #画圆，括号内是半径
    turtle.right(360/60) #画圆

import turtle #导入库
turtle.shape('turtle') #画笔形状
turtle.pensize(3) #画笔粗细
turtle.speed(1)
turtle.penup() #抬笔
turtle.goto(-100,-100) #位置
turtle.pendown() #落笔
turtle.pencolor('yellow') #画笔颜色
turtle.fillcolor('yellow') #填充颜色
turtle.begin_fill() #开始填充
for i in range(5):
    turtle.forward(200) #直线
    turtle.left(144)
turtle.end_fill() #结束填充
'''
#斐波那契螺旋线
'''
import turtle
turtle.shape('turtle')
turtle.pensize(3)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.forward(50)

for i in range(4):
    turtle.forward(50)
    turtle.left(90)
    
turtle.pencolor('red')
turtle.pensize(5)
turtle.circle(50,90)
turtle.pencolor('black')
turtle.pensize(3)

def circle1(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.pencolor('red')
    turtle.pensize(5)
    turtle.circle(a,90)
    turtle.pencolor('black')
    turtle.pensize(3)

circle1(100)
circle1(150)
circle1(250)
circle1(400)
'''
