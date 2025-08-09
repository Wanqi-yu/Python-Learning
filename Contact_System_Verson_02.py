#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/8/5 14:09
# @Author : wanqi.yu
# @File : Contact_System_Verson_02.py.py
# @Software: PyCharm

'''
面向对象实现的通讯录管理系统
'''
import csv
import os
import re


class Contact:
    """联系人实体类"""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

    def to_dict(self):
        """转换为字典格式"""
        return {'姓名': self.name, '手机号': self.phone}


class AddressBook:
    """通讯录管理类"""

    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = []
        self._load_contacts()

    def _load_contacts(self):
        """从CSV文件加载联系人"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8-sig') as csvfile:
                    reader = csv.DictReader(csvfile)
                    self.contacts = [Contact(row['姓名'], row['手机号']) for row in reader]
            else:
                # 创建新文件并写入表头
                with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=['姓名', '手机号'])
                    writer.writeheader()
        except Exception as e:
            print(f"加载联系人失败: {e}")
            self.contacts = []

    def _save_contacts(self):
        """保存联系人到文件"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['姓名', '手机号'])
                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow(contact.to_dict())
            return True
        except Exception as e:
            print(f"保存联系人失败: {e}")
            return False

    def _validate_phone(self, phone):
        """验证手机号格式"""
        # 简单的手机号验证：1开头的11位数字
        return re.match(r'^1\d{10}$', phone) is not None

    def _find_contact(self, name):
        """查找联系人，返回索引和联系人对象"""
        for idx, contact in enumerate(self.contacts):
            if contact.name == name:
                return idx, contact
        return -1, None

    def add_contact(self, name, phone):
        """添加联系人"""
        if not name:
            return "姓名不能为空"

        _, existing = self._find_contact(name)
        if existing:
            return f"联系人 '{name}' 已存在"

        if not self._validate_phone(phone):
            return "手机号格式不正确，请输入11位数字（以1开头）"

        self.contacts.append(Contact(name, phone))
        if self._save_contacts():
            return f"联系人 '{name}' 添加成功"
        return "添加联系人失败，请重试"

    def delete_contact(self, name):
        """删除联系人"""
        if not name:
            return "姓名不能为空"

        idx, contact = self._find_contact(name)
        if contact:
            self.contacts.pop(idx)
            if self._save_contacts():
                return f"联系人 '{name}' 已删除"
            return "删除联系人失败，请重试"
        return f"未找到联系人: {name}"

    def update_contact(self, name, new_phone):
        """修改联系人手机号"""
        if not name:
            return "姓名不能为空"

        idx, contact = self._find_contact(name)
        if not contact:
            return f"未找到联系人: {name}"

        if not self._validate_phone(new_phone):
            return "手机号格式不正确，请输入11位数字（以1开头）"

        contact.phone = new_phone
        if self._save_contacts():
            return f"联系人 '{name}' 已更新"
        return "更新联系人失败，请重试"

    def search_contact(self, name):
        """查询联系人"""
        if not name:
            return "姓名不能为空"

        _, contact = self._find_contact(name)
        if contact:
            return f"联系人: {contact.name}, 电话: {contact.phone}"
        return f"未找到联系人: {name}"

    def display_all_contacts(self):
        """显示所有联系人"""
        if not self.contacts:
            return "通讯录为空"

        result = ["\n所有联系人:", "-" * 30]
        for idx, contact in enumerate(self.contacts, 1):
            result.append(f"{idx}. {contact}")
        result.append("-" * 30)
        result.append(f"共 {len(self.contacts)} 个联系人")
        return "\n".join(result)

    def export_contacts(self, filename=None):
        """导出联系人到CSV"""
        if not self.contacts:
            return "通讯录为空，无需导出"

        filename = filename or "contacts_export.csv"
        if not filename.endswith('.csv'):
            filename += '.csv'

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['姓名', '手机号'])
                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow(contact.to_dict())
            return f"成功导出 {len(self.contacts)} 个联系人到 {os.path.abspath(filename)}"
        except Exception as e:
            return f"导出失败: {str(e)}"

    def get_contact_count(self):
        """获取联系人数量"""
        return len(self.contacts)


class AddressBookSystem:
    """通讯录系统界面类"""

    def __init__(self):
        self.address_book = AddressBook()
        self.menu_options = {
            '1': self.add_contact,
            '2': self.delete_contact,
            '3': self.update_contact,
            '4': self.search_contact,
            '5': self.display_all_contacts,
            '6': self.export_contacts,
            '7': self.exit_system
        }

    def display_menu(self):
        """显示主菜单"""
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

    def run(self):
        """运行系统主循环"""
        print("\n欢迎使用通讯录管理系统!")
        print(f"当前通讯录中有 {self.address_book.get_contact_count()} 个联系人")

        while True:
            self.display_menu()
            choice = input("请选择操作 (1-7): ").strip()

            if choice in self.menu_options:
                self.menu_options[choice]()
            else:
                print("无效选择，请输入1-7之间的数字！")

    def add_contact(self):
        """添加联系人操作"""
        print("\n【添加联系人】")
        name = input("请输入联系人姓名: ").strip()
        phone = input("请输入手机号: ").strip()
        result = self.address_book.add_contact(name, phone)
        print(result)

    def delete_contact(self):
        """删除联系人操作"""
        print("\n【删除联系人】")
        name = input("请输入要删除的联系人姓名: ").strip()
        result = self.address_book.delete_contact(name)
        print(result)

    def update_contact(self):
        """修改联系人操作"""
        print("\n【修改联系人】")
        name = input("请输入要修改的联系人姓名: ").strip()
        new_phone = input("请输入新的手机号: ").strip()
        result = self.address_book.update_contact(name, new_phone)
        print(result)

    def search_contact(self):
        """查询联系人操作"""
        print("\n【查询联系人】")
        name = input("请输入要查询的联系人姓名: ").strip()
        result = self.address_book.search_contact(name)
        print(result)

    def display_all_contacts(self):
        """显示所有联系人操作"""
        print("\n【所有联系人】")
        result = self.address_book.display_all_contacts()
        print(result)

    def export_contacts(self):
        """导出联系人操作"""
        print("\n【导出联系人】")
        filename = input("请输入导出文件名 (默认: contacts_export.csv): ").strip()
        result = self.address_book.export_contacts(filename or None)
        print(result)

    def exit_system(self):
        """退出系统"""
        print("\n正在退出系统...")
        print("感谢使用通讯录管理系统！")
        exit()


if __name__ == "__main__":
    system = AddressBookSystem()
    system.run()