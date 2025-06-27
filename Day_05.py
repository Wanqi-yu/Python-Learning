#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/27 20:40
# @Author : wanqi.yu
# @File : Day_05.py
# @Software: PyCharm
'''
字典/集合 学习
'''

'''
字典:在Python中，字典是一系列键值对，每个键都有对应的值相关联，可以使用键访问对应的值，与键相关联的值可以是字符串/数字/列表甚至另外一个字典
事实上，可以将任何Python对象作为字典中的值
在Python中，字典使用花括号定义
字典作为可变类型的一种，是可以直接进行更改，如新增，更改，删除等
下面是示例
'''
#定义一个字典类型的变量
name_dict = {"A":"Python",
             "B":"字典",
             "C":"集合"}
#访问字典的值 要访问字典中的值，需要在方括号中填写对应的键
print(name_dict['A'])
#添加键值对 添加新的键值对时，要给出键和值的信息 下面是语法示例
name_dict['D'] = 'SQL'
#输出更新后的字典
print(name_dict)
#修改字典中的值 修改字典值的时候，要直接使用新的值覆盖旧值，语法为 字典[键] = 新值
name_dict['A'] = 'New Value'
#输出新的值
print(name_dict['A'])
#删除键值对，在删除键值对时，可以使用del语句将相应的键值对删除，使用del语句时，必须指定字典名和要删除的键
del name_dict['D']
#输出删除后的字典
print(name_dict)
'''
嵌套:有时候需要将一系列字典存储在列表中，或是将列表存储在字典中，这个就被称为嵌套，Python可以在列表中嵌套字典，
在字典中嵌套列表，甚至在字典中嵌套字典
下面是一些示例
'''
#创建三个字典类型的变量
name_age_01 = {'Y':'25'}
name_age_02 = {'C':'28'}
name_age_03 = {'J':'31'}
#将字典嵌套到列表中
dict_list = [name_age_01,name_age_02,name_age_03]
#输出列表
print(dict_list)
#在字典中存储列表
#定义三个列表
food_01 = ['可乐鸡翅','冰可乐','皮蛋瘦肉粥']
food_02 = ['牛肉','羊肉','虾']
food_03 = ['烧鸡','大葱','自助']
#把列表嵌套到字典中
list_dict = {'Y':food_01,
             'C':food_02,
             'J':food_03}
#输出字典
print(list_dict)

#在字典中存储字典
#这里直接使用之前定义好的字典
#将字典嵌套到字典中
friend_deatil = {1:name_age_01,
                 2:name_age_02,
                 3:name_age_03}
#输出字典内容
print(friend_deatil)

'''
集合:Python中的集合是一种无序且不重复的元素集合，支持多种操作，如交集，并集等
集合有以下特点
无序性:集合中的元素没有顺序，无法使用索引访问
唯一性:集合中的元素不能重复，添加重复元素时只会保留一个
可变性:集合本身属于可变类型，可以添加和删除元素，但集合中的元素必须是不可变的(如数字，元组，字符串等)
集合可以通过大括号创建，元素中间用逗号分隔，或者也可以使用set()函数创建
下面是代码示例
'''
#定义一个集合
name_set = {'YWQ','WY','RSH'}
#输出集合的内容
print(name_set)
#添加元素 集合属于可变类型，所以可以添加和删除元素
#向集合中添加元素 语法如下 集合.add(元素) 注意:集合是唯一性的，所以添加重复元素时，只会保留一个元素
name_set.add('CCJ')
#输出更改后的集合
print(name_set)
#删除元素 删除元素时使用remove方法 语法如下 集合.remove(元素)
name_set.remove('CCJ')
#输出更新后的集合
print(name_set)
#集合是元素序列，因此可以像列表或元组一样，计算元素的个数，使用len函数 语法如下 len(集合)
print(len(name_set))

#集合也可以使用in 方法判断元素是否存在于集合中 结果会返回True或False
print('CCJ' in name_set)
print('YWQ' in name_set)

#集合除了删除元素外，还有一种直接清空元素的方法 语法如下:集合.clear()
name_set.clear()
#输出清除后的集合
print(name_set)
#关于集合，还有很多计算和内置函数，后面会慢慢在补充文件中展示

if __name__ == "__main__":
    run_code = 0
