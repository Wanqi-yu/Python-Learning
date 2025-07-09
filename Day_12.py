#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/8 15:44
# @Author : wanqi.yu
# @File : Day_12.py
# @Software: PyCharm

'''
类与对象
面向对象:面向对象编程(Object Oriented Programming),简称OOP，是一种程序设计思想,OOP把对象作为程序的基本单元，一个对象包含了数据和
操作数据的函数，将程序中的信息作为对象，每个对象都有自己的属性和行为，在之前的编程中，我们一直使用的都是面向过程编程
面向对象是模拟真实环境，把每个对象具有的属性，和能做的事情，模拟出来，之后再基于对象进行操作
面向过程(Procedure Oriented):面向过程是一种以过程为中心的编程范型，这些都是以正在发生什么为目标进行编程，编程的时候把解决问题的步骤
完整的写出来，然后用函数把这些步骤实现，再一步一步的具体步骤中按顺序调用函数，来完成我们的目的，面向过程注重于如果解决问题，会把问题拆分开

优缺点的比较
面向对象
优点:
结构清晰，程序是模块化和结构化，更加符合人类的思维方式
易扩展，代码重用率高，可继承，可覆盖，可以设计出低耦合的系统
易维护，系统低耦合的特点有利于减少程序的后期维护工作量
缺点:
开销大，当要修改对象内部时，对象的属性不允许外部直接存取，所以要增加许多没有其他意义、只负责读或写的行为。这会为编程工作增加负担，增加运行开销，并且使程序显得臃肿。
性能低，由于面向更高的逻辑抽象层，使得面向对象在实现的时候，不得不做出性能上面的牺牲，计算时间和空间存储大小都开销很大。
面向过程
优点:
流程化使得编程任务明确，在开发之前基本考虑了实现方式和最终结果，具体步骤清楚，便于节点分析。
效率高，面向过程强调代码的短小精悍，善于结合数据结构来开发高效率的程序。
缺点：
需要深入的思考，耗费精力，代码重用性低，扩展能力差，后期维护难度比较大。
'''

'''
类与对象
类:类是一组相关属性和行为的集合 用白话来说，类就是设计图纸
对象:类的实例，由类创造 对象就是类的实际，也就是按照图纸建造出来的产品
类的定义
在Python中可以使用class关键字定义类，关键字后面跟着类名，类名通常是大写字母开头的单词，紧接着是(Object)，表示该类是从那个类继承下来的
通常，没有合适的继承类，就使用object类，这是所有类最终都会继承下来的类，当然如果是新的类，可以不写
下面是语法示例
class Person:
    pass
创建对象
person = Person()
person是Person类的实例对象
对象的方法
写在类中的函数，我们通常称之为(对象的)方法
class Person
    def talk(self)
        print("我是一个对象的方法")
person = Person()
调用对象的属性或方法
person.talk()
对象的属性
class Person(object):
    def __init__(self, name, gender):
        print("当创建对象的时候，会自动执行这个函数")
        self.name = name
        self.gender = gender

    def talk(self):
        print(f"我的名字是：{self.name}，我的性别是：{self.gender}")
__init__ 是一个特殊方法，在创建对象时进行初始化操作，它会自动执行，他的第一个参数永远都是self，代表实例本身。
self是什么
首先，我们要明白self不是一个关键字，在类中，你也可以不用self，你也可以使用其他名字。之所以将其命名为 self，只是程序员之间约定俗成的一种习惯，遵守这个约定，可以使我们编写的代码具有更好的可读性。
那self这个参数在我们的类中指的是什么呢？
self，英文单词意思很明显，表示自己，本身
self在类中表示的是对象本身。在类的内部，通过这个参数访问自己内部的属性和方法。

# 在这个类中，self表示一个类范围内的全局变量，在这个类中任何方法中，都能访问self绑定的变量
# 同时也能访问self绑定的函数
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.talk()  # 访问self绑定的方法 
        self表示的是对象本身，如果不添加self的话，Python会认为只是在给变量赋值，添加self后，

    def talk(self):  # 参数为self，这个函数是对象的方法
        print(self.name)
        
面向对象三大特性
封装
继承
多态
封装:把客观事物封装成抽象的类，隐藏属性和方法的实现细节，仅对外公开接口。
封装可以把计算机中的数据跟操作这些数据的方法组装在一起，把他们封装在一个模块中，也就是一个类中
用户实际使用时不需要知道类是怎么写的，只需要调用类的方法即可

继承:子类可以使用父类的所有功能，并且对这些功能进行扩展。继承的过程，就是从一般到特殊的过程。
继承简单地说就是一种层次模型，这种层次模型能够被重用。层次结构的上层具有通用性，但是下层结构则具有特殊性。
在继承的过程中类则可以从最顶层的部分继承一些方法和变量。类除了可以继承以外同时还能够进行修改或者添加。通过这样的方式能够有效提高工作效率

多态:
多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
多态存在的三个必要条件
要有继承
要有重写；
父类引用指向子类对象。
有的时候，在类中的属性不希望被外部访问。如果想让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以双下划线开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访问
属性访问权限

'''

class Person:
    def __init__(self,name,age):
        '''
        初始化方法，定义对象的属性
        :param name:
        :param age:
        '''
        self.name = name #将函数获取到的参数给到实例
        self.age = age

    def speak(self):
        print(f'我的名字是{self.name},今年{self.age}岁')

#实例化一个对象
person = Person(name='于万琪',age=25)
#调用对象的方法
person.speak()
#访问对象的属性 访问对象的属性方式与调用变量对应的方法相同 对象.属性/方法
print(person.name)
#创建多个实例 实例可以重复创建，根据需求创建任意类型的实例

person_rsh = Person(name='任士辉',age=27)
person_rsh.speak()
print(person.name)

'''
给属性指定默认值
类的每个属性都必须有初始值，哪怕这个值是0或者空字符串，在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的;
如果你对某个属性这样做了，就无需包含为它提供初始值的形参
'''
class Car:
    '''
    汽车类
    '''
    def __init__(self,car_type,year,model):
        self.car_type = car_type
        self.year = year
        self.model = model
        self.odometer_reading = 0

    def read_odometer(self):
        '''
        输出汽车的里程数
        :return:
        '''
        print(f"This car has {self.odometer_reading} + miles on it")
Audi = Car(car_type='Audi',year=1,model='A6')
Audi.read_odometer()
'''
现在当Python创建对象的时候，将像前一个实例一样存储属性，接下来，Python会创建一个名为odometer_reading的属性，并将初始值设置为0
出售时里程表读数为0的汽车并不多，因此我们需要一个修改该属性的值的途径。
'''

'''
修改属性的值
在Python中，修改属性的值有三种方法
1.直接修改
2.通过方法修改
3.通过方法递增(增加特定的值)
下面是代码实例
'''
#直接修改 要修改属性的值，最简单的方法是通过实例直接访问它
Audi.odometer_reading = 23
#调用方法确认值是否变更
Audi.read_odometer()

#使用方法修改 如果在函数中定义一个更新属性的方法，这样就可以无需访问属性，而可以将值传递给一个方法，由它在内部更新

class Dog:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def change(self,age):
        self.age = age
dog_01 = Dog(name='大黄',age=3,color='yellow')
print(f'{dog_01.name}+{dog_01.age}+{dog_01.color}')
dog_01.change(1)
print(f'{dog_01.name}+{dog_01.age}+{dog_01.color}')
'''
这个例子中使用了一个change的方法，带有一个参数aeg，调用这个方法时，会将实例的age属性更新成函数获取到的属性
'''

#通过方法递增

class Old_car:
    def __init__(self,car_type,year,mileage):
        self.car_type = car_type
        self.year = year
        self.mileage = mileage

    def add_odometer(self,miles):
        self.mileage += miles

old_car_01 = Old_car(car_type='Byond',year=1,mileage=300)
print(f'{old_car_01.car_type} {old_car_01.year} {old_car_01.mileage}')

old_car_01.add_odometer(300)

print(f'{old_car_01.car_type} {old_car_01.year} {old_car_01.mileage}')
'''
这个例子与第二个方法类似，但使用的是递增，使用了+=运算符，将接收到的参数加到实例原本的属性上
'''




if __name__ == "__main__":
    run_code = 0
