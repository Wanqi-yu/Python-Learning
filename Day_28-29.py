#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/8/6 11:27
# @Author : wanqi.yu
# @File : Day_28-29.py
# @Software: PyCharm
'''

'''

class Student:
    '''
    构造函数
    包含了 学号ID 名字Name 班级stu_class 成绩用字典存储，默认值为0
    '''
    def __init__(self,ID,Name,stu_class):
        self.ID = ID
        self.Name = Name
        self.stu_class = stu_class
        self.grades = {"语文" : 0,"数学" : 0,"英语" : 0}
    '''
    设置成绩 成绩存储在字典中，所以这里使用两个参数，第一个参数是课程 第二个是成绩
    if语句判定课程在不在字典中，在的话就更改字典中这个课程对应的成绩
    不在的话输出报错
    '''
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
        else:
            print("课程不存在")
    '''
    计算分数总和,设置一个总成绩变量 默认值为0
    '''
    def sum_grade(self):
        total = 0
        for i in self.grades.values():
            total += i
        return total

    def avg_grade(self):
        total = 0
        for i in self.grades.values():
            total += i
        avg = total/3
        return avg

    def all(self):
        print(self.ID,self.Name,self.stu_class,self.grades)


student = []

chen = Student('001','chen','1班')
chen.set_grade('语文',90)
chen.set_grade('数学',89)
chen.set_grade('英语',97)


yu = Student('002','yu','1班')
yu.set_grade('语文',90)
yu.set_grade('数学',89)
yu.set_grade('英语',99)

student.append(chen)
student.append(yu)

def big_grade():
    name = ''
    total = 0
    for std in student:
        if std.sum_grade() > total:
            total = std.sum_grade()
            name = std
        else:
            continue
    return name
print(f'成绩最高的是{big_grade().Name},各科成绩分别是{big_grade().grades},总成绩为{big_grade().sum_grade()}')
























