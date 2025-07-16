#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/15 16:34
# @Author : wanqi.yu
# @File : Day_17.py
# @Software: PyCharm
'''
迭代器与生成器
在使用Python的过程中，经常会使用到列表/字典/元组 容器(container) 可迭代对象(iterable) 迭代器(iterator) 生成器(generator)等
容器:容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个迭代获取，可以用 in,not in等关键字判断元素
关键字判断元素是否包含在容器中。通常这类数据结构把所有的元素存储在内存中（也有一些特例，并不是所有的元素都放在内存，
比如迭代器和生成器对象），我们常用的 string、set、list、tuple、dict 都属于容器对象。
尽管大多数容器都提供了某种方式获取其中的每一个元素，但这并不是容器本身提供的能力，而是可迭代对象赋予了容器这种能力，当然并不是所有容器都是可迭代的。
那什么是可迭代对象呢？
可以返回一个迭代器的对象都可以称之为可迭代对象，我们来看一个例子
'''
from debugpy.server.cli import run_code

x = [1,2,3]
a = iter(x)
b = iter(x)
print(next(a))

print(next(b))
'''
这里的 x 是一个可迭代对象，可迭代对象和容器一样是一种通俗的叫法，并不是指某种具体的数据类型，list 是可迭代对象，
dict 也是可迭代对象。a 和 b 是两个独立的迭代器，迭代器内部有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代时获取正确的元素。
迭代器有一种具体的迭代器类型，比如 list_iterator，set_iterator。可迭代对象实现了 __iter__() 方法，该方法返回一个迭代器对象。
在循环遍历自定义容器对象时，会使用python内置函数iter()调用遍历对象的__iter__()获得一个迭代器，
之后再循环对这个迭代器使用next()调用迭代器对象的__next__()。__iter__()只会被调用一次，而__next__()会被调用 n 次。
Iterator（迭代器）
迭代器是一个带状态的对象，它能在你调用next()方法时返回容器中的下一个值，
任何实现了__iter__()和__next__()(Python2.x中实现next())方法的对象都是迭代器，__iter__()返回迭代器自身，
__next__()返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。
迭代器与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）方式返回元素，
这正是它的优点。比如列表中含有一千万个整数，需要占超过100M的内存，而迭代器只需要几十个字节的空间。因为它并没有把所有元素装载到内存中，
而是等到调用next()方法的时候才返回该元素（按需调用 call by need 的方式，本质上 for 循环就是不断地调用迭代器的next()方法）。
itertools模块里的函数返回的都是迭代器对象。为了更直观的感受迭代器内部的执行过程，我们自定义一个迭代器，以斐波那契数列为例
'''

# class Fib(object):
#     def __init__(self, max=0):
#         super(Fib, self).__init__()
#         self.prev = 0
#         self.curr = 1
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.max > 0:
#             self.max -= 1
#             # 当前要返回的元素的值
#             value = self.curr
#             # 下一个要返回的元素的值
#             self.curr += self.prev
#             # 设置下一个元素的上一个元素的值
#             self.prev = value
#             return value
#         else:
#             raise StopIteration
#
#
# if __name__ == '__main__':
#     fib = Fib(10)
#     # 调用next()的过程
#     for n in fib:
#         print(n)
#     # raise StopIteration
#     print(next(fib))

'''
Generator（生成器）
了解了迭代器之后，我们来看下生成器，
普通函数用return返回一个值,还有一种函数用yield返回值，这种函数叫生成器函数。
函数被调用时会返回一个生成器对象。生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅，
生成器:通过列表生成式，我们可以直接创建一个列表，但是，受到内存限制，列表容量肯定是有限的，而且创建一个包含100万个元素的列表，不仅会占用很大的存储
空间，如果我们仅仅访问前面几个元素，那后面绝大多数元素占用的空间就浪费了
以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间，在Python中，这种一边循环一边计算的机制，称为生成器：generator
生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，
而可以使用next()函数和send()函数恢复生成器。
生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，不同于一般的函数会一次性返回包括了所有数值的数组，
生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，
因此生成器看起来像是一个函数，但是表现得却像是迭代器

它不需要像普通迭代器一样实现__iter__()和__next__()方法了，只需要一个yield关键字。生成器一定是迭代器（反之不成立），
因此任何生成器也是一种懒加载的模式生成值。下面来用生成器来实现斐波那契数列的例子
'''
# def fib(max):
#     prev, curr = 0, 1
#     while max > 0:
#         max -= 1
#         yield curr
#         prev, curr = curr, prev + curr
#
#
# fib = fib(6)
# # 调用next()的过程
# for n in fib:
#     print(n)
# # raise StopIteration
# print(next(fib))

'''
上面是生成器函数，再来看下生成器的表达式，生成器表达式是列表推导式的生成器版本，看起来像列表推导式，但是它返回的是一个生成器对象而不是列表对象。
'''
x = (x*x for x in range(10))
y = [x*x for x in range(10)]

import time

def func(n):
    for i in range(0, n):
        # yield相当于return，下一次循环从yield的下一行开始
        arg = yield i
        print('func', arg)

f = func(6)
while True:
    print('main-next:', next(f))
    print('main-send:', f.send(100))
    time.sleep(1)








