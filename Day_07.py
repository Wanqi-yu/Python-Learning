#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/1 18:45
# @Author : wanqi.yu
# @File : Day_07.py
# @Software: PyCharm
'''
循环及优化技巧
循环语句:简单来说，循环语句就是让代码反复执行某个操作，直到满足某个条件为止
在Python中，有for循环和while循环两种，也可以进行嵌套循环，将for循环嵌套在while循环中
循环的特性
自动遍历序列元素
支持break/continue语句控制
可以和else字句配合使用
可以使用内嵌函数range生成数字序列
'''

'''
for循环:for循环最常见的用法是用于遍历(迭代)序列中的元素，遍历的对象可以是字符串，列表，元组，字典或其他可迭代的对象
语法如下
for variable in sequence
    code block
variable:循环变量，用于存储序列中的每个元素
sequence:要遍历的序列
code block:要循环执行的代码块
序列:
遍历:
使用场景:1 遍历序列或集合的元素 2.当你知道循环多少次
'''
#定义一个整数类型的列表
num = [1,2,3,4,5]
#使用for循环遍历列表，并将遍历出的值存储在变量i中
for i in num:
    #输出i的值
    print(i)

#结合else子句或break语句
#else语句之前已有介绍，所以这里不再另外介绍，break语句用于保持变量稳定，在使用时，break语句会停止当前的循环
#下面是代码示例
for i in num:
    print(i)
    break
#for - else for-else语句在for循环完成之后执行else代码块，语法格式如下
for i in num:
    print(i)
else:
    print('循环正常结束')
#使用函数 range Python中的函数range能够让你轻松的生成一系列的数字，例如，可以像下面这样使用函数range来打印一系列的数字
for i in range(1,5):
    print(i)
#上面的代码好像应该输出数字1-5，但实际不会输出数字5，这是因为差1行为，函数range让Python从指定的第一个值开始数，并在到达第二个值后停止
#同时range还可以用来创建数字列表，要创建数字列表，可以使用list函数将range的结果直接转换为列表
#在使用range时，还可以指定步长，步长是值每个值与下一个值中间间隔的长度，示例如下
num_list = list(range(1,11,2))
for i in num_list:
    print(i)
#在上面这个语句中，从1开始，到11，步长2步，此时列表的输出为 1 3 5 7 9，因为步长没有2，
#for循环搭配continue语句，continue语句使用时会跳过本次循环代码，直接开始下次迭代，下面是示例代码

for i in range(1,11):
    if i == 8:
        continue
    print(i)
#上面这个语句使用for循环搭配range函数和if语句，continue语句来遍历并输出数字列表中的元素，但因为使用了continue，所以元素为8时，剩余的代码块将会跳过

'''
while循环:while在条件为真时重复执行代码块，直到条件变为假为止，语法如下
while condition:
    code block
condition:循环条件，只要为真,循环就会一直执行
下面是基础代码示例
'''
x=10
while x<=0:
    print(x)
    x-=1
#与for循环相似，while循环也可以搭配contiune/else/break语句一起使用,下面是代码示例
while x>1:
    print(f'x的值是{x}')
    x-=1
    if x == 8:
        break
c = 10
while c>=0:
    c -= 1
    if c == 8:
        continue
    else:
        print(f'c的值是{c}')
'''
循环嵌套:Python允许在一个循环体中嵌套另一个循环体，主要应用于多维数据处理，嵌套数据结构遍历等
优化技巧:减少嵌套层数，不要嵌套太多，否则可能会影响性能，下面是一些基础示例
'''
for i in range(1,11):
    for j in range(11):
        print(i+j)
if __name__ == "__main__":
    run_code = 0
