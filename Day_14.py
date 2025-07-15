#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/10 18:31
# @Author : wanqi.yu
# @File : Day_14.py
# @Software: PyCharm
'''
魔术方法(Magic Methods):
魔术方法是Pytgon中一种特殊的方法，它们以双下滑线开头和结尾 如__init__,这些方法会在特定的场景或操作下自动调用，让我们能够自定义类的行为
使其更加灵活和强大
为什么要学习魔术方法
1.使自定义类支持Python的内置操作 如 + - * /运算符
2.自定义对象的表现形式:如打印对象时的输出内容
3.实现容器类型的行为:如列表或字典等
4.控制属性访问:如获取、设置、删除属性时的行为
'''

'''
常用魔术方法
算数运算符方法
字符串表示方法
容器类型方法
'''

'''
算数运算符方法
相关代码示例
'''

class MyNumber:
    def __init__(self, value):
        self.value = value

    # 加法运算
    def __add__(self, other):
        return self.value + other.value

    # 幂运算
    def __pow__(self, other):
        other = float(other)
        if not isinstance(other, (int, float)):
            raise ValueError("must be number type：integer、float")
        return self.value ** other

    # 普通方法
    def mypow(self, n):
        return self.value ** n

    # 相等比较
    def __eq__(self, other):
        return self.value == other.value


# 使用示例
num1 = MyNumber(100)
num2 = MyNumber(200)
print(num1 + num2)  # 300
print(num1 ** 2)  # 10000
print(num1 == num2)  # False


'''
字符串表示相关方法
示例代码
'''


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 定义对象的字符串表示（print时调用）
    def __str__(self):
        return f"我是{self.name},今年{self.age}岁了,性别{self.gender}"

    # 定义对象的长度
    def __len__(self):
        return 3

    # 定义加法操作
    def __add__(self, str1):
        return self.__str__() + str1


# 使用示例
stu1 = Student("小米", 20, "Male")
print(stu1)  # 我是小米,今年20岁了,性别Male
print(len(stu1))  # 3
print(stu1 + " abc")  # 我是小米,今年20岁了,性别Male abc

'''
3.容器类型相关方法
代码示例
'''


class MyList:
    def __init__(self, value):
        self.value = value

    # 定义长度
    def __len__(self):
        return len(self.value)

    # 定义索引访问
    def __getitem__(self, index):
        index = int(index)
        # 防止索引越界
        return self.value[index if index < self.__len__() else self.__len__() - 1]

    # 定义索引赋值
    def __setitem__(self, index, value):
        self.value[index] = value


# 使用示例
list1 = MyList([1, 2, 3, 4, 5, 6])
print(len(list1))  # 6
list1[2] = 3000  # 修改索引为2的值
print(list1[2])  # 3000
print(list1[10])  # 6 (防止索引越界)

'''
常见魔术方法分类
1. 初始化与构造
__new__(cls, [...]): 创建实例时调用

__init__(self, [...]): 初始化实例时调用

2. 字符串表示
__str__(self): 定义对象的字符串表示（print时调用）

__repr__(self): 定义对象的官方字符串表示

3. 算术运算符
__add__(self, other): 加法 +

__sub__(self, other): 减法 -

__mul__(self, other): 乘法 *

__truediv__(self, other): 除法 /

__pow__(self, other): 幂运算 **

4. 比较运算符
__eq__(self, other): 等于 ==

__ne__(self, other): 不等于 !=

__lt__(self, other): 小于 <

__gt__(self, other): 大于 >

5. 容器类型
__len__(self): 返回长度（len()调用）

__getitem__(self, key): 获取元素（obj[key]调用）

__setitem__(self, key, value): 设置元素（obj[key]=value调用）

__contains__(self, item): 检查是否包含（in操作调用）

'''
if __name__ == "__main__":
    run_code = 0
