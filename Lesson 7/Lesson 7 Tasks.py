'''
编程题：
一、店主开了一个便利店，每天早上都要进货，用于白天的售卖。 为了方便管理店里的商品，店主想要设计一个商品类，要求如下：
1. 类的属性为：商品名称 name、数量 count；
2. 类的方法为：
进货的方法 add（能增加商品的数量）
卖货的方法 sell（减少商品的数量）

二、设计一个简单的程序，可以将第一题中进货，卖货的记录存在txt的文档中'

'''
import tkinter as tk

class Commodity:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def add(self, quantity):
        self.count += quantity
        self.add_record(f"进货 {quantity} 个 {self.name}")

    def sell(self, quantity):
        if self.count >= quantity:
            self.count -= quantity
            self.add_record(f"卖货 {quantity} 个 {self.name}")
        else:
            print("商品数量不足，无法售卖。")

    def add_record(self, transaction):
        with open("record.txt", "a", encoding="utf-8") as file:
            file.write(transaction + "\n")



def add_commodity():
    count = int(count_entry.get())
    coke.add(count)
    result_label.config(text=f"成功进货 {count} 个 {coke.name}")

def sell_commodity():
    count = int(count_entry.get())
    coke.sell(count)
    result_label.config(text=f"成功卖出 {count} 个 {coke.name}")

# 创建商品对象
coke = Commodity("可乐", 10)

# 创建GUI窗口
window = tk.Tk()
window.title("商品管理")
window.geometry("300x200")

# 创建输入栏和标签
count_label = tk.Label(window, text="商品数量:")
count_label.pack()
count_entry = tk.Entry(window)
count_entry.pack()

# 创建按钮
add_button = tk.Button(window, text="进货", command=add_commodity)
add_button.pack()

sell_button = tk.Button(window, text="卖货", command=sell_commodity)
sell_button.pack()

# 创建结果标签
result_label = tk.Label(window, text="")
result_label.pack()

# 运行GUI窗口
window.mainloop()





# print(f"现在有 {coke.count} 个 {coke.name}")  # 输出：10

# coke.add(5)
# print(f"现在有 {coke.count} 个 {coke.name}")  # 输出：15

# coke.sell(8)
# print(f"现在有 {coke.count} 个 {coke.name}")  # 输出：7

# coke.sell(10)  # 商品数量不足

# print(f"现在有 {coke.count} 个 {coke.name}")  # 输出：7