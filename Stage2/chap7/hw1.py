#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/16 10:47
# @Author:Michelle Yang
# @File  :hw1.py
################################作业说明##########################
"""
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。要求：登录成功一次，后续的函数都无需再输入用户名和密码。
注意：从文件中读出字符串形式的字典，可以用以下方式把字典字符串转化成字符串。eval('{"name":"albert","password":"123"}')
"""
import os


def auth(filepath):
    def user_auth(func):
        users_pwd_dict = {}

        def wrapper(*args, **kwargs):
            global current_user
            # 加载用户名和密码
            if not os.path.exists(filepath):
                print('不存在该文件，再见')
                return
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = eval(line)  # 转化成字典形式
                    user = line['name']
                    pwd = line['password']
                    users_pwd_dict[user] = pwd
            #  登录过无需登录
            if current_user['username']:
                res = func(*args, **kwargs)
                return res
            # 没有登录首先登录
            while True:
                name = input('用户名>>:').strip()
                pwd = input('密码>>:').strip()
                if name in users_pwd_dict and users_pwd_dict[name] == pwd:
                    print("登录成功")
                    current_user['username'] = name
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('用户名或者密码错误！')

        return wrapper

    return user_auth


@auth('./user_info.txt')
def home():
    print('welcome to home page!')


@auth('./user_info.txt')
def shop():
    print('welcome to shop page!')


@auth('./user_info.txt')
def recommend():
    print('welcome to recommend page!')


if __name__ == '__main__':
    current_user = {
        'username': None,
    }
    home()
    shop()
    recommend()
