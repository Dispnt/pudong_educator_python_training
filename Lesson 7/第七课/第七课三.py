import tkinter
window = tkinter.Tk()
window.geometry('400x500')
window.title('功能页')

label11 = tkinter.Label(window,text='工商银行',font=('微软雅黑',40))
label11.pack(pady=30)

label22 = tkinter.Label(window,text='请输入金额',font=('微软雅黑',20))
label22.pack(pady=10)
entry11 = tkinter.Entry(window,font=('微软雅黑',20))
entry11.pack(pady=10)

btn11 = tkinter.Button(window,text='查询余额',font=('微软雅黑',20),width=20)
btn11.pack(pady=10)
btn22 = tkinter.Button(window,text='存钱',font=('微软雅黑',20),width=20)
btn22.pack(pady=10)
btn33 = tkinter.Button(window,text='取钱',font=('微软雅黑',20),width=20)
btn33.pack(pady=10)
