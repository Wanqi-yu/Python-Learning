#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2025/7/12 13:35
# @Author: 23955
# @File: Practice_week_03.py
# @Software: PyCharm
'''
### **第3周**
**练习1：学生成绩分析器**
要求：
- 创建函数 `analyze_grades(grade_list)`
- 输入为成绩列表（如 `[85, 92, 78, 90]`)
- 返回字典包含：
  - "max": 最高分
  - "min": 最低分
  - "avg": 平均分（保留1位小数）
- 示例：`analyze_grades([80, 90, 75])` 返回 `{"max":90, "min":75, "avg":81.7}`

**练习2：单词频率分析**
要求：
- 创建函数 `word_frequency(text)`
- 忽略大小写和标点符号
- 返回字典格式：`{单词: 出现次数}`
- 示例：`word_frequency("Hello world, hello Python")` 返回 `{'hello':2, 'world':1, 'python':1}`

**练习3（扩展）：停用词过滤**
要求：
- 扩展 `word_frequency` 函数
- 添加参数 `stop_words=["the", "is", "and"]`
- 过滤常见停用词
- 示例：`word_frequency("The cat is on the mat", stop_words=["the", "is"])` 返回 `{'cat':1, 'on':1, 'mat':1}

'''


'''
1.学生成绩分析器
'''
#定义函数
# def analyze_grades(grade_list:list):
#     '''
#     获取输入
#     :param grade_list: 列表形式的参数
#     :return: 以字典类型返回
#     '''
#     grade_total = 0
#     for grade in grade_list:
#         grade_total += grade
#     grade_avg = grade_total / len(grade_list)
#     grade_dict = {}
#     grade_dict['max'] = max(grade_list)
#     grade_dict['min'] = min(grade_list)
#     grade_dict['avg'] = round(grade_avg,1)
#     return grade_dict
#
# grade_list = [int(i) for i in input("请输入要计算的成绩，成绩之间以空格分割:").split(' ') ]
#
# print(analyze_grades(grade_list))


'''
2.单词频率分析
'''

# def word_frequency(text:str):
#     '''
#     获取输入的字符串，并计算单词出现的频率
#     :param text: 字符串类型的参数
#     :return: 返回以字典类型的计数
#     '''
#     text = text.lower()
#     text_count = {}
#     for word in text.split(' '):
#         if word.lower() in text_count:
#             text_count[word] += 1
#         else:
#             text_count[word] = 1
#     return text_count
#
# text_input = input("请输入要计算单词频率的字符串:")
#
# print(word_frequency(text_input))

'''
3.停用词过滤
'''

def word_frequency(text:str,stop_words:list) -> dict:
    text = text.lower()
    text.split()
    word_dict = {}
    for word in text.split():
        if word in stop_words:
            continue
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

text = input("请输入要计算频率的单词，单词间以空格分割:")
stop_word = input().lower()
stop_word = stop_word.split()

print(word_frequency(text,stop_word))


if __name__ == "__main__":
    run_code = 0
