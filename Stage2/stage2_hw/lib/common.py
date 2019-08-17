#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/17 13:48
# @Author:Michelle Yang
# @File  :common.py
from python_camp_note.Stage2.stage2_hw.bin.start import load_user_info
from python_camp_note.Stage2.stage2_hw.conf import settings
import json

user_info = load_user_info()
config = settings.Configuration()
log = settings.Log()


def signup():
    """注册功能
    :return:
    """
    global user_info
    user_dict = {}
    while True:
        name = input('请输入用户名>>').strip()
        if user_info is not None:
            user_names = [user['name'] for user in user_info]
            if name in user_names:
                print('该用户名已注册，请重新注册！')
                continue
        pwd = input('请输入密码>>').strip()
        while True:
            wage = input('请输入银行卡余额：').strip()
            if wage.isdigit():
                break
        user = settings.User(name, pwd, money=wage, black=0)
        user_dict['name'] = user.name
        user_dict['pwd'] = user.pwd
        user_dict['money'] = user.money
        user_dict['black'] = user.black
        break
    with open(config.user_info_file, 'wt', encoding='utf-8') as f:
        if user_info:
            user_info.append(user_dict)
        else:
            user_info = [user_dict]
        json.dump(user_info, f)
    log.debug('debug')
    log.info("{}用户注册".format(name))


def login():
    """登陆功能
    :return:
    """
    global user_info
    num_try = 3
    user_names = [user['name'] for user in user_info]
    while True:
        name = input('请输入用户名>>').strip()
        if name not in user_names:
            print('该用户名没有注册！')
            return 2
        # 查看密码是否正确
        else:
            while num_try:
                pwd = input('请输入密码>>').strip()
                for i in range(len(user_info)):
                    if name == user_info[i]['name'] and pwd == user_info[i]['pwd']:
                        if user_info[i]['black'] == 0:
                            print('恭喜{}登陆成功'.format(name))
                            log.debug('debug')
                            log.info("{}用户登陆".format(name))
                            return user_info[i]
                        else:
                            print('不好意思，您之前密码填写错误超过3次，已被冻结！')
                            return 2
                num_try -= 1
                print('密码输入错误，请重新输入！')
            # 加入黑名单
            if name in user_names:
                for it in range(len(user_info)):
                    if user_info[it]['name'] == name:
                        user_info[it]['black'] = 1
                        log.debug('debug')
                        log.info("{}用户被加入黑名单".format(name))


def exit_():
    """退出功能
    :return:
    """
    print('欢迎下次光临！')
    return exit(0)


def exit_2(user):
    """退出功能
       :return:
       """
    print('您购买的商品如下:')
    print(user.basket)
    print('{},欢迎下次光临！'.format(user.name))
    dict_list = []
    with open(config.user_info_file, 'wt', encoding='utf-8') as f:
        for it in user_info:  # 字典
            if it["name"] == user.name:
                it['money'] = user.money
            dict_list.append(it)
        json.dump(dict_list, f)
    log.debug('debug')
    log.info("{}用户退出该系统".format(user.name))

    return exit(0)


def withdraw_cash(user):
    """提取现金
    :return:
    """
    while True:
        m = input('请输入取现的金额>>').strip()
        if m.isdigit():
            if int(m) > user.money:
                print('取现超过您的余额，请重新输入！')
                continue
            user.money -= int(m)
            print('银行卡取走{},余额为{}'.format(m, user.money))
            log.debug('debug')
            log.info("{}用户取现：{}".format(user.name, m))
            return user
        else:
            print('输入有误，请重新输入！')


def consume(user):
    """消费
    :return:
    """
    good_dict = {
        '1': {"iphone": 8000},
        '2': {'macbook': 10000},
        '3': {'bike': 1500},
        '4': {'banana': 10},
        '5': {'juice': 20}
    }
    money_comsume = 0
    while True:
        print("商品列表如下：")
        print(good_dict)
        choice = input('请输入您的商品选择,按q随时退出，如1:').strip()
        if choice.isdigit():
            if int(choice) not in [i for i in range(1, 6)]:
                print("不存在该商品！")
            else:
                price = 0
                good = ''
                for i in good_dict[choice]:
                    good = i
                    print(good)
                    price = int(good_dict[choice][i])
                if user.money < price:
                    print("工资不够，请重新选择商品:")
                else:
                    money_comsume += price
                    print("商品%s已经加入购物车，您的余额为:%s" % (good, str(int(user.money) - int(price))))
                    content = "id" + choice + ",good:" + good + ',price:', int(price)
                    user.money = user.money - price
                    user.basket.append(content)
                    log.debug('debug')
                    log.info("{}用户购买：{}，花费{}".format(user.name, good, price))
        elif choice == 'q':
            break
        else:
            print("不存在该商品！")
    return user


def repay(user):
    """还款
    :return:
    """
    while True:
        m = input('请输入还款金额>>').strip()
        if m.isdigit():
            if int(m) > user.money:
                print('还款超过您的余额，请重新输入！')
                continue
            user.money -= int(m)
            print('已还款{},余额为{}'.format(m, user.money))
            log.debug('debug')
            log.info("{}用户还款{}元".format(user.name, m))
            return user
        else:
            print('输入有误，请重新输入！')


def lift_amount(user):
    """提额
    :return:
    """
    while True:
        m = input('请输入提款金额>>').strip()
        if m.isdigit():
            user.money += int(m)
            print('已提款{},余额为{}'.format(m, user.money))
            log.debug('debug')
            log.info("{}用户提额{}元".format(user.name, m))
            return user
        else:
            print('输入有误，请重新输入！')
