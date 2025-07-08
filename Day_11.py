#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/7 09:38
# @Author : wanqi.yu
# @File : Day_11.py
# @Software: PyCharm
'''
装饰器原理
装饰器:装饰器是Python中一种特殊的函数(高阶操作中也定义为类)，它允许在不锈钢原函数代码的前提下，通过@语法糖动态的为目标函数添加额外的功能，
其本质是接受一个函数做为参数，在内部创建一个新函数来封装原来的函数，并返回新封装函数的闭包结构。
采用“咖啡店售卖一杯咖啡”进行类比，手工萃取好的浓缩咖啡为业务函数（目标函数），糖浆、奶油等配料为装饰器，装饰器机制实现的功能可以类比为店员自动为咖啡添加配料。
示例代码
'''
# 糖浆装饰器
# def syrup_decorator(coffee_maker):
#     def add_syrup():
#         coffee = coffee_maker()
#         return coffee + " +   特制糖浆"
#     return add_syrup
#
# # 奶油装饰器
# def cream_decorator(coffee_maker):
#     def add_cream():
#         coffee = coffee_maker()
#         return coffee + " + ⚪ 打发奶油"
#     return add_cream
#
# # 点单制作咖啡的目标函数
# @cream_decorator
# @syrup_decorator
# def order_coffee():
#     return "  萃取浓缩咖啡"
#
# print(order_coffee())
# 输出：  萃取浓缩咖啡 +   特制糖浆 + ⚪️ 打发奶油
'''
理解关键
@decorator等价于func = decorator(func)。
可保证在目标函数不变的条件下，利用装饰器实现若干功能的模块化拓展。
装饰器可一次定义多出应用，并按目标函数处的堆叠顺序，自下而上执行。
'''

'''
参数化函数装饰器
装饰器本身是一个函数。做为函数如果不能传参，其功能就会大受限制，只能执行固定的逻辑。装饰器的逻辑代码的执行若需要根据不同场景进行调整，
就要写多个装饰器以满足其需要。这显然是不合理的，因此需要带参数的函数装饰器。
通过参数化的函数装饰器设计，我们可以创建出类似“功能模板”的灵活扩展机制。这种模式充分体现了“开闭原则”（对扩展开放，对修改关闭）的精髓。
为理解方便，沿用前述示例场景，就像咖啡店升级成自动调味系统，既能保持核心的咖啡制作流程不变，又能通过参数配置为每位顾客提供个性化的饮品定制服务。
即，顾客可以指定调味品的具体参数：糖浆口味（香草/榛果）、奶油量（正常/双倍）、温度要求（冰/热）。
示例代码
'''
# 糖浆装饰器
def flavored_syrup(syrup_type):
    # 口味配置字典
    flavor_map = {
        "vanilla": " +   香草糖浆",
        "hazelnut": " +   榛果糖浆"
    }

    def syrup_decorator(coffee_maker):
        def add_syrup():
            coffee = coffee_maker()
            return coffee + flavor_map[syrup_type]
        return add_syrup
    return syrup_decorator

# 奶油装饰器
def quantity_cream(cream_type):
    # 份量配置字典
    quant_map = {
        "normal": " + ⚪ 正常奶油",
        "double": " + ⚪ 双倍奶油"
    }

    def cream_decorator(coffee_maker):
        def add_cream():
            coffee = coffee_maker()
            return coffee + quant_map[cream_type]
        return add_cream
    return cream_decorator

# 支持温度控制的进阶装饰器
def temperature_control(ice=False):
    def decorator(func):
        def wrapper():
            drink = func()
            return f"  {drink}" if ice else f"  {drink}"
        return wrapper
    return decorator

# 点单制作咖啡的目标函数
def order_coffee():
    return "  萃取浓缩咖啡"

# 顾客a订单
@quantity_cream("double")
@flavored_syrup("hazelnut")
@temperature_control()
def customer_a():
    return order_coffee()

# 顾客b订单
@quantity_cream("normal")
@flavored_syrup("vanilla")
@temperature_control(True)
def customer_b():
    return order_coffee()

print(customer_a(), customer_b(), sep='\n')
# 输出：
#           萃取浓缩咖啡 +   榛果糖浆 + ⚪ 双倍奶油
#           萃取浓缩咖啡 +   香草糖浆 + ⚪ 正常奶油
if __name__ == "__main__":
    run_code = 0
