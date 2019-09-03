#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/2 20:04
# @Author:Michelle Yang
# @File  :people.py
from project.python_camp_note.Stage3.stage3_hw.db import operate_file

users_info = operate_file.load_users_info()


# users_info = None


class People(object):
    def __init__(self, name=None, pwd=None, role='student'):
        self.name = name
        self.pwd = pwd
        self.role = role


class Student(People):
    # 注册
    def __init__(self, name, pwd, role):
        super(Student, self).__init__(name, pwd)
        self.school = ' '
        self.course = []
        self.score = []

    def save_dic(self):
        return {'name': self.name, 'pwd': self.pwd, 'school': self.school, 'role': self.role, 'course': self.course,
                'score': self.score}


class Teacher(People):
    def __init__(self, name, pwd, school, role='teacher'):
        super(Teacher, self).__init__(name, pwd, role)
        self.school = school
        self.course = []

    def save_dic(self):
        return {'name': self.name, 'pwd': self.pwd, 'school': self.school, 'role': self.role, 'course': self.course}


class Manager(People):
    def __init__(self, name, pwd, role='manager'):
        super(Manager, self).__init__(name, pwd, role)

    def save_dic(self):
        return {'name': self.name, 'pwd': self.pwd, 'role': self.role}
