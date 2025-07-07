#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/5 7:56
# @Author : wanqi.yu
# @File : Practice_week_02.py
# @Software: PyCharm
'''
每周六进行简单练习
#### **第2周：流程控制（引入基础函数）**
1. **成绩转换函数**
   - 函数名：`convert_score(percent)`
   - 功能：将百分制分数转换为等级制（≥90→A, ≥80→B, ≥70→C, 其他→D）

2. **交通信号决策器**
   - 函数名：`traffic_decision(color, vehicle_type)`
   - 功能：根据信号灯颜色（"红"/"绿"/"黄"）和车辆类型（"汽车"/"行人"）返回能否通行
   - 输出规则:
    - 汽车:绿灯行，红灯/黄灯停
    - 行人:绿灯行,红灯停,黄灯警告
**练习3（扩展）：紧急通行系统**
要求：
- 扩展 `traffic_decision` 函数
- 新增车辆类型："救护车"/"消防车"
- 规则：紧急车辆在任何信号灯下均可通行
- 示例：`traffic_decision("红", "救护车")` 返回 "允许通行

'''

'''
1.成绩转换器
'''
def convert_score(percent):
    '''
    计算成绩信息，转换成等级
    :param percent:
    :return: 返回等级信息
    '''
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    else:
        return 'D'
score = int(input('请输入你的成绩:'))
print(convert_score(score))

'''
2.交通信号决策器
'''
def traffic_decision(color, vehicle_type):
    '''
    根据信号灯颜色返回能否通行
    :param color: 交通信号灯当前颜色
    :param vehicle_type:
    :return: 返回能否通过
    '''
    if vehicle_type == 'car':
        if color == 'red':
            return "停止"
        elif color == 'green':
            return "通行"
        elif color == 'yellow':
            return "停止"
    elif vehicle_type == 'men':
        if color == 'red':
            return "停止"
        elif color == 'green':
            return "通行"
        elif color == 'yellow':
            return "警告:信号灯即将变红，请勿通过"

vehicle = input('请输入类型')
color = input('信号灯颜色')
print(traffic_decision(color, vehicle))
'''
3.交通信号灯扩展
'''
def traffic_02(color, vehicle_type,car_type='ordinary'):
    '''
    根据信号灯颜色返回能否通行
    :param color: 交通信号灯当前颜色
    :param vehicle_type:
    :return: 返回能否通过
    '''
    if car_type == 'ordinary':
        if vehicle_type == 'car':
            if color == 'red':
                return "停止"
            elif color == 'green':
                return "通行"
            elif color == 'yellow':
                return "停止"
        elif vehicle_type == 'men':
            if color == 'red':
                return "停止"
            elif color == 'green':
                return "通行"
            elif color == 'yellow':
                return "警告:信号灯即将变红，请勿通过"
    elif car_type == 'ambulance' or car_type == 'fire engine':
        return '通行'
vehicle = input('请输入类型')
color = input('信号灯颜色')
car_type = input('请输入车辆类型')
print(traffic_02(color, vehicle,car_type))
if __name__ == "__main__":
    run_code = 0
