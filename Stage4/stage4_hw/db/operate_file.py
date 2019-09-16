#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/16 19:53
# @Author:Michelle Yang
# @File  :operate_file.py
from project.python_camp_note.Stage4.stage4_hw.conf.config import user_txt
from project.python_camp_note.Stage4.stage4_hw.lib.common import User


def load_file():
    users_list = []
    with open(user_txt, 'r', encoding='utf-8') as f:
        for line in f:
            tmp = line.split('\n')[0].split('|')
            user = User(tmp[0], tmp[1], tmp[2])
            users_list.append(user)
    return users_list


def save_file(users_list):
    with open(user_txt, 'w', encoding='utf-8') as f:
        for user in users_list:
            f.write(user.name + '|' + user.pwd + '|' + str(user.login) + '\n')


if __name__ == '__main__':
    # save_file([])
    load_file()
