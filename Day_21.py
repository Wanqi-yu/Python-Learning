#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/21 17:44
# @Author : wanqi.yu
# @File : Day_21.py
# @Software: PyCharm
'''
正则表达式
正则表达式(Regax)是一种用于字符串匹配的强大工具，广泛应用于各大开发语言中
内容涵盖:简单字符串匹配，多条件匹配，按类型匹配和中文字符匹配等
在Python3已经内置了正则表达式库，要使用的话，只需要导入即可，库名是re
本篇介绍常用方法
向re.compile()传入一个字符串，表示正则表达式，它将返回一个Regex模式对象
接着我们就可以对这个Regex对象进行操作
下面是代码示例
'''
#导入正则表达式库
import re
# #创建匹配对象 \d表示匹配数字，更多匹配字符会在单独的笔记中记录
# ph_number = re.compile(r"\d\d\d-\d\d\d\d-\d\d\d\d")
# '''
# 匹配Regex对象
# Regex对象的search()方法会查找传入的字符串，寻找该正则表达式的所有匹配，如果字符串中没有找到符合该正则表达式的字符，将会返回None
# 如果找到了该模式，search会返回一个Macth对象，Macth对象有一个group方法,它返回被查找的字符串中实际匹配的文本--稍后解释
# 下面是代码示例
# '''
# #创建两个变量用来存储Macth对象，并传入字符串，第一个会返回Macth对象，第二个会返回None
# result_1 =  ph_number.search("我的手机号是 111-1111-1111")
# result_2 = ph_number.search("我的手机号是 11111111111")
# print(result_1.group())
# print(result_2)
#
#
# '''
# 利用括号分组
# 假如需要将电话号码的分开显示，可以通过在正则表达式中添加括号创建分组
# (\d\d\d)-(\d\d\d\d)-(\d\d\d\d)
# 然后可以使用group()匹配对象方法，从一个分组中获取匹配的文本
# 第一队括号是第一组，第二队括号是第二组，向group()匹配对象方法中传入整数1或者2，就可以取得匹配文本的不同部分，传入0或者不传入参数
# 则会默认获取所有文本 ，下面是代码示例
# '''
#
#
# #创建一个正则表达式，并用括号分组
# ph_number_group = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
#
# group_1 = ph_number_group.search("我的手机号是 123-4567-8910")
# #获取第一组
# print(group_1.group(1))
# #获取第二组
# print(group_1.group(2))
# #获取第三组
# print(group_1.group(3))
# #传入0获取全部
# print(group_1.group(0))

'''
如果想要获取所有的分组,可以使用groups方法
groups返回多个值的元组，所以可以使用多重复制的方法，每个值赋给一个单独的变量
'''
# print(group_1.groups())

'''
括号在正则表达式中有特殊的含义，但当你需要匹配括号时该怎么办呢，这种情况下，可以使用反斜杠\和()进行字符转义，下面是代码示例
'''
# new_re = re.compile(r"(\(\d\d\d\))-(\d\d\d\d)-(\d\d\d\d)")
#
# new_result = new_re.search('我的手机号是 (123)-4567-8910')
#
# print(new_result.group(1))

'''
用管道匹配多个分组
字符|被称为管道符，希望匹配许多表达式中的一个时，就可以使用它，例如
正则表达式 r"Batman|Tina Fey"将匹配 Batman或Tina Fey
下面是代码示例
'''

heroRegex = re.compile(r'Batman|Tina Fey')

hero_name = heroRegex.search("Batman")
print(hero_name.group())

'''
也可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分
假如你想匹配所有由Bat开头的字符串，如Batman,Batmobile,Batcopter等，如果能够指定前缀，就很方便，这些可以通过括号实现
下面是代码示例
'''
batre = re.compile(r"Bat(man|mobile|copter)")
bat_1 = batre.search("Batmobile")

print(bat_1.group())

'''
用问号实现可选匹配
有时候，想要匹配的模式是可选的，就是说，这段文本无论存不存在，正则表达式都会认为匹配
字符?表示它前面的分组在这个模式中是可选的，下面是代码示例
'''
#创建一个正则表达式对象
friend = re.compile(r"(gril)?friend")
#向正则表达式对象中传入字符串并保存到变量中
friend_1 = friend.search('friend')

friend_2 = friend.search('grilfriend')

print(friend_1.group())
print(friend_2.group())

'''
用星号*匹配多次
*被称为星号，意味着匹配零次或多次，即星号之前的分组，可以在文本中出现任意次。它可以完全不存在，或一次又一次的重复
下面是代码示例
'''

batre_02 = re.compile(r"Bat(wo)*man")

bat_2 = batre_02.search("Batwowowowoman")
print(bat_2.group())

'''
用加号+匹配一次或多次
+加号的作用与星号类似，但加号意味着至少要出现一次，这不是可选的
下面是代码示例
'''
#定义一个正则表达式
batre_03 = re.compile(r"Bat(wo)+man")
#传入字符串，包含了wo，满足了至少一次的要求
bat_3 = batre_03.search("Batwoman")
print(bat_3.group())#返回符合的字符
#因为没有wo，所以会返回None
bat_4 = batre_03.search("Batman")
print(bat_4)

'''
用花括号匹配特定次数
如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字，例如正则表达式(Ha){3}将匹配字符串"HaHaHa"，但不会匹配"HaHa"
因为后者只重复了两次
除了一个数字，还可以指定一个范围，即在花括号内写下一个最小值，一个逗号和一个最大值
例如正则表达式(Ha){3,5}将匹配"HaHaHa"和"HaHaHaHa"以及"HaHaHaHaHa"，也可以不写花括号中的第一个或第二个数字，不限制最小值或最大值
下面是代码示例
'''

happy_01 = re.compile(r"(Ha){3}")

happy_02 = re.compile(r"(Ha){3,5}")

happy_03 = re.compile(r'(Ha){1,}')

happy_04 = re.compile(r'(Ha){,5}')

happy_re_01 = happy_01.search("HaHaHa")
print(happy_re_01.group())
happy_re_02 = happy_02.search("HaHaHa")
print(happy_re_02.group())
happy_re_03 = happy_02.search("HaHa")
print(happy_re_03)
happy_re_04 = happy_03.search("HaHaHaHa")
print(happy_re_04.group())
happy_re_05 = happy_04.search("Ha")
print(happy_re_05.group())

'''
贪心和非贪心匹配
在字符串'HaHaHaHaHa'中，因为(Ha){3,5}可以匹配 3 个、4 个或 5 个实例，你可能
会想，为什么在前面花括号的例子中，Match 对象的 group()调用会返回'HaHaHaHaHa'，
而不是更短的可能结果。毕竟，'HaHaHa'和'HaHaHaHa'也能够有效地匹配正则表达
式(Ha){3,5}。
Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽
可能匹配最长的字符串。花括号的“非贪心”版本匹配尽可能最短的字符串，即在
结束的花括号后跟着一个问号
下面是代码示例
'''
#正则表达式默认贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
#这里使用了问号和花括号，将正则表达式更改为非贪心匹配
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

'''
findall方法
除了search方法外，Regex对象也有一个findall()方法。search()将返回一个Match
对象，包含被查找字符串中的“第一次”匹配的文本，而 findall()方法将返回一组
字符串，包含被查找字符串中的所有匹配。
下面是代码示例
'''
ph_number_Regex = re.compile(r"\d\d\d-\d\d\d\d-\d\d\d\d")
#这里使用了search方法，所以只返回第一次匹配的文本
ph_number_01 = ph_number_Regex.search("我的手机号是 123-4567-8910和109-8765-4321")
#这里使用findall方法，这个方法会返回一组字符串，包含所以匹配的文本,返回的类型是列表类型
ph_number_02 = ph_number_Regex.findall("我的手机号是 123-4567-8910和109-8765-4321")

print(ph_number_01.group())

print(ph_number_02,type(ph_number_02))

'''
字符分类
在前面的例子中，我们可以看到\d表示数字，在正则表达式中有许多这样的缩写字符分类
下面是一些常用的
\d  0-9的任何数字
\D  除了0-9的数字以外的任何字符
\w  任何字母、数字和下划线
\W  除字母，数字和下划线以外的任何字符
\s  空格、制表符或换行符(可以认为是匹配"空白"字符)
\S  除空格、制表符和换行符以外的任何字符
正则表达式的内容非常丰富，后续将继续补充
'''



if __name__ == "__main__":
    run_code = 0
