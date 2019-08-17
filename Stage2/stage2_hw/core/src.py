#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/17 13:49
# @Author:Michelle Yang
# @File  :src.py
from python_camp_note.Stage2.stage2_hw.lib.common import signup, login, exit_
from python_camp_note.Stage2.stage2_hw.lib.common import withdraw_cash, consume, repay, lift_amount, exit_2
from python_camp_note.Stage2.stage2_hw.conf import settings

# [{"name": "michelle", "pwd": "michelle123", "money": 88560, "black": 0}]
login_func_dict = {
    '1': signup,
    '2': login,
    '0': exit_,
}

func_dict = {
    '0': exit_2,
    '1': withdraw_cash,
    '2': consume,
    '3': repay,
    '4': lift_amount
}


def main():
    print('欢迎光临该电子商城：')
    ###########登陆/注册功能############
    while True:
        print("""
            1 注册
            2 登陆
            0 退出
            """)
        choice = input('输入您的选择>>:').strip()
        if choice in login_func_dict:
            ret = login_func_dict[choice]()
            if int(choice) == 2:
                if ret != 2:
                    print(ret)
                    global user
                    user = settings.User(name=ret['name'], pwd=ret['pwd'], money=ret['money'])
                    break

        else:
            print('非法操作')

    ############登陆成功，可以进行更多的操作#######
    while True:
        print("""
                    1 取现
                    2 消费
                    3 还款
                    4 提额
                    0 退出
                    """)
        choice = input('输入您的选择>>:').strip()
        if choice in func_dict:
            func_dict[choice](user)
        else:
            print('非法操作')


if __name__ == '__main__':
    main()
