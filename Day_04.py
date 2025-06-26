#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/26 16:41
# @Author : wanqi.yu
# @File : Day_04.py
# @Software: PyCharm
'''
列表和元组基础
购物清单管理程序
'''
'''
列表:由一系列按特定顺序排列的元素组成，在Python中，用方括号[]来表示列表，并用逗号分隔其中的元素
'''
#定义一个数值类型的列表 元素全部由整数组成
num_list = [1,2,3,4,5,6,7,8,9]
#输出列表内容
print(num_list)

#访问列表的元素 列表是有序集合，因此要访问列表中的元素时，只需要将该元素索引的位置告诉Python即可
#访问列表中第1个元素 索引从0开头，所以实际是第一个元素
print(num_list[0])
'''
修改，增加和删除元素
列表在Python中是可变类型的一种，因此可以随着程序运行增加和删除元素
'''
#修改列表元素 修改列表元素时需要给出两个参数 1.索引 2.新的值
num_list[0] = 10
print(num_list)

#在列表中添加元素 在添加元素时，具有多个方法，如在某个索引前后添加，或直接添加到列表末端
#下面是一个使用append方法像列表末端添加元素的示例 append方法会将值添加进列表中，并默认放在列表最后
num_list.append(11)
print(num_list)

#向列表中插入元素 insert方法可以向列表中任意位置添加元素，为此需要给出两个参数 1.新元素的索引 2.新元素的值
num_list.insert(0,'12')
print(num_list)

#还有一种方法是使用extend方法向列表中添加值，但要注意的是，extend方法只接受可以迭代的值
num_list.extend('Hello')
print(num_list)
#从列表中删除元素，删除元素有两种方法，一种是del语句，另一种是remove方法，del语句需要知道要删除的元素在列表中的位置，也就是索引
#而remove方法则不需要，只需要值即可，还可以使用pop方法弹出列表中的值，默认情况下pop方法会弹出列表末端的值，但pop方法可以像Insert方法一样使用
#使用del删除
del num_list[0]
print(num_list)
#使用remove方法删除
num_list.remove(10)
print(num_list)
#使用方法pop删除元素 pop方法可以删除列表末尾的元素，并能够接着使用它，如果你需要元素的值，可以将它保存在一个变量中
pop_value = num_list.pop()
print(num_list)
print(pop_value)

'''
组织列表:在创建的列表中，元素的排列常常是无法预测的，有时我们需要以特定顺序呈现信息，这时我们就可以使用排序语句或方法
sort方法 这个方法可以对列表进行永久性的排序，另外可以向sort方法输入参数   reverse=True，这时就可以反转排序
sorted函数，这个函数会暂时改变列表的排序，适合在临时场景中使用
下面是一部分示例
'''
#创建一个数值类型的列表
new_list_1 = [1,3,2,4,7,6]
#输出原始列表
print(new_list_1)
#使用sort方法进行排序
new_list_1.sort()
#输出排序后的列表
print(new_list_1)
#向sort方法传入参数，进行反向排序
new_list_1.sort(reverse=True)
print(new_list_1)
#再创建一个数值类型的列表
new_list_2 = [1,3,5,6,7,2,4,9,10,8]
print(new_list_2)   #输出原始列表
print(sorted(new_list_2))   #使用sorted函数进行临时排序
print(new_list_2)#再次输出原始列表

#倒着打印列表，reverse方法可以将列表中的元素顺序进行直接的反转
new_list_2.reverse()
print(new_list_2)   #输出反转后的列表
#确定列表的长度，与字符串一致，都是使用len函数确认长度
print(len(new_list_2))
#列表相关的内容还有切片，列表复制与推导式等，切片与复制已在字符串中展示过，后续将会补充文件和练习

'''
元组:元组是一种与列表类似的数据结构，使用圆括号()包裹，元组与列表的不同之处在与，它是不可修改的，属于不可变类型
'''
#定义元组，与定义列表相同，只是使用了圆括号
name_tuple = ('Andy','Ben','Corey') #定义一个字符串元素的元组
print(name_tuple)   #输出元组
#修改元组变量 元组是不可变的类型，所以无法修改元组中的元素，但可以直接对存储元组的变量赋值，覆盖旧的值
name_tuple = ('Anna','Barry','Cai') #给这个变量赋新的值
print(name_tuple)   #输出新的元组

'''
购物清单管理
1.创建一个空列表，接收用户输入的数据
2.将用户输入的数据添加到列表中
3.使用字符串操作方法，将用户输入的内容分隔，分隔符是空格
'''
#定义一个空列表
shop_list = []
#获取用户的输入
shop = input('请输入你要购买的物品，以空格分隔:\n')
#使用split方法分隔并把分隔后的值加入列表中
shop_list.extend(shop.split(' '))
#输出最后的清单
print(shop_list)
if __name__ == "__main__":
    run_code = 0
