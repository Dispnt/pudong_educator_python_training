#输入输出 print input
#变量
#表示一个空间

#数据类型
#数字(整数、浮点数)
#字符串(用引号引起来的就是字符串)
'''
a = 10
b = 2
print(a ** b) #幂运算
print(a % b) #取余、取模

a = '你好'
b = 3
print(a+b)
#数据类型的强制转换
int() #转换为整数
str() #转换为字符串

a = '你好'
b = 3
print(a*b)
'''
#列表
#[]
#teachers = ['黄老师','陈老师','李老师']
#              0       1        2
#print(teachers[3])
#索引、下标
#索引用于查找列表中的元素，从0开始的
#索引越界

#列表的操作
#增删改查插
'''
teachers = ['黄老师','陈老师','李老师']
print(teachers)
#增
teachers.append('刘老师') #默认添加在最后
print(teachers)

#删
teachers.pop(1)
#pop()括号中可以填写索引，不填就是默认删除最后的
print(teachers)
teachers.remove('李老师') #删除指定的元素
print(teachers)

#改
teachers[0] = '陈老师'
print(teachers)

#插
teachers.insert(1,'孙老师') #插入指定的元素到指定的位置
print(teachers)
'''
#字典
#{}
#字典中的元素都是成对出现的,key和value，键和值
#student = {'姓名':'xxx','年龄':28,'性别':'女'}
#print(student['姓名'])
#student['姓名'] = '111'
#print(student['姓名'])

#元组，和列表几乎没有区别
#列表中的元素可修改，元组中的元素不可修改
#()
#a = (1)
#print(a)
#a = (1,)
#print(a)

#students = ('陈同学','李同学','王同学')
#print(students)
#students[0] = '孙同学'
#print(students)

#集合,元素是唯一的
#a = {1,1,2}
#print(a)

#type() 检测数据的类型
#a = '1'
#print(type(a))

#数据结构
#顺序、分支、循环
'''
分支结构
1、单分支
2、双分支
3、多分支
'''
#单分支 if...
#判断
#tab
#if 1>2:
#    print('正常')
# 布尔值
#对和错，真和假，True,False
#print(1>2)
#print(2>1)

#双分支 if...else...
#if 1>2:
#    print('正常')
#else:
#    print('不正常')

#多分支 if...elif...else
#input函数的返回值是字符串类型
#多分支语句只会执行最先满足条件的
'''
score = int(input('请输入学生的成绩:'))
if score>=90:
    print('优秀')
elif score>=80:
    print('良好')
elif score>=70:
    print('一般')
elif score>=60:
    print('及格')
else:
    print('不及格')
'''
#循环结构
#for循环
#range(开头,结尾,步长) ，开头默认为0 ，步长默认为1
'''
for i in range(100):
    print('Pyhon'+str(i))
'''
#列表的遍历
#循环的同事，列表本身也在变化
'''
students = ['1','2','3']
for i in students:
    students.remove(i)
print(students)
'''
#while循环
'''
while 条件:
    循环体


for i in range(100):
    print(1)

a=1
while a<=100:
    print(1)
    a+=1
'''
'''
for i in range(9999999999999999999):
    print(1)

a = 1
while True:
    print(a)
    a += 1

#库
import random
num = random.randint(1,1000)
while True:
    n = int(input('请输入您猜的数字：'))
    if n>num:
        print('猜大了')
    elif n<num:
        print('猜小了')
    else:
        print('猜对了')
        break #强行结束循环
'''
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=' ')
    print()















