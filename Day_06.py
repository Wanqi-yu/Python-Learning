#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/30 15:00
# @Author : wanqi.yu
# @File : Day_06.py
# @Software: PyCharm
'''
条件语句及嵌套
在Python中的条件控制语句是通过一条或多条语句的执行结果(True 或 False) 来决定执行代码的逻辑
每一个if语句的核心都是一个值为true或false的表达式，这种表达式被称为条件测试，Python根据条件测试的值为True或False来决定
是否执行if语句中的代码，如果条件测试的结果为true，Python就执行if语句后面的代码，如果为false，Python就会忽略这些代码
if语句
仅有一个判断条件，如果条件成立，则执行判断语句后带缩进的代码逻辑，否则不执行
缩进:指在代码前添加空格或制表符来实现代码块的层级结构，在Python中，缩进直接决定了代码的逻辑结构和执行顺序
为什么要使用缩进
1.增强代码可读性
2.减少代码符号
3.统一代码风格
下面是代码示例
'''
#定义一个整数变量
num = 10
#使用if语句和比较运算符来判断条件是否成立
if num == 10:
    print('这个变量的值是10')
#大多数条件测试都将一个变量的值同特定值比较，最简单的是检查变量的值是否与特定值相等
#检查相等时不考虑大小写，Python是严格区分大小写的，因此，两个大小写不同的值会被视为不相等
print("Hello World!" == "hello world!")
#如果需要不考虑大小写时，可以使用upper或lower函数来更改值
print("Hello World!".lower() == "hello world!".lower())
#检查是否不相等 要检查是否不相等，可以使用!=运算符，感叹号表示不，下面是示例
if num != 1:
    print('这个变量的值不是1')
'''
条件语句中可以包含各种数学比较，如小于 大于 等于 不等于
注意:在Python中，检查相等的运算符是 == 两个等号相连，因为一个等号会被认为是赋值语句
'''
#检查多个条件:在需要同时检查多个条件的情况下，可以使用关键字 and 或 or
#使用and检查多个条件:使用and检查多个条件时，可以使用and关键字将两个条件合二为一，如果每个测试都通过了，表达式结果将为true，如果有至少一个
#测试没有通过,结果将会为false
if num > 1 and num < 11:
    print('这个值大于1，小于11')

#使用or检查多个条件:当使用or关键字检查多个条件时，如果有至少一个测试通过，结果都会为true
if num > 1 or num > 11:
    print('true')

'''
if-else语句:if-else语句是if语句的扩展，当你需要在通过条件测试时执行第一个操作，没有通过条件测试时执行第二个操作时，可以使用if-else语句
if-else语句与简单的if语句类似，但其中的else语句让你能够指定条件测试未通过时要执行的操作
'''
if num > 18:
    print('恭喜你，你已经成年了，可以进行投票了')
else:
    print('很抱歉，你的年龄不足')

'''
if-elif-else语句
经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else 结构。Python只执行if-elif-else 结构中的一个代码块，它依次检查每个条件测试，直到遇到通过
了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。
在现实世界中，很多情况下需要考虑的情况都超过两个条件，下面是一个例子
现在有一个游乐场
1.4岁以下的孩子免费
2.4-18岁收费10元
18岁(含)以上收15元
如果只使用一条if语句，该如何判断
下面是示例代码
'''
age = int(input('请输入你的年龄:'))
if age < 4:
    print('欢迎进入，你无需付款')
elif age < 18:
    print('欢迎进入，你需要付费10元')
else:
    print('欢迎进入，你需要付费15元')
'''
在这个语句中，if语句检查age变量的值是否小于4岁，如果是的话，Python就打印一条消息，然后跳过剩下的测试
而elif语句是另一个if语句，它仅在第一个if语句未通过时才会运行
而else语句则是在所有条件都未通过时运行
注意:elif语句可以根据需求任意数量的使用
省略else代码块:Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代码块很有用；而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰：
'''

#测试多个条件 if-elif-else结构功能很强，但只适合于只有一个条件满足的情况下，当我们必须检查所有条件时，就需要使用多个if语句
#下面是一个示例
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


'''
操作运算符
== 等于   判断两边的值是否相等
!= 不等于  判断两边的值是否不相等
> 大于    判断左边的值是否大于右边的值
< 小于    判断左边的值是否小于右边的值
>= 大于等于 判断左边的值是否大于等于右边的值
<= 小于等于 判断左边的值是否小于等于右边的值
!> 不大于 判断左边的值是否不大于右边的值
!< 不小于 判断左边的值是否不小于右边的值
in/not in 成员运算符，判断字符或元素是否在字符串或列表中
is/not is
逻辑运算符
and 与 
or 或
not 非
'''
if __name__ == "__main__":
    run_code = 0
