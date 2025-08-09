#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/8/4 13:58
# @Author : wanqi.yu
# @File : Day_26-27_optimized.py
# @Software: PyCharm

'''
优化版通讯录管理系统
'''
import csv
import os

CONTACTS_FILE = 'contacts.csv'
contacts = []


# 文件初始化
def init_contacts():
    """初始化联系人数据"""
    global contacts
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                contacts = [dict(row) for row in reader]
        except Exception as e:
            print(f"读取文件错误: {e}")
            contacts = []
    else:
        # 创建新文件并写入表头
        with open(CONTACTS_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['姓名', '手机号'])
            writer.writeheader()
        contacts = []


def validate_phone(number):
    """验证手机号格式（简单验证）"""
    return number.isdigit() and 7 <= len(number) <= 15


def find_contact(name):
    """查找联系人，返回索引和联系人数据"""
    for idx, contact in enumerate(contacts):
        if contact['姓名'] == name:
            return idx, contact
    return -1, None


def add_contact():
    """添加联系人"""
    name = input("请输入联系人姓名: ").strip()
    if not name:
        print("姓名不能为空！")
        return

    _, existing = find_contact(name)
    if existing:
        print(f"联系人 '{name}' 已存在")
        return

    while True:
        number = input("请输入手机号: ").strip()
        if not number:
            print("手机号不能为空！")
            continue
        if not validate_phone(number):
            print("手机号格式不正确，请输入7-15位数字")
            continue
        break

    contacts.append({'姓名': name, '手机号': number})
    save_contacts()
    print(f"联系人 '{name}' 添加成功")


def delete_contact():
    """删除联系人"""
    name = input('请输入要删除的联系人姓名: ').strip()
    if not name:
        print("姓名不能为空！")
        return

    idx, contact = find_contact(name)
    if contact:
        contacts.pop(idx)
        save_contacts()
        print(f"联系人 '{name}' 已删除")
    else:
        print(f"未找到联系人: {name}")


def update_contact():
    """修改联系人"""
    name = input("请输入要修改的联系人姓名: ").strip()
    if not name:
        print("姓名不能为空！")
        return

    idx, contact = find_contact(name)
    if not contact:
        print(f"未找到联系人: {name}")
        return

    while True:
        new_number = input("请输入新的手机号: ").strip()
        if not new_number:
            print("手机号不能为空！")
            continue
        if not validate_phone(new_number):
            print("手机号格式不正确，请输入7-15位数字")
            continue
        break

    contacts[idx]['手机号'] = new_number
    save_contacts()
    print(f"联系人 '{name}' 已更新")


def search_contact():
    """查询联系人"""
    name = input('请输入要查询的联系人姓名: ').strip()
    if not name:
        print("姓名不能为空！")
        return

    _, contact = find_contact(name)
    if contact:
        print(f"\n联系人: {contact['姓名']}, 电话: {contact['手机号']}")
    else:
        print(f"未找到联系人: {name}")


def display_all_contacts():
    """显示所有联系人"""
    if not contacts:
        print("\n通讯录为空")
        return

    print("\n所有联系人:")
    print("-" * 30)
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['姓名']}: {contact['手机号']}")
    print("-" * 30)
    print(f"共 {len(contacts)} 个联系人")


def save_contacts():
    """保存联系人到文件"""
    try:
        with open(CONTACTS_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['姓名', '手机号'])
            writer.writeheader()
            writer.writerows(contacts)
    except Exception as e:
        print(f"保存文件失败: {e}")


def export_contacts():
    """导出联系人到CSV"""
    if not contacts:
        print("通讯录为空，无需导出")
        return

    filename = input("请输入导出文件名 (默认: contacts.csv): ").strip() or "contacts.csv"
    if not filename.endswith('.csv'):
        filename += '.csv'

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['姓名', '手机号'])
            writer.writeheader()
            writer.writerows(contacts)
        print(f"成功导出 {len(contacts)} 个联系人到 {os.path.abspath(filename)}")
    except Exception as e:
        print(f"导出失败: {str(e)}")


def display_menu():
    """显示菜单"""
    print("\n" + "=" * 30)
    print("     通讯录管理系统")
    print("=" * 30)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 修改联系人")
    print("4. 查询联系人")
    print("5. 显示所有联系人")
    print("6. 导出联系人")
    print("7. 退出系统")
    print("=" * 30)


# 初始化联系人数据
init_contacts()

# 主程序
while True:
    display_menu()
    choice = input("请选择操作 (1-7): ").strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_all_contacts()
    elif choice == '6':
        export_contacts()
    elif choice == '7':
        print("正在退出系统...")
        break
    else:
        print("无效选择，请输入1-7之间的数字！")

print("系统已退出")