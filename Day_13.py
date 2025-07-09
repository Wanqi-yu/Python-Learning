#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/9 14:55
# @Author : wanqi.yu
# @File : Day_13.py
# @Software: PyCharm
'''
继承/多态/抽象类
面向对象三大特性
在Day12已记录，这里是更详细的描述和代码实现
'''

'''
封装:将现实世界事物在类中描述为属性和方法，即为封装
也可以说 把客观的事物封装成抽象的类，隐藏属性和方法的实现细节，仅对外公开接口
外部用户在使用时不需要知道方法是怎么实现的，只需要根据需求调用即可
还有一些变量或方法，不需要被外部用户使用，但要被类内的成员使用，这些就被称为私有成员
定义私有成员的方法非常简单
私有变量:变量名以__开头，私有方法也是一样的
'''
#定义汽车类
class Car:
    #初始化函数 有两个参数 类型 和 年限
    def __init__(self,car_type,car_year):
        self.car_type = car_type
        self.car_year = car_year
    #定义了一个私有变量
    __mileage = 0



"""
继承:在Python中，如果本身已经存在的类，在需求更新后，需要分成两个或两个以上的分支，并且两个分支的属性相同，只是方法不同的话，就可以使用继承
子类可以继承父类的属性和方法
在Python中，具有单继承和多继承两种
单继承:仅继承一个父类的属性和方法
多继承:继承多个父类的属性和方法
举例:大学生和小学生都是学生，都具有学号，成绩,名称，学校属性，一开始我们定义了一个学生类型
后面我们发现，他们都需要做作业，但做的作业难度肯定不同，所以我们就可以分为两个类，继承学生类的属性和方法，同时再各自新增一些独立的方法和属性
下面是语法示例
"""

#创建一个Student类
class Student:
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name
#实例化一个Student对象
chen = Student('0001','Chen')
#定义 小学生子类，继承Student类的属性和方法，并添加单独的方法
class EleStudent(Student):
    #在继承时，子类的初始化方法必须有和父类一致的属性
    def __init__(self,ID,name):
        #在继承时必须使用这个方法初始化父类，否则子类将没有ID和name两个属性
        super().__init__(ID,name)
        self.grades = {"语文":0,"数学":0,"英语":0}

    def play(self):
        print('课件出去玩')
#定义大学生类，继承Student类的属性和方法，并添加了单独的方法
class ColStudent(Student):

    def __init__(self,ID,name):
        super().__init__(ID,name)
        self.grades = {"专业课程":0,"高数":0,"英语":0,"毛概":0,"公开课(备注:超级恶心，完全没有意义，不过可以代课)":0}

    def game(self):
        print('下课了，回去打游戏了')

'''
对子类方法的重构，当子类继承了父类的方法后，如果方法不能满足功能需求，我们可以在子类中重新构建一个方法，在Python中，类方法调用时，
会优先调用自己的类中的方法，如果在子类中找不到对应方法，才会去调用父类的方法
下面是代码示例
'''
#定义一个动物类
# class Animal:
#     #初始化
#     def __init__(self,name:str,age:int):
#         self.name = name
#         self.age = age
#     #定义了一个方法
#     def call(self):
#         print(self.name+'会叫')
# #定义一个猫猫类，继承动物类
# class Cat(Animal):
#     #初始化
#    def __init__(self, name, age, gender):
#        #继承父类的属性
#        super(Cat, self).__init__(name,age)
#        #定义了子类单独使用的属性
#        self.gender = gender
#
#    def call(self):
#        print(self.name,'会“喵喵”叫')
# #实例化了一个对象
# c = Cat('喵喵', 2, '男')  #  Cat继承了父类Animal的属性
# #调用对象的方法
# c.call()  # 输出 喵喵 会叫 ，Cat继承了父类Animal的方法

'''
Python中父类与子类的关系
class Animal(object):
   pass

class Cat(Animal):
   pass

A= Animal()
C = Cat()
子类与父类的关系是 “is” 的关系，如上 Cat 继承于 Animal 类，我们可以说：

“A”是 Animal 类的实例，但，“A”不是 Cat 类的实例。

“C”是 Animal 类的实例，“C”也是 Cat 类的实例。

判断对象之间的关系，我们可以通过 isinstance (变量,类型) 来进行判断：
print('"A" IS Animal?', isinstance(A, Animal))
print('"A" IS Cat?', isinstance(A, Cat))
print('"C" IS Animal?', isinstance(C, Animal))
print('"C" IS Cat?', isinstance(C, Cat))
拓展：isinstance() 判断变量类型
函数 isinstance() 不止可以用在我们自定义的类，也可以判断一个变量的类型，如判断数据类型是否为 int、str、list、dict 等。
print(isinstance(100, int))
print(isinstance('100', int))
print(isinstance(100, str))
print(isinstance('100', str))

'''

'''
多态:类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Animal 派生出 Cat和 Dog，并都写了一个 call() 方法，如下示例：

'''

class Animal(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def call(self):
       print(self.name, '会叫')

class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name, age)
       self.sex = sex

   def call(self):
       print(self.name, '会“喵喵”叫')

class Dog(Animal):
   def __init__(self, name, age, sex):
       super(Dog, self).__init__(name, age)
       self.sex = sex
   def call(self):
       print(self.name, '会“汪汪”叫')


def do(all):
   all.call()

A = Animal('小黑',4)
C = Cat('喵喵', 2, '男')
D = Dog('旺财', 5, '女')

for x in (A,C,D):
   do(x)


'''
输出结果:
小黑 会叫
喵喵 会“喵喵”叫
旺财 会“汪汪”叫

这种行为称为多态。也就是说，方法调用将作用在 all 的实际类型上。C 是 Cat 类型，它实际上拥有自己的 call() 方法以及从 Animal 继承的 call 方法
但调用 C .call() 总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。

传递给函数 do(all) 的参数 all 不一定是 Animal 或 Animal 的子类型。任何数据类型的实例都可以，只要它有一个 call() 的方法即可。
其他类不继承于 Animal，具备 call 方法也可以使用 do 函数。这就是动态语言，动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用
'''

'''
Python类继承 注意事项：
在继承中基类的构造方法（__init__()方法）不会被自动调用，它需要在其派生类的构造方法中亲自专门调用。
在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。而在类中调用普通函数时并不需要带上self参数
Python 总是首先查找对应类的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找)

'''
if __name__ == "__main__":
    run_code = 0
























