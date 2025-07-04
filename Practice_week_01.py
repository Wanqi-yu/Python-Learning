#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/6/28 10:49
# @Author : 23955
# @File : Practice_week_01.py
# @Software: PyCharm
'''
每周六进行简单练习
**第1周：基础语法（无函数）**
1. **BMI计算器**
   - 要求：使用变量存储身高(m)和体重(kg)，计算并打印BMI值（公式：体重/身高²）

2. **购物车总价计算**
   - 要求：给定商品列表 `[("苹果", 5.5, 2), ("牛奶", 3.8, 1)]`，计算总价并格式化输出

3. **用户登录验证**
   - 要求：预定义字典 `users = {"alice": "pass123"}`，通过input获取输入并验证
'''
#1.BMI值计算器
#定义两个变量获取身高和体重
# weight = float(input("请输入你的体重:,单位(KG)"))
# height = float(input("请输入你的身高:,单位(M)"))
#计算BMI值并保存到变量BMI中
# BMI = weight / (height * height)
#输出BMI值
# print(f"你的BMI值是{BMI}")

#2.购物车总价计算
'''
商品列表是使用了列表嵌套元组类型，所以首先要获取列表的元素，列表[索引][索引] 这样可以把元组中的值取出，再进行计算
'''
#定义商品列表
shop_list = [("苹果", 5.5, 2), ("牛奶", 3.8, 1)]
#使用索引获取列表中的元组，再使用第二个索引获取元组中的值，并计算
apple_price = shop_list[0][1] * shop_list[0][2]
milk_price = shop_list[1][1] * shop_list[1][2]
#计算两个商品的和
total_price = apple_price + milk_price
print(f"购物车的总价是{total_price}")

#3.用户登录验证
users = {"alice": "pass123"}
password = input("请输入你的密码")
print(f"{users['alice'] == password}")
if __name__ == "__main__":
    run_code = 0
