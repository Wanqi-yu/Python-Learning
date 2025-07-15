#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/11 17:34
# @Author : wanqi.yu
# @File : Day_15.py
# @Software: PyCharm
'''
单元测试
单元测试(又被称为模块测试 Unit Testing)是针对程序模块(软件的最小设计单元)来进行正确性检验的测试工作，程序单元是应用的最小的可测试部件
在面向过程编程中，一个单元就是单个程序，函数，或方法等，面向对象编程中，一般是单个类，或类的方法
为什么要进行单元测试
进行测试的原因主要有以下几点
1.保证代码的正确性，确保代码升级或重构后不会引发新问题
2.提高代码设计能力
3.确保代码的质量
在编程中有一个重要的概念
测试驱动开发(TDD:Test Driven Development)
我们日常编写代码的过程中，一般是由开发者自行调试，但当代码上线后，使用的用户越来越多，我们就会发现，很多在设计时没有想象到的场景会发生
导致出现各种新问题，所以测试可以增加代码的安全性，也可以发现很多在开发过程中想不到的场景
比如对函数abs()，可以编写出以下测试用例
输入正数，比如1、1.2、0.99，期待返回值与输入相同；
输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
输入0，期待返回0；
输入非数值类型，比如None、[]、{}，期待抛出TypeError。
把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。

单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，
如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
Python相关的测试库
unittest Python的内置模块
nose
pytest
mock
目前主要学习使用unittest模块
unittest模块简介
Python的unittest模块是Python标准库中用于进行单元测试的模块，它提供了一套丰富的API供我们编写和运行单元测试。unittest模块的使用主要包括三个步骤
1.导入模块
2.定义一个继承自untitest.TestCase的测试类，然后在类中定义测试方法
3.运行测试
以下是代码示例
'''
#定义一个基础除法函数
def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y
import unittest
#定义一个测试类
class TestDivide(unittest.TestCase):
    #注意点:unittest类中单元测试的要求如下
    '''
    1.测试类必须以Test开头或Test结尾
    2.测试函数必须以test开头或结尾，且类中不能有构造函数
    '''
    def test_divide(self):
        #检查调用函数后返回的值是否和预设的值相同
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-4, 2), -2)
        #检测调用函数后捕获的错误
        self.assertRaises(ValueError, divide, 4, 0)

'''
测试用例、测试套件、测试运行器的概念和创建
在unittest模块中，有以下几个重要概念
测试用例（Test Case）：一个测试用例就是一个完整的测试流程，包括测试前的准备环节、执行测试动作和测试后的清扫环节。在unittest模块中，
一个测试用例就是一个unittest.TestCase的实例。
测试套件（Test Suite）：测试套件是一系列的测试用例或测试套件的集合。我们可以使用unittest.TestSuite类来创建测试套件。
测试运行器（Test Runner）：测试运行器是用来执行和控制测试的。我们可以使用unittest.TextTestRunner类来创建一个简单的文本测试运行器。
'''

import unittest

class TestMath(unittest.TestCase):
    # 测试用例
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(3 - 2, 1)

# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(TestMath('test_add'))
suite.addTest(TestMath('test_subtract'))

# 创建测试运行器
runner = unittest.TextTestRunner()
runner.run(suite)

'''
使用setUp和tearDown处理测试前后的准备和清理工作
编写单元测试时，我们经常需要在每个测试方法执行前后做一些准备和清理工作。例如，我们可能需要在每个测试方法开始前创建一些对象，
然后在每个测试方法结束后销毁这些对象。我们可以在测试类中定义setUp和tearDown方法来实现这些功能。
import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # 创建数据库连接
        self.conn = create_database_connection()

    def tearDown(self):
        # 关闭数据库连接
        self.conn.close()

    def test_insert(self):
        # 使用数据库连接进行测试
        self.conn.insert(...)

在这个例子中，我们在setUp方法中创建了一个数据库连接，在tearDown方法中关闭了这个数据库连接。
这样，我们就可以在每个测试方法中使用这个数据库连接进行测试，而不需要在每个测试方法中都创建和销毁数据库连接。
'''









if __name__ == '__main__':
    unittest.main()














