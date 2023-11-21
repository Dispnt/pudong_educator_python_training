'''
while True:
    year = int(input('请输入年份：'))
    #闰年：能够被4整除且不能被100整除 或者 被400整除
    if year%4 == 0:
        if year%100 != 0:
            print('是闰年')
        elif year%400 == 0:
            print('是闰年')

while True:
    num = input('请输入数字：')
    if num == '0':
        print('编程课')
    elif num == '1':
        print('数学课')
    elif num == '2':
        print('语文课')
    elif num == '3':
        print('英语课')
    else:
        print('没有此编号，请重新输入')

'''
# 算术运算符
# + - * / % // **
#print(11/2)
#print(11//2)
#只要进行了除法运算，就会自动转换为浮点型数据

#比较运算符
# == != > < >= <=

# 逻辑运算符
# 与或非
# and与 两边的条件都必须同时满足，结果才为True
# or或 两边的条件只需要满足一边，结果就为True
# not非 取反
'''
while True:
    year = int(input('请输入年份：'))
    #闰年：能够被4整除且不能被100整除 或者 被400整除
    if year%4 == 0 and year%100 != 0:
        print('是闰年')
    elif year%400 == 0:
        print('是闰年')

while True:
    year = int(input('请输入年份：'))
    #闰年：能够被4整除且不能被100整除 或者 被400整除
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print('是闰年')

#逻辑运算符的优先级：not > and > or
'''
#函数
#封装
#参数：形参（形式参数）、实参（实际参数）
#返回值 return

#普通函数
'''
def a():
    print('我爱我家')
a()
a()
a()
a()

#函数一定要先定义、再调用
def print():
    print('我爱我家')
print()
print
input

import random
print(random.randint(0,100))
'''
#带参函数
#希望一个函数能够实现多样化的功能
#定义函数的时候，写在括号里的就是形参
#调用函数的时候，写在括号里的就是实参
'''
def teacher(name):
    print(name+'是老师')
teacher('xxx')
teacher('jjj')
teacher('qqq')

#默认参数，就是给形参默认的值
def eat(food1,food2='妈妈做的菜'):
    print('中午吃'+food1+food2)
eat('开封菜')
'''
#变量的作用域
#全局变量、局部变量
#全局变量：定义在最外面的变量，可以作用于全局任何位置
#局部变量：定义在函数内，只可以作用于函数内部
'''
a = 2
def num():
    global a
    a = 3
num()
print(a)

#通过global可以使得局部变量全局化
def num():
    global a,b
    a = 10
    b = 20
num()
print(a,b)
'''
#函数的返回值
#return 返回
#函数的返回值可以帮助用户获取函数内的信息
#如何判断一个函数有没有返回值，就是用一个变量尝试去接收这个函数
#如果有值，就是有返回值
#a = input('python')
#print(a)
#print没有返回值，input有返回值

'''
def num():
    a = 10
    return a

n = num()
print(n)
'''
#普通函数
#带参函数
#带返回值的函数
'''
def eat(food1,food2,food3='妈妈做的饭'):
    return food1+food2+food3
a = input('请输入您中午想吃的1：')
b = input('请输入您中午想吃的2：')
n = eat(a,b)
print(n)
'''
#Python面向对象
#类与对象

#类：类相当于图纸
#对象：通过类生产出来的产物
#对象在程序中指的是事物本身
#万物皆对象

#创建一个类
#类名同样需要遵循变量命名的规则，但是首字母必须大写
#类的结构
'''
class Student():
    def __init__(self): #用于储存类的属性
        self.name = '坤坤'
        self.age = 28
        self.id = '100868'
    def study(self): #类中的方法
'''  
#所有的类，都储存了属性和方法
#属性用于描述对象的特征（名词）外观、颜色、年龄、名字
#方法用于描述对象的行为（动词）学习，跑步，吃饭，睡觉
'''
class Student():
    def __init__(self):
        self.name = '坤坤'
        self.age = 28
        self.ids = '100868'
    def study(self):
        return '练习时长两年半'
    def eat(self):
        print('喜欢吃鸡')
    def play(self):
        print('喜欢打篮球')

kunkun = Student()
#类中的属性和方法，需要通过对象点（.）来调用
print('我叫'+kunkun.name+',我今年'+str(kunkun.age)+'岁了,我的编号是'+kunkun.ids)
print(kunkun.study())
kunkun.eat()
kunkun.play()
'''
'''
#带参数的类
class Student():
    def __init__(self,name,age,ids):
        self.name = name
        self.age = age
        self.ids = ids
    def study(self):
        return '练习时长两年半'
    def eat(self):
        print('喜欢吃鸡')
    def play(self):
        print('喜欢打篮球')

kunkun = Student('老八',40,'1111')
#类中的属性和方法，需要通过对象点（.）来调用
print('我叫'+kunkun.name+',我今年'+str(kunkun.age)+'岁了,我的编号是'+kunkun.ids)
print(kunkun.study())
kunkun.eat()
kunkun.play()
'''

