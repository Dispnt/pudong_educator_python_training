#什么是库？
#实际上，库也只是一个Python文件
#可以理解为直接使用别人定义好的程序去实现某种功能
#库共分三类：
#标准库  随着Python的下载，自然自然就会一同下载下来的库
#第三方库  就是第三方制作的库，需要自行下载才能使用
#自定义库  就是自己定义的库

#random随机数库
#time时间库
#turtle库

#第三方库如何查询
#win+R → cmd → pip list
#win+R → cmd → where python → Lib

#这节课主要学习pygame以及tkinter这两个库

#Pygame库
#可以用来做游戏
#需要下载pygame库
#win+R → cmd → pip install pygame
'''
import pygame #导入pygame库
import random
pygame.init() #初始化
#对于pygame而言，里面还细分了很多小工具包
#创建窗口,窗口大小默认全屏,窗口的大小一定和背景相同
sc = pygame.display.set_mode((1080,540))
#导入背景
bg = pygame.image.load('bg.jpg')
#粘贴背景，坐标
sc.blit(bg,(0,0))
#如何创建文字，字体，大小
font = pygame.font.Font('msyh.ttf',40)
#RGB色彩模式，三原色
#颜料三原色：红黄蓝
#色光三原色：红绿蓝，数值大小范围均为0~255
snow = font.render('Python真棒',True,(244,150,242))
x = []
y = []
while True:
    sc.blit(bg,(0,0))
    for i in range(100):
        #粘贴文字，坐标
        x.append(random.randint(0,1080))
        y.append(random.randint(0,540))
        sc.blit(snow,(x[i],y[i]))
        x[i] -= 1
        if x[i]<0:
            x[i]=1080
        #自动刷新
    pygame.display.update()
'''
#tkinter库
#简易计算器
#导入tkinter库,获取所有工具
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

#按钮
btn1 = Button(root, bg='white',text='+',command=run1)
btn1.place(x=220, y=100, width=50, height=30)



























