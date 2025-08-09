#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/23 19:40
# @Author : wanqi.yu
# @File : Day_23.py
# @Software: PyCharm

'''
日志记录
日志记录框架是一种工具，可帮助您标准化应用程序中的日志记录过程，虽然某些编程语言提供内置日志记录模块作为其标准库的一部分，但大多数日志记录框架
都是第三方库，例如logging(Python)、Log4j(Java)、Zerolog(Go)或Winston(Node.js)
有时，组织会选择开发自定义日志记录解决方案，但这通常仅限于具有高度专业化需求的大型公司。
Python中提供了一个标准库进行日志记录 库名是 logging
该日志记录解决方案有效地满足了库和应用程序开发人员的需求，并包含了以下严重性级别：DEBUG、INFO、WARNING、ERROR 和 CRITICAL
以下是代码示例
'''

import logging
#
# logging.debug("A debug message")
# logging.info("An info message")
# logging.warning("A warning message")
# logging.error("An error message")
# logging.critical("A critical message")
'''
输出:
WARNING:root:A warning message
ERROR:root:An error message
CRITICAL:root:A critical message
此default（或root）记录器在该WARNING级别运行，这意味着只有严重性等于或超过的记录调用WARNING才会产生输出

'''

'''
自定义日志记录器
这种配置可确保只显示潜在的重要信息，减少日志输出中的噪音。不过，Python也可以根据需要自定义日志级别并微调日志记录行为。
使用logging模块的推荐方法是通过 getLogger()方法创建自定义日志记录器
import logging

logger = logging.getLogger(__name__)
一旦有了自定义记录器，就可以通过 logging模块 提供的Handler(处理程序)、 Formatter(格式化器)和Filter(过滤器) 类来自定义其输出。
Handlers决定输出目的地，并可根据日志级别进行定制。一个日志记录器还可添加多个Handlers，以便同时向不同目的地发送日志信息。

Formatters决定了日志记录器产生的记录的格式。然而，目前还没有JSON、Logfmt等预定义格式。您必须结合可用的日志记录属性来构建自己的格式。
root日志记录器的默认格式为%(levelname)s:%(name)s:%(message)s。
然而，自定义日志记录器默认为只有%(message)s。

Filters由handler和logger objects使用，用于过滤日志记录。与日志级别相比，Filters能更好地控制哪些日志记录应被处理或忽略。
在日志被发送到最终目的地之前，它们还能以某种方式增强或修改记录。例如，您可以创建一个自定义过滤器，以删除日志中的敏感数据。
下面是一个代码示例，该示例来自CSDN
https://blog.csdn.net/JENREY/article/details/132009995
'''
import sys


logger = logging.getLogger("example")
logger.setLevel(logging.DEBUG)

# Create handlers for logging to the standard output and a file
stdoutHandler = logging.StreamHandler(stream=sys.stdout)
errHandler = logging.FileHandler("error.log")

# Set the log levels on the handlers
stdoutHandler.setLevel(logging.DEBUG)
errHandler.setLevel(logging.ERROR)

# Create a log format using Log Record attributes
fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
)

# Set the log format on each handler
stdoutHandler.setFormatter(fmt)
errHandler.setFormatter(fmt)

# Add each handler to the Logger object
logger.addHandler(stdoutHandler)
logger.addHandler(errHandler)

logger.info("Server started listening on port 8080")
logger.warning(
    "Disk space on drive '/var/log' is running low. Consider freeing up space"
)

try:
    raise Exception("Failed to connect to database: 'my_db'")
except Exception as e:
    # exc_info=True ensures that a Traceback is included
    logger.error(e, exc_info=True)


'''
执行上面的程序时，控制台会打印出日志信息
同时还创建了 error.log 文件，该文件应仅包含 ERROR 日志，因为 errHandler 的最小级别已设置为 ERROR

'''


'''
除了Python自带的库以外，还有一些第三方库，下面是一些库
python-json-logger
loguru
Structlog
Eliot
Logbook
Picologging
'''
