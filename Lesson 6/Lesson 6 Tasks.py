'''
完成简易计算器
'''

from tkinter import *
#创建窗口
root = Tk()
#设置窗口大小
root.geometry('300x400')
#窗口标题
root.title('简易计算器')

root.resizable(0,0)
#文字
lb1 = Label(root,bg='white',text='先输入两个数，然后按运算符')
lb1.place(x=50,y=50, width=220, height=30)

#输入框
entry1 = Entry(root)
entry1.place(x=50, y=100, width=150, height=30)

entry2 = Entry(root)
entry2.place(x=50, y=150, width=150, height=30)#调整三个框框的位置

#多行文本框    
txt = Text(root)
txt.place(x=50,y=200, width=150,height=130)

#按钮方法
def run1():
    a = entry1.get()
    b = entry2.get()
    c = float(a)+float(b)
    s = a+'+'+b+'='+str(c)
    txt.delete(0.0,'end')  #清空文本框内容
    txt.insert(0.0, s)     #显示运算结果


# 减法按钮方法
def run2():
    a = entry1.get()
    b = entry2.get()
    c = float(a) - float(b)
    s = a + '-' + b + '=' + str(c)
    txt.delete(0.0, 'end')  # 清空文本框内容
    txt.insert(0.0, s)  # 显示运算结果

# 乘法按钮方法
def run3():
    a = entry1.get()
    b = entry2.get()
    c = float(a) * float(b)
    s = a + '*' + b + '=' + str(c)
    txt.delete(0.0, 'end')  # 清空文本框内容
    txt.insert(0.0, s)  # 显示运算结果

# 除法按钮方法
def run4():
    a = entry1.get()
    b = entry2.get()
    if float(b) != 0:
        c = float(a) / float(b)
        s = a + '/' + b + '=' + str(c)
    else:
        s = "除数不能为0"
    txt.delete(0.0, 'end')  # 清空文本框内容
    txt.insert(0.0, s)  # 显示运算结果

#加法按钮
btn1 = Button(root, bg='white',text='+',command=run1)
btn1.place(x=220, y=100, width=50, height=30)


# 减法按钮
btn2 = Button(root, bg='white', text='-', command=run2)
btn2.place(x=220, y=150, width=50, height=30)

# 乘法按钮
btn3 = Button(root, bg='white', text='*', command=run3)
btn3.place(x=220, y=200, width=50, height=30)

# 除法按钮
btn4 = Button(root, bg='white', text='/', command=run4)
btn4.place(x=220, y=250, width=50, height=30)

root.mainloop()