#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/25 12:12
# @Author:Michelle Yang
# @File  :hw7.py
########################homework 7###################
"""作业说明：
学生成绩管理系统：
    1.根据姓名查看学生所有成绩
    2.查看所有人的某学科成绩
    3.查看总平均分
    4.查看某人的某学科成绩
    5.根据姓名删除学生信息
增强版要求:
    1.首先编写json格式的数据文件
    2.将json数据解析后转化为学生对象在增删改查
"""


class Student(object):
    def __init__(self, name, math_score, english_score, computer_score):
        self.name = name
        self.math_score = math_score
        self.english_score = english_score
        self.computer_score = computer_score


class StudentScoreSystem(object):
    all_object = []

    # 系统添加学生
    def add_student(self, obj):
        StudentScoreSystem.all_object.append(obj)

    # 查看学生的所有科目成绩
    def student_score(self, name):
        if name not in [stu.name for stu in StudentScoreSystem.all_object]:
            print('没有该学生')
            return 0
        else:
            obj = None
            for obj in StudentScoreSystem.all_object:
                if obj.name == name:
                    break
            return obj

    # 查看所有人的某学科成绩
    def check_subject_score(self, subject):
        if subject not in ['math', 'english', 'computer']:
            print('不好意思，没有该科目的成绩！')
            return -1
        elif subject == 'math':
            return [obj.math_score for obj in StudentScoreSystem.all_object]
        elif subject == 'english':
            return [obj.english_score for obj in StudentScoreSystem.all_object]
        else:
            return [obj.computer_score for obj in StudentScoreSystem.all_object]

    # 查看某学科的平均分
    def check_avg_score(self, subject):
        if subject not in ['math', 'english', 'computer']:
            print('不好意思，没有该科目的成绩！')
            return -1
        num = len(StudentScoreSystem.all_object)
        score_list = self.check_subject_score(subject)
        avg_score = sum(score_list) / num
        print('该学科的平均成绩为:{}'.format(avg_score))

    # 查看某人的某学科成绩
    def check_student_score(self, name, subject):
        if name not in [stu.name for stu in StudentScoreSystem.all_object]:
            print('没有该学生')
            return 0
        if subject not in ['math', 'english', 'computer']:
            print('不好意思，没有该科目的成绩！')
            return 0
        else:
            obj, score = self.student_score(name), 0
            if subject == 'math':
                score = obj.math_score
            elif subject == 'english':
                score = obj.english_score
            else:
                score = obj.computer_score
            print("该学生{}的成绩:{}".format(name, score))

    # 根据姓名删除学生信息
    def del_information(self, name):
        for obj in StudentScoreSystem.all_object:
            if obj.name == name:
                StudentScoreSystem.all_object.remove(obj)
                print('该对象信息已经删除')
                return 0
        print('没有该对象信息！')
        return -1


if __name__ == '__main__':
    print('欢迎登陆学生成绩管理系统！')
    system = StudentScoreSystem()
    stu1 = Student('michelle', 100, 90, 90)
    stu2 = Student('alex', 100, 100, 95)
    stu3 = Student('lily', 80, 80, 90)
    system.add_student(stu1)
    system.add_student(stu2)
    system.add_student(stu3)
    while True:
        print("""
              1.根据姓名查看学生所有成绩
              2.查看所有人的某学科成绩
              3.查看某学科的平均分
              4.查看某人的某学科成绩
              5.根据姓名删除学生信息
              0.退出系统
              """)
        choice = input('输入您的选择>>:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                name = input("请输入姓名>>").strip()
                obj = system.student_score(name)
                print("该学生{}的数学成绩:{}，英语成绩:{}, 计算机科学的成绩{}".format(obj.name, obj.math_score, obj.english_score,
                                                                 obj.computer_score))
            elif choice == 2:
                subject = input('输入你想看的某学科>>').strip()
                score_list = system.check_subject_score(subject)
                print('所有成绩如下:', score_list)
            elif choice == 3:
                subject = input('输入你想看的某学科>>').strip()
                system.check_avg_score(subject)
            elif choice == 4:
                name = input("请输入姓名>>").strip()
                subject = input('输入你想看的某学科>>').strip()
                system.check_student_score(name, subject)
            elif choice == 5:
                name = input("请输入姓名>>").strip()
                system.del_information(name)
            elif choice == 0:
                print('再见')
                exit(0)
            else:
                print('错误输入！')
        else:
            print('错误输入')
