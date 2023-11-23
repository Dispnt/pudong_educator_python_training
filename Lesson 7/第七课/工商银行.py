import tkinter
import tkinter.messagebox

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
        tkinter.messagebox.showinfo('余额','您的账户余额为：'+str(self.balance))
    #存钱功能
    def save(self,money):
        self.balance += money
        self.operation = '存入'+str(money)
        tkinter.messagebox.showinfo('提示','存钱成功')
    #取钱功能
    def withdraw(self,money):
        if money < self.balance:
            self.balance -= money
            self.operation = '取出'+str(money)
            tkinter.messagebox.showinfo('提示','取钱成功')
        else:
            tkinter.messagebox.showinfo('提示','余额不足')
    #记录功能
    def record(self):
        #open函数的写入功能，如果找不到文件，会自动创建
        f = open(self.name+'.txt','a',encoding='utf-8')
        f.write(self.name + ',' +self.password + ',' +self.operation + ',余额为,' + str(self.balance) + '\n')
        f.close()

window = tkinter.Tk()
window.geometry('400x500')
window.title('登录界面')

label1 = tkinter.Label(window,text='工商银行',font=('微软雅黑',40))
label1.pack(pady=30)

label2 = tkinter.Label(window,text='账户名',font=('微软雅黑',20))
label2.pack(pady=0)
entry1 = tkinter.Entry(window,font=('微软雅黑',20))
entry1.pack()

label3 = tkinter.Label(window,text='密码',font=('微软雅黑',20))
label3.pack(pady=0)
entry2 = tkinter.Entry(window,font=('微软雅黑',20))
entry2.pack()

#登录函数
def login():
    name = entry1.get()
    pwd = entry2.get()
    try:
        f1 = open(name+'.txt','r',encoding='utf-8')
    except:
        tkinter.messagebox.showwarning('警告','账户不存在，请先去注册')
    else:
        lines = f1.readlines()
        line = lines[len(lines)-1]
        lineList = line.split(',')
        password1 = lineList[1]

        if password1 == pwd:
            balance1 = int(lineList[4])
            user = Account(name,pwd,balance1,'登录账户')
            user.record()
            tkinter.messagebox.showinfo('提示','登录成功')
            
            #销毁窗口
            window.destroy()
            
            window1 = tkinter.Tk()
            window1.geometry('400x500')
            window1.title('功能页')

            label11 = tkinter.Label(window1,text='工商银行',font=('微软雅黑',40))
            label11.pack(pady=30)

            label22 = tkinter.Label(window1,text='请输入金额',font=('微软雅黑',20))
            label22.pack(pady=10)
            entry11 = tkinter.Entry(window1,font=('微软雅黑',20))
            entry11.pack(pady=10)

            def checkMoney():
                user.check()
                
            def saveMoney():
                money = int(entry11.get())
                user.save(money)
                user.record()
                
            def withdrawMoney():
                money = int(entry11.get())
                user.withdraw(money)
                user.record()
                
            btn11 = tkinter.Button(window1,text='查询余额',font=('微软雅黑',20),width=20,command=checkMoney)
            btn11.pack(pady=10)
            btn22 = tkinter.Button(window1,text='存钱',font=('微软雅黑',20),width=20,command=saveMoney)
            btn22.pack(pady=10)
            btn33 = tkinter.Button(window1,text='取钱',font=('微软雅黑',20),width=20,command=withdrawMoney)
            btn33.pack(pady=10)
            
        else:
            tkinter.messagebox.showerror('错误','密码错误')

#注册函数
def signin():
    name = entry1.get()
    pwd = entry2.get()
    try:
        open(name+'.txt','r',encoding='utf-8')
    except:
        user = Account(name,pwd,0,'创建账户')
        user.record()
        tkinter.messagebox.showinfo('提示','注册成功')
    else:
        tkinter.messagebox.showwarning('警告','账户已存在，请重新输入')

btn1 = tkinter.Button(window,text='登录',font=('微软雅黑',20),width=20,command=login)
btn1.pack(pady=20)
btn2 = tkinter.Button(window,text='注册',font=('微软雅黑',20),width=20,command=signin)
btn2.pack(pady=0)







        
window.mainloop()