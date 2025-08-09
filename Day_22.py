#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/22 17:47
# @Author : wanqi.yu
# @File : Day_22.py
# @Software: PyCharm
'''
数据序列化/反序列化
数据序列化(Serialization)
指将数据结构或对象转换为可存储或传输的格式的过程。这通常涉及将数据转换为字节流或字符串，以便它们可以在不同的环境中传递或存储。
反序列化(Deserialization)
是将序列化后的数据还原为原始数据结构或对象的过程。允许在接收端或将来的时间点重新使用数据
为什么需要数据序列化和反序列化
在编程中使用数据序列号与反序列化有以下几个原因
数据交换：当不同的应用程序需要共享数据时，它们可能位于不同的计算机、操作系统或编程语言中。序列化数据使得跨越这些边界成为可能。
数据存储：序列化数据可以有效地保存在文件、数据库或其他持久性存储中，以备将来使用。
跨语言通信：如果系统需要与其他编程语言编写的组件进行通信，序列化和反序列化是一种跨语言通信的通用方式。
远程调用：在分布式系统中，远程调用需要将数据从客户端传输到服务器，并在服务器上执行操作。序列化和反序列化允许这种通信。
数据序列化与反序列化是在不同情况下实现数据的可传输性和持久性的强大工具。
常见的数据序列化格式
1.Json(JavaScript Object Notation)
JSON是一种轻量级的文本数据交换格式，易于人类阅读和编写，同时也易于机器解析和生成。它基于JavaScript的对象字面量表示法，但已成为多种编程语言的通用格式。
在Python内置了 json库用于进行数据序列化和反序列化
Json在Web API\配置文件\日志记录等方面广泛应用
2.xml(eXtensible Markup Language)
XML是一种可扩展的标记语言，用于存储和交换数据。它的结构具有层次性，允许表示复杂的数据结构。
在Python中，有多个库用于处理XML数据包括xml.etree.ElementTree和lxml。
import xml.etree.ElementTree as ET

data = ET.Element('person')
name = ET.SubElement(data, 'name')
name.text = 'Alice'
age = ET.SubElement(data, 'age')
age.text = '30'

xml_string = ET.tostring(data, encoding='utf8').decode('utf8')  # 将XML元素序列化为字符串

# 从XML字符串反序列化为XML元素
root = ET.fromstring(xml_string)
3.Pickle
Pickle是Python的内置模块，用于将Python对象序列化为二进制数据，然后反序列化为原始对象，但是仅适用于Python
import pickle

data = {'name': 'Carol', 'age': 35}

# 将Python对象序列化为二进制数据
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# 从二进制数据反序列化为Python对象
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
下面是代码示例，在本示例中，主要使用Json进行数据序列化和反序列化
'''

'''
序列化
在json模块中，提供了两个方法用于将数据序列化
1.json.dumps():将Python对象转换为json格式的字符串
2.json.dump():将Python对象转换为json格式并写入文件中
下面是代码示例
'''
import json
data = {"Age":25}
#使用dumps方法可以将Python中字典类型的数据转换为Json格式
json_data = json.dumps(data)
print(json_data)
file_data = {

    "name": "李四",

    "age": 25,

    "is_employee": False,

    "skills": ["JavaScript", "HTML", "CSS"]

}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(file_data, f, ensure_ascii=False, indent=4)
'''
反序列化
反序列化是指将JSON格式的字符串转换回Python数据对象，json模块同样提供了两个主要的方法来实现这一过程
1.json.loads():将json格式的字符串解码为Python对象
2.json.load():从文件中读取json字符串并将其解码为Python对象
下面是代码示例
'''
#同时Python也支持将序列化的数据进行反序列化 反序列化后，会转换为Python中的字典格式
loda_data = '{"name": "王五", "age": 28, "is_employee": true, "skills": ["Go", "Rust"]}'
data_dict = json.loads(loda_data)
print(data_dict)

#使用json.load()从文件中读取
with open('data.json', 'r', encoding='utf-8') as f:
    read_data = json.load(f)

print(read_data)

print(type(read_data))

'''
json的应用场景
json广泛应用用各个场景，如
Web API：作为Web服务的数据交换格式，客户端和服务器之间经常使用JSON进行通信。通过JSON，Web应用程序可以请求和响应数据。
配置文件：许多应用程序使用JSON格式的配置文件来存储设置和配置信息。JSON易于人类阅读和编写，同时也容易解析。
日志记录：JSON格式也常用于日志记录，因为它可以结构化存储各种信息，例如时间戳、事件和数据。
数据存储：有时，数据需要持久存储，以备将来使用。JSON格式适合于将数据写入文件或数据库，并在需要时进行检索。
使用JSON进行数据序列化与反序列化是一种通用的、可扩展的方法，可用于各种不同的应用程序和用例。
'''

'''
数据类型对应表
在Python中，不同的数据类型在序列化和反序列化过程中会对应不同的JSON数据类型。以下是Python与JSON之间的数据类型转换对应表
Python数据类型	JSON数据类型
dict	        object
list	        array
tuple	        array
str	            string
int	            number
float	        number
bool	        true/false
None	        null
'''








if __name__ == "__main__":
    run_code = 0
