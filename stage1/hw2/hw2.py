#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/7 13:10
# @Author:Michelle Yang
# @File  :hw2.py
"""需求：
    用户名：密码和密码存在文件中，格式为Albert|Albert123|3000
    启动程序后：
        已注册用户->先登录->登陆成功->读取用户余额->开始购物
                登陆过程中，用户名密码输入超过3次则退出程序
                并将用户名添加到黑名单，再次启动程序登陆该用户名，提示用户禁止登陆
        未注册用户->先注册->注册成功->输入用户工资，即为余额->开始购物
    允许用户根据商品编号购买商品，比如：
        1 iphone
        2 macbook
        3 bike
    用户选择商品后，检测余额是否足够，够直接扣款，修改文件中用户余额，不够就提醒，
    可随时退出，退出时，打印已购买商品和余额
"""


# 用户信息类
class UserInfo():
    def __init__(self, user_name, user_pwd, user_money):
        self.name = user_name
        self.pwd = user_pwd
        self.money = user_money
        self.shop_list = []
        self.consume = 0

    def shop_info(self, shop_list, consume):
        for it in shop_list:
            self.shop_list.append(it)
        self.consume += consume
        self.money -= consume
        return self.shop_list, self.consume


# 解决登陆时不存在该用户、注册时已存在用户的方法
def other_choices():
    while True:
        choose = input("请输入您的选择==>").strip()
        if choose.isdigit() and int(choose) == 0:
            signup()
            break
        elif choose.isdigit() and int(choose) == 1:
            login_shop()
            break
        else:
            print("输入不合法，请重新选择,注册别名请选择0，登陆请选择1")


# 登陆
def login_shop():
    global user
    try_num = 3
    user_input_name = input('请输入已注册的用户名==>').strip()
    if user_input_name in black_list:
        print("该用户被禁止登陆！！！")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        exist_flag = False  # 用户是否存在的标志
        pwd_flag = False  # 密码输入正确的标志
        for line in f:
            # 判断是否用户名是否存在
            line_user_name = line.split('|')[0]
            if line_user_name == user_input_name:
                exist_flag = True
                # 判断密码是否正确
                while try_num:
                    user_input_pwd = input('请输入您的密码==>').strip()
                    try_num -= 1
                    if user_input_pwd == line.split('|')[1]:
                        wage_user = float(line.split('|')[2])
                        pwd_flag = True

                        user = UserInfo(user_input_name, user_input_pwd, wage_user)
                        break
                else:
                    print('你输入密码有误，已经加入黑名单！您被迫重新做选择')
                    black_list.append(user_input_name)
                    f_black.write(user_input_name + '\n')
                    return
            if pwd_flag:
                break
        if not exist_flag:
            print("该用户不存在，注册别名请选择0，登陆请选择1")
            other_choices()


def shop():
    ##################登陆成功，可以购物了##############
    name, pwd, wage = user.name, user.pwd, user.money
    print("恭喜您，登陆成功，请选择商品")
    good_list = []
    consume = 0
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
                    price = good_dict[choice][i]
                if wage < price:
                    print("工资不够，请重新选择商品:")
                else:
                    consume += price
                    print("商品%s已经加入购物车，您的余额为:%s" % (good, str(wage - consume)))
                    content = "id", choice, "good：", good, 'price:', wage
                    good_list.append(content)

        elif choice == 'q':
            break
        else:
            print("不存在该商品！")
    return consume, good_list


# 注册
def signup():
    # 用户注册内容
    # 判断用户名是否存在或者注册
    while True:
        user_name = input("请输入姓名==>").strip()
        if user_name in all_user_list:
            print("该用户已注册!请重新输入，注册别名请选择0，登陆请选择1")
            other_choices()
            return
        else:
            break
    # 设置密码
    user_pwd = input("请输入密码==>").strip()
    # 接收用户输入的工资
    while True:
        user_wage = input('请输入工资==>').strip()
        if user_wage.isdigit():
            break
        else:
            print('工资输入不合法,重新输入')
    with open(file_path, 'a+', encoding='utf-8') as f:
        f.write(user_name + "|" + user_pwd + '|' + user_wage + '\n')
        all_user_list.append(user_name)


def main():
    #  主逻辑
    global good_dict, file_path, black_user, all_user_list, new_file_path, black_list, f_black
    good_dict = {
        '1': {"iphone": 8000},
        '2': {'macbook': 10000},
        '3': {'bike': 1500},
        '4': {'banana': 10},
        '5': {'juice': 20}
    }

    file_path = './user_info.txt'
    black_user = './black.txt'
    # 加载黑名单的人
    black_list = []
    with  open(black_user, 'r', encoding='utf-8') as f1:
        for line in f1:
            black_list.append(line.split('\n')[0])
    f_black = open(black_user, 'a+', encoding='utf-8')

    # 加载所有注册的用户
    all_user_list = []
    with  open(file_path, 'r', encoding='utf-8') as f1:
        for line in f1:
            name = line.split('|')[0]
            all_user_list.append(name)

    new_file_path = './new_user_info.txt'
    print(
        "欢迎光临该网站，请输入您的选择(例如1): "
    )
    global user
    user = None
    consume, shop_list = 0, []
    while True:
        choice = input("请选择 0 注册 1 登陆 2 购物 3退出==>").strip()
        if choice.isdigit():
            choice = int(choice)
            # 注册
            if choice == 0:
                signup()
            # 登陆
            elif choice == 1:
                login_shop()
            # 购物
            elif choice == 2:
                if not user:
                    print('请先登录！')
                else:
                    # 购物并更新用户信息
                    consume, shop_list = shop()
                    shop_list, consume = user.shop_info(shop_list, consume)
            # 退出
            elif choice == 3:
                if not user:
                    print("您购买的商品如下:")
                    for it in shop_list:
                        print(it)
                    print('您的余额为:', user.money - user.consume)
                    new_line = user.name + "|" + user.pwd + "|" + str(user.money - user.consume)
                    with open(file_path, 'r', encoding='utf-8') as f, open(new_file_path, 'w',
                                                                           encoding='utf-8') as f_new:
                        for line in f:
                            if line.split('|')[0] == user.name:
                                line = new_line
                            f_new.write(line)

                    print("再见！")
                    break
                else:
                    print('好可惜，没有带走一件商品，欢迎您下次光临')
                    break
            else:
                print("选择不合法，请重新选择！")
        else:
            print("选择不合法，请重新选择！")
    f_black.close()


if __name__ == '__main__':
    main()
