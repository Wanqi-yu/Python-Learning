#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/7/14 16:18
# @Author: 23955
# @File: Day_16.py
# @Software: PyCharm
'''
Python-上下文管理器
在学习文件处理时，有两种方法
1.先使用open函数，再使用close函数关闭
2.使用with方法打开，只要退出with块。不管是异常导致的退出，还是正常退出，文件都会被关闭
with后面跟着的就是上下文管理器
里面定义好了进入和退出with块的行为，所以才能自动打开和关闭文件
with可以用在打开文件或数据库链接灯行为
但当我们需要手动编写上下文管理器时，就需要按照一些定义好的规则来创建对应的类或者函数
在Python的定义中，要实现一个上下文管理器的类，只需要定义好进入和退出with块的行为
并将代码写到 __enter__和__exit__两个方法中
enter定义的是进入with块的行为，exit定义退出的行为
以下是语法示例
class MyOpne:
    def __init__(self,file_name):
        self.file_name = file_name

    def __enter__(self):
        print('进入with块')
        '实际处理代码'
        return self.file_path
        这个返回的值会绑定as后的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with块")
        '实际代码'

exit 除了self还有另外的三个参数，分别表示发生异常时的异常类型，异常的值，以及traceback
下面是代码示例
'''


class MyOpne:
    def __init__(self,file_name):
        self.file_name = file_name

    def __enter__(self):
        print("进入with块")
        return self.file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with块")

with MyOpne('test.txt') as f:
    print(f"The value is {f}")
'''
如果with块里面出现了异常，中断了with的执行，依然会执行exit里面的内容
'''

# with MyOpne('test.txt') as f:
#     raise ValueError('<UNK>')
#     print(f"The value is {f}")

'''
在exit中，有三个参数，所以我们可以在exit中定义一些处理异常的代码,来防止异常导致代码中断,如果希望处理完异常之后，代码继续执行，就需要在
exit中，返回一个True
'''

class MyFile:
    def __init__(self,file_name):
        self.file_name = file_name
    def __enter__(self):
        print("进入with块")
        return self.file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with块")
        if exc_type is ValueError:
            print("捕获到了一个ValueError")
        return True

with MyFile('test.txt') as f:
    raise ValueError("<UNK>ValueError")
    print(f"The value is {f}")











if __name__ == "__main__":
    run_code = 0
