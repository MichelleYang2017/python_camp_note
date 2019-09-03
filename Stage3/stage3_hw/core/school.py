#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/1 22:45
# @Author:Michelle Yang
# @File  :school.py
class Course(object):
    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price


class School(object):
    # 创建学校
    def __init__(self, school_name, school_place):
        self.school_name = school_name
        self.school_place = school_place
        self.course_name = []
        self.course_time = []
        self.course_price = []

    # 创建课程
    def create_course(self, name, time, price):
        self.course_name.append(name)
        self.course_time.append(time)
        self.course_price.append(price)

    def save_dic(self):
        return {'school_name': self.school_name, 'school_place': self.school_place, 'course_name': self.course_name,
                'course_time': self.course_time, 'course_price': self.course_price}
