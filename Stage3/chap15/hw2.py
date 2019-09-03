#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/1 10:40
# @Author:Michelle Yang
# @File  :hw2.py

#################################homework2 #######################
"""
自定义一个Integer类
     -- 该类有个input方法，调用该方法一定会得到一个合法的数字(非数字为不合法，越界为不合法)
            ---- 如果是非数字不合法，需要打印不合法消息，然后用户需要重新输入
             -- 如输入'abc'，不合法消息就为：invalid literal for int() with base 10: 'abc'
            ---- 如果是越界不合法，需要打印不合法消息，然后用户需要重新输入
             -- 如输入'2147483648'，不合法消息就为：ErrorMsg：2147483648 - 越界
"""


class SlopOverError(BaseException):

    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self):
        return '%s:%s-越界' % (self.message, self.number)


class Interger(object):
    def verifySlopOver(self, num):
        if num < -2147483648 or num > 2147483647:
            print(SlopOverError(num, 'ErrorMsg'))
            return False
        return True

    def input(self):
        while True:
            value = input('请输入数字：').strip()
            try:
                value = int(value)
            except ValueError:
                print("invalid literal for int() with base 10: 'abc'")
                continue
            if not self.verifySlopOver(value):
                continue
            return value


if __name__ == '__main__':
    type_my = Interger()
    value = type_my.input()
    print('终于等到你', value)
