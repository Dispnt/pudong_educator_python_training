'''
txt = open('1.txt')
a = txt.read()
print(a)
b = txt.readlines()
print(b)
'''
#open函数
#r w a
#r 读取
#w 写入
#a 添加 
#w和a的区别在于，一个会覆盖前面的内容，另一个不会
#txt = open('2.txt')
#print(txt)

#银行系统
#注册、登录（存钱、取钱、查询）

#定义银行类
class Account():
    def __init__(self,name,password,balance,operation):
        self.name = name
        self.password = password
        self.balance = balance
        self.operation = operation
        print(self.name,'账户创建成功')
    #查询功能
    def check(self):
        print('当前余额为：',self.balance)
    #存钱功能
    def save(self,money):
        self.balance += money
        self.operation = '存入'+str(money)
    #取钱功能
    def withdraw(self,money):
        if money < self.balance:
            self.balance -= money
            self.operation = '取出'+str(money)
        else:
            print('您的余额已不足')
    #记录功能
    def record(self):
        #open函数的写入功能，如果找不到文件，会自动创建
        f = open(self.name+'.txt','a',encoding='utf-8')
        f.write(self.name + self.operation + ',余额为,' + str(self.balance) + '\n')
        f.close()

name = input('请输入您的姓名：')
password = input('请输入您的密码：')
try:
    file = open(name+'.txt','r',encoding='utf-8')
except:
    balance = int(input('请输入您的余额：'))
    operation = '创建账户'
else:
    lines = file.readlines()
    line = lines[len(lines)-1]
    lineList = line.split(',')
    balance = int(lineList[2])
    operation = '登录账户'

user = Account(name,password,balance,operation)
while True:
    num = input('请输入您的操作，1、查询；2、存钱；3、取钱')
    if num == '1':
        user.check()
    elif num == '2':
        money = int(input('请输入您想存入的金额：'))
        user.save(money)
        user.record()
    elif num == '3':
        money = int(input('请输入您想取出的金额：'))
        user.withdraw(money)
        user.record()
    else:
        print('请输入正确的指令')













