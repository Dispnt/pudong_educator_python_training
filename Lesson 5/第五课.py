#五星红旗
'''
import turtle

t1 = turtle.Turtle()
t1.shape('turtle')
t1.penup()
t1.goto(-150,-100)
t1.pendown()
t1.color('red')
t1.begin_fill()
for i in range(2):
    t1.forward(300)
    t1.left(90)
    t1.forward(200)
    t1.left(90)
t1.end_fill()

turtle.penup() #抬笔
turtle.goto(-130,50) #位置
turtle.pendown() #落笔
turtle.color('yellow') #颜色
turtle.begin_fill() #开始填充
for i in range(5):
    turtle.forward(30) #直线
    turtle.left(144)
turtle.end_fill() #结束填充

turtle.penup() #抬笔
turtle.goto(-85,80) #位置
turtle.pendown() #落笔
turtle.color('yellow') #颜色
turtle.begin_fill() #开始填充
for i in range(5):
    turtle.forward(20) #直线
    turtle.left(144)
turtle.end_fill() #结束填充
'''

#简易算法
#什么叫算法
#算法就是解决问题的办法，并不是只有编程中算法

#算法可以理解为数学里的奥数题，它是可以不断优化的

#递推算法
#找规律
#两种分支：顺推法（斐波那契数列）、逆推法（上楼梯）
#1 1 2 3 5 8 13 21...
#兔子繁殖
#（最开始有一对小兔子，小兔子出生后三个月可以生下另一对小兔子，假设兔子不会死亡）
#1 1 2 3 5 8
#输入一个月份，得出该月份有几只兔子
'''
#列表中最后一个元素的索引值一定是比长度少1的
rab = [1,1]
#假设我要获取第7个月的兔子
#那么我的列表中至少要有6个月的兔子
n = int(input('请输入您要获取第几个月的兔子：'))
for i in range(1,n-1):
    rab.append(rab[i] + rab[i-1])
print(str(n)+'个月的兔子数量是：'+str(rab[len(rab)-1]))
'''
#递归算法
#盗梦空间、恐怖游轮
#自己调用自己

'''
n = 1
def a():
    global n
    n=n+1
    print(n)
    a()
a()

#递归来做兔子数列
def rab(n):
    if n==1 or n==2:
        return 1
    else:
        return rab(n-2) + rab(n-1)

print(rab(7))
'''
#排序算法
#选择排序、冒泡排序
#排序算法顾名思义，一般就发生在数列的排序中，无论是正序还是倒序
#排序算法一定要用在有规律的数列中

#选择排序，就是一个个遍历数列中的数据，然后将选中的数字和目标位置的数字交换
#[3,2,1,4]
#[1,2,3,4]

#冒泡排序
#冒泡排序就是将数列中的数据两两比较，然后进行互换
'''
[13,2,56,100,9,32,1]
# 1
[2,13,56,9,32,1,100]
# 2
[2,13,9,32,1,56,100]
# 3
[2,9,13,1,32,56,100]
# 4
[2,9,1,13,32,56,100]
# 5
[2,1,9,13,32,56,100]
# 6
[1,2,9,13,32,56,100]
'''

'''
#变量互换
a = 1
b = 10
#第一种
c = a
a = b
b = c
#第二种
a,b = b,a
'''
'''
num = [13,2,56,100,9,32,1]
print(num)
for i in range(len(num)-1): #冒泡的轮次
    for i in range(len(num)-1-i): #每轮冒泡的次数
        if num[i] > num[i+1]:
            num[i],num[i+1] = num[i+1],num[i] #数据互换
            
print(num)
'''
#蒙特卡洛算法
#求π的
#求圆周率的算法：割圆法-祖冲之，实验法，蒙特卡洛打点算法
#概率

import turtle,random
R = 250 #半径

t = turtle.Turtle() #创建画笔
t.speed(0)
t.penup()
t.goto(0,-R)
t.pendown()

t.circle(R)

t.penup()
t.goto(-R,-R)
t.pendown()

for i in range(4):
    t.forward(R*2)
    t.left(90)

m = 0 #总数量
n = 0 #红色点数量
while True:
    m += 1
    x = random.randint(-R,R)
    y = random.randint(-R,R)
    t.penup()
    t.goto(x,y)
    t.pendown()
    if t.distance(0,0) <= R:
        n += 1
        t.dot(5,'red')
    else:
        t.dot(5,'black')

    pi = n/m * 4
    print(pi)
























