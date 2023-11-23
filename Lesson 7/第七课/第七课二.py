import tkinter
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

btn1 = tkinter.Button(window,text='登录',font=('微软雅黑',20),width=20)
btn1.pack(pady=20)
btn2 = tkinter.Button(window,text='注册',font=('微软雅黑',20),width=20)
btn2.pack(pady=0)
