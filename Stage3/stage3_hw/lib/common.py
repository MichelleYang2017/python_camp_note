#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/27 13:48
# @Author:Michelle Yang
# @File  :common.py
from project.python_camp_note.Stage3.stage3_hw.db import operate_file
from project.python_camp_note.Stage3.stage3_hw.conf import settings
from project.python_camp_note.Stage3.stage3_hw.core.people import Student, Teacher, Manager
from project.python_camp_note.Stage3.stage3_hw.core.school import School

users_info = operate_file.load_users_info()
log = settings.Log()
schools_info = operate_file.load_school_info()



def register(role='student'):
    """注册功能
    :return:
    """
    global users_info
    obj = None
    while True:
        name = input('请输入用户名>>').strip()
        if users_info is not None:
            user_names = [user for user in users_info.keys()]
            if name in user_names:
                print('该用户名已注册，请重新注册！')
                continue
        pwd = input('请输入密码>>').strip()
        if role == 'student':
            obj = Student(name, pwd, role)
            users_info[name] = obj.save_dic()
            break
        elif role == 'manager':
            obj = Manager(name, pwd, role)
            users_info[name] = obj.save_dic()
            break
        else:
            print('非法输入呢！')
    return obj


def login(role='student'):
    """登陆功能
    :return:
    """
    global users_info
    num_try = 5
    user_names = [user for user in users_info.keys()]
    while True:
        name = input('请输入用户名>>').strip()
        if name not in user_names:
            print('该用户名没有注册！')
            return 2
        # 查看密码是否正确
        else:
            while num_try:
                pwd = input('请输入密码>>').strip()
                for key in users_info:
                    if name == users_info[key]['name'] and pwd == users_info[key]['pwd']:
                        if users_info[key]['role'] == role:
                            return users_info[key]
                        else:
                            print('请检查您的身份，重新登录！')
                            return None
                num_try -= 1
                print('密码输入错误，请重新输入！')
            print('抱歉试用机会已经用完，再见')
            return None


def exit_(user):
    """退出功能
    :return:
    """
    print('{} 欢迎下次光临！' % (user))
    operate_file.dump_users_info(users_info)
    operate_file.dump_school_info(schools_info)
    return exit(0)


def choose_school(user):
    """学生选择学校
    :return:
    """
    while True:
        schools_list = schools_info.keys()
        while True:
            print('有如下学校：', list(schools_info.keys()))
            # print('有如下学校供你选择：')
            # for (name, time, price) in zip(schools_info['school_name'], schools_info['school_time'],
            #                                schools_info['school_place']):
            #     print('course name:', name, '\t course time:', time, '\t course price:', price)
            school = input('请输入学校>>').strip()
            if school in schools_list:
                user['school'] = school
                log.debug('debug')
                log.info("{}用户选择：{}学校".format(user['name'], school))
                return user
            else:
                print('输入有误，请重新输入！')


def choose_course(user):
    """学生选择课程
    :return:
    """
    school_info_c, school_info_t, school_info_p = [], [], []
    for school in schools_info:
        if school == user['school']:
            print('hi:', schools_info[school])
            school_info_c.append(schools_info[school]['course_name'])
            school_info_t.append(schools_info[school]['course_time'])
            school_info_p.append(schools_info[school]['course_price'])
    # school_info = schools_info[user['school']]
    while True:
        idx = 0
        for (name, time, price) in zip(school_info_c, school_info_t,
                                       school_info_p):
            print('课程索引', idx, '\t course name:', name, '\t course time:', time, '\t course price:', price)
            idx += 1

        choice = input('请输入您想要选择的课程索引,按q随时退出，如1:').strip()
        if choice.isdigit():
            if int(choice) not in [i for i in range(0, idx + 1)]:
                print("不存在该课程！")
            else:
                course = school_info_c[int(choice)]
                print(users_info, user)
                users_info[user['name']]['course'].append(course[0])
                users_info[user['name']]['score'].append(0)
                log.debug('debug')
                log.info("{}学生选择：{}课程".format(user, course[0]))
        elif choice == 'q':
            break
        else:
            print("错误输入！")
    return user


def check_score(user):
    print('%s 的成绩如下：' % user)
    for (subject, score) in zip(user['course'], user['score']):
        print('科目：', subject, '\t 成绩：', score)
    log.debug('debug')
    log.info("{}用户查看成绩".format(user['name']))


def check_course(user):
    print('%s 讲师的课程如下：' % user['name'])
    course_name = []
    course_time = []
    course_price = []
    print(user['course'])
    for subject in user['course']:
        print(schools_info, subject)
        course_name.append(subject)
        course_time.append(schools_info[subject]['course_time'])
        course_price.append(schools_info[subject]['course_price'])
    for (subject, time, price) in zip(course_name, course_time, course_price):
        print('科目：', subject, '\t 时长：', time, '\t 价格：', course_price)
    log.debug('debug')
    log.info("{}讲师查看课程".format(user))


def check_student(user):
    students = {}
    for name in users_info.keys():
        role = users_info[name]['role']
        if role == 'student':
            students[name] = users_info[name]
    for key in students:
        print("学生姓名：", key, end='\t')

    log.debug('debug')
    log.info("{}讲师查看学生".format(user['name']))


def modify_score(user):
    global users_info
    print('学生如下：')
    check_student(user)
    name = input('请输入你想要修改的学生姓名：').strip()

    if name in users_info:
        subject = input('请输入你想要修改的科目:').strip()
        if subject in users_info[name]['course']:
            index = users_info[name]['course'].index(subject)
            print(index)
            score = input('请输入你想要修改的分数:').strip()
            users_info[name]['score'][index] = score
            log.debug('debug')
            log.info("{}讲师修改学生成绩".format(user['name']))
        else:
            print('该科目学生没有选')

    else:
        print('该学生不存在')


def create_school(user):
    global schools_info
    while True:
        school_name = input('输入学校的名字：').strip()
        if school_name in schools_info:
            print('该学校名字已存在，请重新输出')
        else:
            break
    school_place = input('输入学校的地点：').strip()
    school_ = School(school_name, school_place)
    schools_info[school_name] = school_
    while True:
        course_name = input('请输入课程名称：').strip()
        course_time = input('请输入课程周期：').strip()
        course_price = input('请输入课程价格：').strip()
        school_.create_course(course_name, course_time, course_price)
        choice = input('请选择是否继续添加课程？输入c继续').strip()
        if choice != 'c':
            break
    schools_info[school_name] = school_.save_dic()
    log.debug('debug')
    log.info("{}管理员创建学校并创建课程".format(user['name']))


def create_teacher(user):
    global users_info
    while True:
        teacher_name = input('输入教师的名字：').strip()
        if teacher_name in users_info.keys():
            print('该教师已存在，请重新输出！')
        else:
            break
    teacher_pwd = input('输入教师登陆的密码：').strip()

    while True:
        teacher_school = input('输入教师工作学校：').strip()
        if teacher_school in schools_info.keys():
            break
    teacher = Teacher(teacher_name, teacher_pwd, teacher_school)
    users_info[teacher_name] = teacher.save_dic()
    log.debug('debug')
    log.info("{}管理员创建老师".format(user['name']))


