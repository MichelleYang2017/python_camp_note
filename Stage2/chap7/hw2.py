#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/16 11:11
# @Author:Michelle Yang
# @File  :hw2.py

######################################作业说明########################
"""编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录"""
import os
import time


def auth(filepath):
    def user_auth(func):
        users_pwd_dict = {}

        def wrapper(*args, **kwargs):
            global current_user
            # 先将文件中的用户名和密码取出来
            if not os.path.exists(filepath):
                print('不存在该文件，再见')
                return
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = eval(line)  # 转化成字典形式
                    user = line['name']
                    pwd = line['password']
                    users_pwd_dict[user] = pwd
            while True:
                # 判断是否登录且有没有超时
                if current_user['username'] and time.time() - current_user['usertime'] < time_out:
                    break
                elif current_user['username'] and time.time() - current_user['usertime'] >= time_out:
                    print('登录已超时，请重新登录')
                # 没有登录或者超时需要重新登录
                name = input('用户名>>:').strip()
                pwd = input('密码>>:').strip()
                if name in users_pwd_dict and users_pwd_dict[name] == pwd:
                    print("登录成功")
                    current_user['username'] = name
                    current_user['usertime'] = time.time()
                    break
                else:
                    print('用户名或者密码错误！')
            res = func(*args, **kwargs)
            return res

        return wrapper

    return user_auth


@auth('./user_info.txt')
def home():
    time.sleep(4)
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
        'usertime': None
    }
    time_out = 3
    home()
    shop()
    recommend()
