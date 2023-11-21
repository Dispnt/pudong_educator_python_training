#简答题
# 一、Python中的逻辑运算符有哪些，分别作用是什么
"""
Python中的逻辑运算符有三个：and、or和not。
1. and：当两个条件都为真时，返回True；否则返回False。
2. or：当两个条件中至少有一个为真时，返回True；否则返回False。
3. not：对条件进行取反操作，如果条件为真，则返回False；如果条件为假，则返回True。
"""

# 二、请大致描述你对于函数的理解，以及函数的好处
"""
函数是一段可重复使用的代码块，用于执行特定的任务。输入参数，经过计算最后返回输出结果。
函数的好处：
- 代码重用：函数可以被多次调用，避免重复编写相同的代码，提高代码复用性。
- 模块化：函数将代码分割成小块，使得代码更加清晰、易于理解维护。
- 提高效率：函数可以通过传参和返回值实现数据的传递处理，提高了代码执行效率。
"""

# 三、请谈谈类与对象的概念，属性是什么？方法是什么？
"""
类是一种抽象的概念，定义了对象的属性和方法。对象是类的实例化，是类的具体实体。它具有类定义的属性和方法，并可以通过调用方法来执行特定的操作
属性是类或对象的特征状态，用于描述对象的特点。变量用于存储对象的信息。
方法是类或对象的行为操作，用于描述对象的行为。函数用于执行对象的操作
"""


#编程题
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
    
    def teach(self):
        return f"教了{self.experience}年的{self.name}还在上{self.subject}课"
    
    def update_subject(self,subject):
        self.subject = subject
        print(f"{self.name}变成上{self.subject}课了")

x=10
def task1():
    global x
    x=int(input("输入一个变量x:"))
    if x > 0 and x < 10:
        return "x在0和10之间"
    elif x < 0 or x > 10:
        return "x不在0和10之间"
    elif x == 0 or x == 10:
        return "x在0和10之间的边界上"
    

def task2():
    teacher1 = Teacher("虞老师", "数学", 80)
    print(f"教师姓名：{teacher1.name}")
    print(f"教授课程：{teacher1.subject}")
    print(f"教学经验：{teacher1.experience}")
    print(teacher1.teach())
    teacher1.update_subject("信息科技")



print(task1(),end="\n\n\n")
task2()


