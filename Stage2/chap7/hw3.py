#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/16 11:44
# @Author:Michelle Yang
# @File  :hw3.py
#######################作业说明##########################
"""
编写日志装饰器，实现功能：一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定。
"""

import time


def logger(log_file):
    def logger_file(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write('本次函数执行时间为：%s 秒' % (end_time - start_time))
            return res

        return wrapper

    return logger_file


@logger('./home.txt')
def home():
    time.sleep(4)
    print('welcome to home page!')


@logger('./shop.txt')
def shop(str):
    time.sleep(1)
    print('welcome %s to shop page!' % str)


@logger('./recommend.txt')
def recommend(str):
    time.sleep(2)
    print('welcome %s to recommend page!' % str)


if __name__ == '__main__':
    home()
    shop('Michelle')
    recommend('Michelle')
