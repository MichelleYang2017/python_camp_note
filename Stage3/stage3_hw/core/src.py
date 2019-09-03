#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/27 13:49
# @Author:Michelle Yang
# @File  :src.py
from project.python_camp_note.Stage3.stage3_hw.core.people import Student, Teacher, Manager
from project.python_camp_note.Stage3.stage3_hw.db import operate_file
from project.python_camp_note.Stage3.stage3_hw.lib.common import register, login, choose_school, choose_course, \
    check_score, exit_, check_student, check_course, modify_score, create_school, create_teacher

users_info = operate_file.load_users_info()



student_func_dict = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
    '0': exit_,
}

teacher_func_dict = {
    '1': login,
    '2': choose_course,
    '3': check_course,
    '4': check_student,
    '5': modify_score,
    '0': exit_,
}

manager_func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '0': exit_,
}


def main():
    print('欢迎光临操作管理系统：')
    ##################选择登陆/注册的角色##############
    while True:
        print("""
            1 学生
            2 讲师
            3 管理员
            0 退出
            """)
        choice = input('输入您的选择>>:').strip()
        if choice in ['1', '2', '3']:
            break
        elif choice == '0':
            print('您准备退出该系统，再见！')
            exit(0)
        else:
            print('非法操作')

    #######################根据登陆/注册的角色执行相应的功能##############
    choices = ['1', '2', '3', '4', '5', '0']
    if choice == '1':
        obj = None
        while True:
            print(""" 请选择如下操作的一个：
                1 注册
                2 登陆
                3 选择学校
                4 选择课程
                5 查看分数
                0 退出登陆
            """)
            choice = input('输入您的选择>>:').strip()
            if choice in choices:
                if int(choice) == 1:
                    student_func_dict[choice]()
                elif int(choice) == 2:
                    obj = student_func_dict[choice](role='student')
                elif obj != 2 and obj:
                    student_func_dict[choice](obj)
                else:
                    print('请先登录')
            else:
                print('非法输入')
    elif choice == '2':
        obj = None
        while True:
            print("""
               1 登陆
               2 选择课程
               3 查看课程
               4 查看学生
               5 修改分数
               0 退出登陆
                       """)
            choice = input('输入您的选择>>:').strip()
            if choice in choices:
                if choice == '1':
                    obj = teacher_func_dict[choice](role='teacher')
                elif obj != 2 and obj:
                    teacher_func_dict[choice](obj)
                else:
                    print('请先登录')
            else:
                print('非法输入')

    elif choice == '3':
        obj = None
        while True:
            print("""
               1 注册
               2 登陆
               3 创建学校和课程
               4 创建老师
               0 退出登陆
                       """)
            choice = input('输入您的选择>>:').strip()
            if choice in ['1', '2', '3', '4', '0']:
                if choice == '1':
                    manager_func_dict[choice](role='manager')
                elif choice == '2':
                    obj = manager_func_dict[choice](role='manager')
                elif obj != 2 and obj:
                    manager_func_dict[choice](obj)
                else:
                    print('请先登录！')
            else:
                print('非法输入')


if __name__ == '__main__':
    main()
