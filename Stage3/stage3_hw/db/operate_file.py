#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/2 19:54
# @Author:Michelle Yang
# @File  :operate_file.py
import pickle
from project.python_camp_note.Stage3.stage3_hw.conf import settings

config = settings.Configuration()


def load_users_info(filepath=config.user_filepath):
    try:
        f = open(filepath, 'rb')
        user_infos = pickle.load(f)
    except FileNotFoundError:
        user_infos = {}
    return user_infos


def dump_users_info(users_info, filepath=config.user_filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(users_info, f)


def load_school_info(filepath=config.school_file):
    try:
        f = open(filepath, 'rb')
        school_infos = pickle.load(f)
        f.close()
    except FileNotFoundError:
        school_infos = {}
    return school_infos


def dump_school_info(school_course, filepath=config.school_file):
    with open(filepath, 'wb') as f:
        pickle.dump(school_course, f)
    del school_course
