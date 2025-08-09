#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/24 14:32
# @Author : wanqi.yu
# @File : Day_24.py
# @Software: PyCharm
'''
虚拟环境管理
Venv：虚拟环境，是Python用来创建和管理虚拟环境的模块，该模块供你用来存放你的Python脚本以及安装各种Python第三方模块，
模块里的环境和本机是完全分开的，也就是说你在venv下通过pip安装的Python第三方模块是不会存在于你本机的环境下的
虚拟环境的作用
Python的虚拟环境可以使一个Python程序拥有独立的库library和解释器interpreter，而不用与其他Python程序共享统一个library和interpreter。
虚拟环境的好处是避免了不同Python程序间的互相影响（共同使用global library 和 interpreter）
例如：程序A需要某个库的2.0版本，而程序B需要同样这个库的3.0版本，如果没有虚拟环境的话，我们本地只能有这个库的一种版本，如果程序B执行，
代表本地安装的3.0版本的库，A就不能成功执行了。

'''
if __name__ == "__main__":
    run_code = 0
