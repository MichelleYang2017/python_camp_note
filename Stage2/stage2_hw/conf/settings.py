#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/17 13:49
# @Author:Michelle Yang
# @File  :settings.py
import logging


class Configuration():
    def __init__(self):
        self.log_file_path = '../log/access.log'
        self.user_info_file = "../db/db.json"
        self.log_flie_path = '../log/access.log'


class User(object):
    def __init__(self, name, pwd, money=0, black=0, basket=[]):
        self.name = name
        self.pwd = pwd
        self.money = int(money)
        self.black = black
        self.basket = basket


def Log():
    config = Configuration()
    logging.basicConfig(
        filename=config.log_file_path,
        format='%(asctime)s - %(name)s -%(levelname)s - %(module)s-%(funcName)s : %(message)s',  # 控制日志的格式
        datefmt='%Y-%m-%d %H:%M:%S %p',  # 控制日志的格式
        level=20,
    )
    return logging
