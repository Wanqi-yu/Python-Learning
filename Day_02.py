#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/24 15:37
# @Author : wanqi.yu
# @File : Day_02.py
# @Software: PyCharm
'''
Day 2:变量和简单数据类型
'''
#定义一个名为 message的变量存储值 Hello World
message = "Hello World!"
#输出变量的值
print(message)

#定义一个字符串类型的变量
name = "Wanqi.yu"
print(name)
'''
字符串:在Python中，被引号引起来的就是字符串，引号可以是单引号，双引号，三引号
'''
#使用upper方法将字符串更改为全大写
print(name.upper())
#使用lower方法将字符串更改为全小写
print(name.lower())
'''
在Python中，还有一个方法，更改为首字母大写.title
'''
print("hello world!".title())

#字符串拼接 在Python中，可以使用加号将两个字符串进行连接
print("Hello "+"World!")

'''
转义字符，当遇到字符串中有部分特殊字符或有多个引号时使用，也可以用来换行或添加空白
'''
#基础转义字符
print('He said:"Let\'s go."')
#字符串换行
print('这是第一行\n这是第二行')
#添加空白
print('这是第一段\t这是第二段')
'''
三引号字符串，三引号的字符串中可以直接换行，不必使用转义字符，也可以用来作为注释
注释:描述代码或变量的作用，在Python中，有两种注释方法，一种是在注释前添加#字符，另一种是使用三引号，三引号包裹起来的内容，如果没有保存在变量中，
或者被函数执行的话，Python会直接忽略
'''

'''
删除空白，当字符串中具有空白，而我们不想要空白的情况下，可以使用去除空白的方法
rstrip lstrip strip
'''
#清除字符串中的空白,全部清除
print("    Hello World!     ".strip())
#清除字符串左边的空白
print("    Hello World!     ".lstrip())
#清除字符串右边的空白
print("    Hello World!     ".rstrip())

'''
数字:在编程中，经常使用数字来记录得分，可视化数据，Python根据数字的不同用法用不同的方式处理他们，
在Python中，基础数字类型有 int 整数，float 浮点数
'''
#整数:正数，负数，0等
num_01 = 1
num_02 = 2
num_03 = -3
num_04 = 0
#在Python中，可以用运算符对数字进行加减乘除运算,加号和减号不变，乘号使用*号，除号使用/符号
print(1+1)
print(1-1)
print(1*1)
print(1/1)

#浮点数:在Python中，带有小数点的数就被称为浮点数
float_01 = 1.1
float_02 = 2.1
float_03 = 1.5
#相同的，浮点数也可以进行加减乘除的运算，并且浮点数可以与整数进行运算，最终算出来的值也是浮点数类型的
print(float_01+float_01)
print(float_02-float_01)
print(float_01*float_02)
print(float_01/float_01)
#浮点数与整数运算
print(float_03 * num_02)

'''
类型转换:在Python中，经常需要使用变量中的值，但当变量是数字类型，而你需要输出字符串类型的信息时，如果直接使用+号进行拼接，Python将会报错
要解决这个问题，可以使用类型转换函数
'''
#将数字转换为字符串,str函数可以将其他类型的值转换为字符串，这样就可以进行字符串拼接
print('Hello,My name is Wanqi.I am ' + str(25) + 'years old.')
#将字符串转换为数字类型，int和float函数可以将其他类型的值转换为数字类型，但必须是可以转换的值，也就是值必须是数字，如 1 30 -9等
#如果是Python这种字符串，转换时将会报错
#将值转换为整数
print(int('23'))
#将值转换为浮点数
print(float('23'))

'''
输入和输出:在编程中，有两个重要的内容，就是输入和输出
输出是在程序中向用户输出一些信息和内容，使用print函数即可
如果要获取用户的输入，该怎么办
我们可以使用input函数，获取用户的输入并保存在变量中，并且可以在input中给用户要输入的内容的提示
'''
#input函数获取的输入默认是字符串的类型，所以如果我们要做计算，需要使用int或float函数更改为数字类型
#简易BMI值计算器
weight = input("请输入您的体重，单位(KG)")
height = input("请输入您的身高，单位(M)")
weight = float(weight)
height= float(height)
#BMI计算公式 体重/身高的平方
BMI = weight/ height ** 2
print("您的BMI值是"+str(BMI))

if __name__ == "__main__":
    run_code = 0
