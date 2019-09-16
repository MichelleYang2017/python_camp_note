#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/16 19:41
# @Author:Michelle Yang
# @File  :user_choice.py
from project.python_camp_note.Stage4.stage4_hw.lib.common import User, File
from project.python_camp_note.Stage4.stage4_hw.db.operate_file import load_file, save_file
import os
user_list = load_file()
names_list = []
pwd_list = []
login_list = []
for user in user_list:
    names_list.append(user.name)
    pwd_list.append(user.pwd)
    login_list.append(user.login)


def signup():
    global user_list
    name = input('请输入注册的用户名：').strip()
    if name not in names_list:
        pwd = input('请输入密码:').strip()
        user_list.append(User(name, pwd))
    else:
        print('该用户名已经被注册！')


def auth(func):
    """
    验证是否登陆
    :param func:
    :return:
    """

    def wrapper(user):
        if user.name in user_list:
            if user_list[user_list.index(user.name)].login == 1:
                res = func(user)
                return res
        global user_list
        name = input('请输入登陆的用户名：').strip()
        pwd = input('请输入密码:').strip()
        if name in names_list and (names_list.index(name) == pwd_list.index(pwd)):
            user_list[names_list.index(name)].login = 1
            res = func(user_list[names_list.index(name)])
        else:
            print('用户名或密码输入错误！')

    return wrapper


@auth
def uploadfile():
    file_path = input('请输入上传的文件路径：').strip()
    if not os.path.exists(file_path):
        print('文件不存在！')
        return




def login():
    global user_list
    name = input('请输入登陆的用户名：').strip()
    pwd = input('请输入密码:').strip()
    if name in names_list and (names_list.index(name) == pwd_list.index(pwd)):
        user_list[names_list.index(name)].login = 1
        return user_list[names_list.index(name)]
    else:
        print('用户名或密码输入错误！')
        return None


def exit_(conn):
    print('下次再见！')
    save_file(user_list)
    exit(0)


