#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/17 11:22
# @Author:Michelle Yang
# @File  :hw.py
# ##########################作业1#####################
"""
1.文件内容如下，标题为：姓名，性别，年纪，薪资
abert male 18 3000
james male 38 30000
林志玲 female 28 20000
新垣结衣 female 28 10000
要求从文件中取出每一条记录放入列表中，列表的每个元素都是如下格式：
{'name':'albert','sex':'male','age':18, 'salary':3000}
"""
with open('info.txt', 'r', encoding='utf-8') as f:
    f_lines = f.readlines()
name_list = list(map(lambda x: x.split(' ')[0], f_lines))
sex_list = list(map(lambda x: x.split(' ')[1], f_lines))
age_list = list(map(lambda x: int(x.split(' ')[2]), f_lines))
salary_list = list(map(lambda x: int(x.split(' ')[-1]), f_lines))
info_list = []
for it in range(len(f_lines)):
    info_dict = {}
    info_dict['name'] = name_list[it]
    info_dict['sex'] = sex_list[it]
    info_dict['age'] = age_list[it]
    info_dict['salary'] = salary_list[it]
    info_list.append(info_dict)
print(info_list)
################################作业2################
"""
根据题目1得到的列表，取出薪资最高的人的信息
"""
highest_salary_info = sorted(info_list, key=lambda x: x['salary'])[-1]
print(highest_salary_info)
############################作业3####################
"""
根据题目1得到的得表，取出最年轻的人的信息
"""
youngest_salary_info = sorted(info_list, key=lambda x: x['age'])[0]
print(youngest_salary_info)
############################作业4####################
"""
根据题目1得到的列表，将每个人的信息中的名字映射成首字母大写的形式
"""
import copy

new_name = list(map(lambda x: x['name'].capitalize(), info_list))
info_list_ = copy.deepcopy(info_list)
for it in range(len(info_list)):
    info_list_[it]['name'] = new_name[it]
print(info_list_)
############################作业5####################
"""
根据题目1得到的列表，过滤掉名字以a开头的人的信息
"""
info_list_filter = list(filter(lambda x: not x['name'].startswith('a'), info_list))
print(info_list_filter)
############################作业6####################
"""
使用递归打印斐波那契数列
"""


def fib(num):
    if num < len(num_list):
        return num_list[num]
    else:
        return fib(num - 2) + fib(num - 1)


def main():
    global num_list
    num_list = [0, 1]
    while True:
        num = input('输入您想查看的项>>:').strip()
        if num.isdigit():
            num = int(num)
            break
        else:
            print('输入不正确')
    it = 2
    while it < num:
        num_list.append(fib(it))
        it += 1
    print(num_list[:num])


main()
############################作业7####################
"""
使用random模块写一个随机生成8位验证码的程序，验证码中有随机大小写字母和数字
"""

import random

###小写字母
w_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
w_list.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])  # 添加大写字母
w_list.extend([str(i) for i in range(0, 10)])  # 添加数字
pwd_char = random.sample(w_list, 8)
pwd = ''.join(pwd_char)
print("8位随机验证码：", pwd)

############################作业8####################
"""
写一个模拟撞库的程序，假如密码都是用md5加密的，没有加盐，撞库就是用多个猜测的密码
尝试对比正确的密码，对比过程一定是用md5来进行的。
"""
import hashlib

pwd = 'michelle123'
m = hashlib.md5()
m.update(pwd.encode('utf-8'))
pwd_hexdigest = m.hexdigest()
while True:
    m_guess = hashlib.md5()
    pwd_guess = input('输入密码：').strip()
    m_guess.update(pwd_guess.encode('utf-8'))
    if pwd_hexdigest == m_guess.hexdigest():
        print("密码输入正确！")
        break
    else:
        print('密码输入错误，请重新输入！')
############################作业9####################
"""
使用re模块写一个验证手机号号码是否有效的程序(文件是嫩模联系方式.txt)，按照中国大陆的手机号标准来对比验证，输出有效的号码
"""
import re

with open('嫩模联系方式.txt', 'r', encoding='utf-8') as f:
    list_txt = f.readlines()[1:]
num_list = [s.split(' ')[-1].split('\n')[0] for s in list_txt]
ret_list = []
# 然后手机号第二位只有3,5,6,7,8,这几个数字，所以通过[3,5,7,8,9]来匹配其中的任一数字
phone_rule = re.compile("^1[35789]\d{9}$")
for it in num_list:
    res = re.search(phone_rule, it)
    if res:
        ret_list.append(res.group(0))
print(ret_list)
