#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/25 18:13
# @Author : wanqi.yu
# @File : Day_03.py
# @Software: PyCharm
'''
字符串操作、格式化输出
字符串是Python中常用的一种基础数据类型，属于不可变类型的一种，具有多种操作
'''
#重复输出 字符串可以使用*运算符进行重复输出 *号后面的数字是几，就是重复输出几次
print('Hello' * 3)
#长度获取，在Python中，可以使用len函数获取字符串的长度
#len(要获取长度的变量或值)
print(len("Hello World!"))
#索引与切片
'''
索引是表示字符串中某一个字符的位置，要注意的是，索引是从0开始的，第一个字符的索引是0，切片则是使用两个索引，复制字符串的数据
切片:对操作的对象截取一部分的操作
语法 字符串[索引]
切片 字符串[开始索引:结束索引]
注意点: 开始索引和结束索引中间由冒号分割，如果不写开始索引，默认从第一个字符开始，并且切片会显示到结束索引的前一位
下面是一些例子
'''
#通过字符串的索引获取值
message = "Hello World!"
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
#通过切片获取字符串和复制字符串
print(message[0:4]) #这里会输出Hell 因为结束索引位置的字符不显示
#索引可以是负数，并且负数由-1开始，最后一位字符的索引是-1
print(message[-1])

#判断字符是否在字符串内 在Python中，可以使用in 来判断，字符是否在字符串内，in 会返回两个结果 True和False，True为真，False为假
print('H' in "Hello World!")    #H在字符串Hello World!内，所以返回为真，也就是 True
print('N' in "Hello World!")    #N不在字符串Hello World!内，所以返回为假，也就是False

#join方法拼接字符串 在Python中,Join方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#注意:join只接收一个参数，必须是可迭代的对象，否则将会报错
'''
迭代:迭代是计算机科学中的核心概念，指通过重复执行某个过程来逐步接近目标结果的行为。在编程中，迭代特指按顺序访问集合中的每个元素的过程。
后续将制作为详细笔记记录
'''
print(''.join(['a','b','c']))
#统计字符或字符串出现的次数，在Python中，可以使用count方法来统计一个字符或一个字符串在长字符串中出现的次数，下面是简单使用例子
#语法 字符串.count(要统计的字符或字符串)
print(message.count('l'))

#判断字符串是否以指定字符开头或结尾
#可以使用startswith和endswith方法进行判断，返回的逻辑与in一直
print(message.startswith('H'))
print(message.endswith('H'))

#寻找指定字符出现的第一个位置，并返回对应的索引
print(message.find('e'))

#替换字符串，替换字符串可以使用replace方法，需要给出两个参数，1.要替换的字符 2.被替换进字符串里的字符，下面是简单示例
print(message) #原始字符串
message = message.replace('World!','Wanqi') #将World替换成Wanqi
print(message) #替换后的字符串

#字符串分割，使用split对传入的字符串进行分割,split接收两个参数，1.分隔符 2.分割的次数 分割后会返回一个列表
print(message.split(' '))

#根据字符查询在字符串中的索引位置 与find方法有类似的功能
print(message.index('W'))

'''
字符串检测，在Python中，有很多用于字符串类型检测的方法，如检测字符串的组成，字符串是否为大小写等
下面是详细的例子和实际代码
'''
print(message.isalnum()) #检查字符串是否由字母和数字组成
print(message.isidentifier()) #检查字符串是否以字母开头且合法
print(message.islower()) #检查字符串是否为全小写
print(message.isupper()) #检查字符串是否为全大写

#字符串的大小写转换 如果要将字符串的大小写全部转换过来，可以使用swapcase方法，这个方法会把字符串内的小写字母转换为大写，大写字母转换为小写
print(message.swapcase())

#字符串居中，在Python中，可以使用center方法，使字符串居中显示，需要给出两个参数，1.字符串长度 2.字符串两边显示的字符
print(message.center(50,'-'))

'''
格式化输出:将信息按照预定的格式展示给用户，使其更容易理解和使用。在Python中，可以使用格式化符号，f-字符串和其他函数来实现
'''
#字符串插值 在字符串中插入变量，在Python3.6之前，可以使用百分号格式化字符串，在更高版本，我们可以使用f-字符串
#使用百分号的语法如下 在使用百分号时，要在百分号后加上代码数据类型的字符,字符串 %s 整数%d 浮点数%f
name = 'Wanqi'
age = 25
print('My name is %s and I am %d years old.'%(name,age))
#使用f字符串的方法如下 f-字符串是在引号外加入一个f字符，这个时候可以在字符串内使用{}，大括号里面添加要显示的变量
#这种方式可以不用讲变量的类型进行更改，在实际使用时，会增加代码的可读性及简洁性
print(f"My name is {name},I am {age} years old!")
#此外还有format方法，format方法与f字符串类似，但具有多种可选的使用方式
#下面是语法示例
#可以看到，format的语法和f字符串类似，都是使用{}在字符串中插入要格式化的变量，这个是使用位置来指定变量值
print("My name is {} and I am {} years old!".format(name,age))
#format方法还可以使用名称来指定变量值
print("My name is {n} and I am {a} years old!".format(n=name,a=age))

#由于目前常用的方法基本是这三种，其他方法暂时不过多赘述

'''
ASCII艺术字:ASCII 艺术字是用纯文本字符（字母、数字、符号）构成的视觉图形化文字。在 Python 中，可通过多种方式生成 ASCII 艺术字
以下是其中一种实现方法，使用了第三方库
第三方库:在Python中，包含了许多用于处理信息的库和函数，但当我们需要的函数没有时，我们可以使用非MES官方的库，这些库一般是由一些Python社区或
组织开发的，不属于Python标注库的软件包，它们极大的扩展了Python的功能，当我们需要安装第三方库时，可以使用下面的命令
pip install 库名称
导入第三方库时，使用 import 库名称
下面是使用Python第三方库制作ASCII艺术字
'''

import pyfiglet
my_word = '''
Don't be trapped by your past self, start thinking about the meaning of life from now on, plan your future, change yourself, remove those flaws and become a better you!
'''
print(pyfiglet.print_figlet(my_word))
if __name__ == "__main__":
    run_code = 0
