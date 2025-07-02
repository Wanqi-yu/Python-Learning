#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/2 18:58
# @Author : wanqi.yu
# @File : Day_08.py
# @Software: PyCharm
'''
函数和参数
函数是带名字的代码块，用于完成特定的工作
函数的优点:可以重复使用 用来将代码封装，减少代码重复
在Python中分为内置函数和自定义函数两种，内置函数是Python本身包含的一些函数，用于处理信息，数据等
自定义函数是我们在日常编程中，用于重复完成某个功能的时候使用的函数
函数的自定义方法，在Python可以使用def关键字定义一个函数，语法如下
def 函数名称(参数):
    函数描述
    函数代码
    return 返回值
函数名与变量名一样
下面是代码示例
'''
# def Hello():
#     '''
#     显示简单的问候语
#     '''
#     print("Hello World!")
# Hello()
'''
向函数传递信息:在使用函数时，可以给函数传入一些信息和数据，这些数据就被称为参数
函数的参数分为形参和实参
形参是在函数定义时用于接收数据的变量，实参是在调用函数时实际使用的值
下面是代码示例
'''
#定义一个打招呼的函数，函数里有一个参数 name
# def Say_Hello(name):
#     '''
#     打招呼用的函数
#     '''
#     print(f"Hello {name},welcome!")
#定义一个name变量获取用户输入
# name = input('请输入你的名字:')
#调用函数并将name变量作为实参传给函数
# Say_Hello(name)
'''
位置参数与关键字参数
调用函数时，实参按照顺序位置与形参的位置绑定，称为位置参数
也可以在调用函数时写明实参与形参的关系，称作传递关键字参数，这个时候位置信息会被忽略
在同时传递位置参数与关键字参数时，应该先传递位置参数，再传递关键字参数!
下面为代码示例
'''
#1.位置参数
# def BMI(weight,height):
#     '''
#     用于计算BMI值的小程序
#     :param weight:体重,单位(KG)
#     :param height:身高,单位(M)
#     '''
#     BMI = weight / height ** 2
#     print(f'您的BMI值是{BMI}')
# weight = float(input("请输入您的体重,单位(KG)"))
# height = float(input("请输入您的身高,单位(M)"))
#这里的参数是位置参数，当传入的参数位置错误时，会导致函数返回的值错误，为了避免这种类型，更推荐使用关键字函数
# BMI(weight,height)
#2.关键字参数 在下面的调用过程中，我们使用了关键字函数，这样即时填写的参数位置不对，也不会发生返回的值不对的问题
# BMI(height =height,weight = weight)

'''
默认值:编写函数时，可以给每个参数指定默认值，在调用函数中给形参提供实参时，Python将使用指定的实参值，否则将会使用默认值
因此，在给形参指定默认值之后，可以在函数调用时省略掉相应的实参，使用默认值可以简化函数调用，还可以清楚的指出函数的典型用法
下面是代码示例
'''
#在这个函数中，我们给animal_type参数添加了默认值，因此在调用pet函数时，可以省略这个参数的实参
def pet(pet_name,animal_type = 'cat'):
    '''
    输出宠物名字及种类
    :param pet_name: 宠物名称
    :param animal_type: 种类
    '''
    print(f'This is my pet,it\'s name is {pet_name},it is a {animal_type}')
#调用函数，这里只传入了一个实参，因此另一个参数将会使用默认值
pet(pet_name='Candy')
#再次调用，这次传入了两个实参，因此函数将会使用实参的值覆盖默认值并返回结果
pet(pet_name = 'Candy',animal_type = 'Dog')
'''
返回值:函数并非总是显示输出，相反的，它可以接收一些数据，并返回一个或一组值，这个值被称为返回值，在函数中，可以使用return语句将值返回到调用函数的
代码行，返回值让你能够将程序的大部分繁重工作转移到函数中完成，从而简化主程序，同时也可以将返回值作为另一个函数的参数，用于完成复杂的程序
下面是一个代码示例，在上面的函数BMI中，我们使用了print语句输出BMI的值，现在我们将这个函数更新，将BMI值作为返回值，并传给另一个参数
'''
weight = float(input('请输入你的体重,单位(KG)'))
height = float(input("请输入你的身高,单位(M)"))

def BMI(user_weight,user_height):
    '''
    计算并返回BMI值
    :param user_weight: 体重
    :param user_height: 身高
    :return: BMI值
    '''
    BMI = user_weight / (user_height ** 2)
    return BMI

def health(BMI):
    if BMI < 18.5:
        print(f"你的BMI值是{BMI},这表示你体重过瘦")
    elif BMI < 25:
        print(f'你的BMI值是{BMI},这表示你体重正常')
    elif BMI < 30:
        print(f'你的BMI值是{BMI},这表示你体重偏胖')
    else:
        print(f'你的BMI值是{BMI},这表示你的体重肥胖，需要注意一下了')
#这里调用了health函数，并将BMI函数返回的值作为health函数的实参
health(BMI(user_weight=weight,user_height=height))
'''
可选实参:有时候，需要让实参变成可选的，这样在使用函数时只在必要的时候才提供额外信息，可以使用默认值来做到这样的效果
方法如下：将函数的形参设置默认值，并将默认值设置为空，这样就可以在使用时既不影响函数代码，也可以不填写实参
'''

if __name__ == "__main__":
    run_code = 0
