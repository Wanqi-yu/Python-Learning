#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/4 12:41
# @Author : wanqi.yu
# @File : Day_10.py
# @Software: PyCharm
'''
文件读写/异常处理
文件读写:从文件中读取数据
在日常工作中，经常会遇到要从文件中读取信息的场景，在Python中，文件读写是基础技能之一，无论是数据处理，日志记录还是配置管理，都需要对文件的读写
要读写文件的信息，需要首先将信息读取到内存中，为此可以一次性读取文件所有内容或一行一行的读取
Python提供了一些函数和方法用于打开和读取文件信息，下面是示例
'''

#要读取文件，第一步就是要打开文件，在Python中，提供了open函数进行文件打开，open函数接收三个参数，一个是文件路径，一个是打开模式，还有一个是
#文件编码
'''
打开模式:
'r' 只读模式，用于读取文件内容
'w' 写入模式，用于向文件中写入信息，如果文件不存在，则会自动创建一个新文件，如果文件已存在，将会把文件内容清空后再进行写入
'a' 追加模式，用于在文件末尾添加内容，如果文件不存在，会创建一个新文件
'b' 二进制模式，用于处理二进制文件，如图片，视频等
'''
#以只读模式打开文件，编码是utf8
file = open('Python_Read.txt','r',encoding='utf8')
#读取文件，在打开文件后，就可以进行文件的读取，与打开模式相似，读取也有多个模式，它们的不同在于，读取使用的是方法
#在上面我们定义了一个名为file的变量用来存储文件对象，接下啦可以使用读取方法来读取文件
#全部读取 全部读取时可以使用 变量.read方法 这个方法会把文件中所有的信息读取出来，这样我们就可以保存到变量中
# file_deatil = file.read()
# print(file_deatil)
#逐行读取，除了读取所有内容，Python还可以一行一行的读取，使用变量.readline()方法
#这个方法默认读取一行
# file_deatils = file.readline()
# print(file_deatils)

#读取所有行，readlines这个方法可以读取文件所有内容，并返回一个列表，列表中的元素为文件中的每一行
# file_list = file.readlines()
# print(file_list)

'''
关闭文件:在文件读取完成后，要注意的一点是必须关闭文件，否则文件将无法被其他软件打开
关闭文件时使用变量.close方法
在Python中，有时我们不想手动关闭，Python提供了一个语法可以在使用完成后自动关闭
语法如下
with open(文件路径,模式,编码) as file:
    操作代码
注意:这里使用了as关键字 是为了把打开的文件对象保存到变量中
并且操作文件的代码在with代码块内
'''
# file.close()
#使用with open语法
# with open('Python_Read.txt','r',encoding='utf8') as file:
#     print(file.read())

'''
写入文件:除了读取文件的内容，有时候我们也需要向文件中写入一些信息，比如程序的日志，发生的异常等
与读取一样，写入也是使用了对应的方法，下面是代码示例
写入有两种，一种是单行写入，另一种是多行写入
'''
#单行写入
# with open('Python_Write.txt','w',encoding='utf8') as file:
#     file.write('使用Python向文件中写入内容')
#在写入后我们可以再使用一次读取模式确认我们写入的内容
# with open('Python_Write.txt','r',encoding='utf8') as file:
#     print(file.read())

#多行写入
# with open('Python_Write_2.txt','w',encoding='utf8') as file:
#     file.writelines('这是第一行\n这是第二行\n这是第三行\n')

'''
文件迭代器:文件对象是可迭代的，所以我们可以使用for循环逐行读取文件内容，但目前已经有了readline方法，所以仅做演示
'''
# with open('Python_Read.txt','r',encoding='utf8') as file:
#     for line in file:
#         print(line)

'''
文件追加写入:在实际编程中，由于程序问题，我们可能要不断的向同一个文件中写入，但写入模式会清空之前的文件内容，在这种情况下
我们就可以使用追加模式 向文件写入数据,追加模式会自动向文件的末尾添加数据
语法示例如下
'''

# with open('Python_Write_2.txt','a',encoding='utf8') as file:
#     file.write('这个是使用了追加模式向文件中写入的信息')

'''
二进制文件处理，在处理二进制文件时，打开文件时，需要指定b模式
并且不能单独使用,必须要和其他模式搭配 如 rb ab wb等
下面是代码示例
'''
# with open('踢你屁股.png','rb') as file:
#     print(file.read())

'''
异常:异常是程序在执行过程中发生的错误事件，它会中断程序的正常执行。如果没有适当处理异常，程序将会终止并输出错误信息。
常见的异常包括除零错误、文件未找到错误、类型错误等。
异常处理:Python使用被称为异常的特殊对象来管理程序运行期间发生的错误，每当发生让Python不知所措的错误时，它都会创建一个异常对象
，如果你编写了处理该异常的代码，程序将会继续运行，如果你未对异常进行处理，程序将会停止，并显示一个traceback,其中包含有关异常的报告
在Python中，异常使用try-except代码块进行处理，try-except让Python执行指定的操作，同时告诉Python应该怎么做，使用这个代码块后
即使出现异常，程序也将会继续运行，显示你编写的友好信息，而不是让用户迷惑的traceback
下面是一个简单的示例
'''

#在Python中，数字是不能除0的，这样做会引发异常，Python会返回一个traceback
# print(5/0)

'''
在运行这个代码时，python将会返回下面的报错信息
Traceback (most recent call last):
  File "Day_10.py", line 103, in <module>
    print(5/0)
          ~^~
1 ZeroDivisionError: division by zero
1处指出的错误ZeroDivisionError 是一个异常对象。Python无法按你的要求做时，就会创建这种对象。在这种情况下，Python将停止运行程序，并指出
引发了哪种异常，而我们可根据这些信息对程序进行修改。下面我们将告诉Python，发生这种错误时怎么办；这样，如果再次发生这样的错误，Python将会返回
我们设定好的错误信息,下面是代码示例
'''

try:
    print(5/0)
except:
    print('0无法作为被除数')

'''
我们将导致错误的代码放进了try代码块中，如果try代码块中的代码运行起来没有问题，Python会跳过except代码块，如果try代码块中的代码引发了错误
Python会查找对应的except代码块，并运行其中的代码
'''

'''
使用异常避免崩溃:发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就能再提示用
户提供有效输入，而不至于崩溃。
下面我们来创建一个只执行除法的简单计算器
'''
print('请输入两个数字，作为除数和被除数')
print('按q退出程序')

while True:
    first_number = input('第一个数字')
    if first_number == 'q':
        break
    second_number = input('第二个数字')
    if second_number == 'q':
        break
    result = int(first_number) / int(second_number)
    print(result)
'''
这个程序提示用户输入数字，并存储到变量中，如果用户输入的是q，就会退出程序
这个程序没有任何的处理措施，一旦让它执行除数为0的计算时，它就会崩溃
通过将可能引发错误的代码放在try-except代码块中，可以提高程序抵御错误的能力
'''

'''
else块
else块可以和try和except一起使用，用于在没有引发异常时执行的代码
语法如下
try:
    # 可能会引发异常的代码
except ExceptionType:
    # 处理异常的代码
else:
    # 没有异常时执行的代码
'''
try:
    x = 10 / 2
except ZeroDivisionError:
    print("除零错误！")
else:
    print("计算成功，结果为：", x)
'''
finally块
finally块中的代码无论是否发生异常都会执行，通常用于清理工作，如关闭文件或释放资源。
try:
    # 可能会引发异常的代码
except ExceptionType:
    # 处理异常的代码
finally:
    # 始终执行的代码
'''

'''
处理多个异常
except可以处理一个专门的异常，也可以处理一组圆括号中的异常，
如果except后没有指定异常，则默认处理所有的异常。每一个try，都必须至少有一个except
语法如下
try:
    x = int(input("请输入一个整数："))
    y = 1 / x
except ValueError:
    print("输入的不是一个整数！")
except ZeroDivisionError:
    print("输入的整数不能为零！")

在python的异常中，有一个万能异常：Exception，他可以捕获任意异常
可以通过捕获基类Exception来捕获所有异常，但这是一种不推荐的做法，除非在特定情况下确实需要捕获所有可能的异常

自定义异常:可以通过创建自定义异常类来定义自己的异常类型，通常自定义异常类继承自Exception类。
语法示例
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print("捕获自定义异常：", e)

'''




















































if __name__ == "__main__":
    run_code = 0
