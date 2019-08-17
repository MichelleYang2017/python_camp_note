#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/16 21:54
# @Author:Michelle Yang
# @File  :hw.py
##############################hw1##################
"""
作业说明:将names=['albert', 'james', 'kobe','kd']中的名字全部编程大写
"""
names = ['albert', 'james', 'kobe', 'kd']
names_modify = map(lambda x: x.upper(), names)
print(list(names_modify))  # ['ALBERT', 'JAMES', 'KOBE', 'KD']

#########################hw2########################
"""
作业说明：将names=['albert','jr_shenjing', 'kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
"""
names = ['albert', 'jr_shenjing', 'kobe', 'kd']
names_filter = list(filter(lambda x: not x.endswith('shenjing'), names))  # ['albert', 'kobe', 'kd']
names_filter_len = list(map(lambda x: len(x), names_filter))
print(names_filter_len)

#########################hw3#########################
"""
作业说明：求文件a.txt中最长的行的长度(长度按字符个数算，需要使用max函数)
"""
with open('./a.txt', 'r', encoding='utf-8') as f:
    list_f = f.readlines()

max_len = len(max(list_f, key=lambda x: len(x)))
print(max_len)

###########################hw4######################
"""
作业说明：文件shopping.txt内容如下，分别代表商品，价格和数量
mac,20000,3
lenovo,3000,10
bmv,1000000,10
chicken,200,1
(1)求总共花了多少钱？
(2)打印出所有的商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
(3)求单价大于10000的商品信息，格式同上
"""
from functools import reduce

with open('shopping.txt', 'r', encoding='utf-8') as f:
    shop_info_list = f.readlines()

shop_price_list = list(map(lambda x: int(x.split(',')[1]), shop_info_list))
shop_name_list = list(map(lambda x: x.split(',')[0], shop_info_list))
shop_count_list = list(map(lambda x: int(x.split(',')[-1]), shop_info_list))
###############求总共花了多少钱##############
product_every_price = [x * y for x, y in zip(shop_count_list, shop_price_list)]
product_price_all = reduce(lambda x, y: x + y, product_every_price)
print(product_price_all)
###############打印出所有的商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
product_info_list = []
for i in range(len(shop_info_list)):
    dict1 = {}
    dict1['name'] = shop_name_list[i]
    dict1['price'] = shop_price_list[i]
    dict1['count'] = shop_count_list[i]
    product_info_list.append(dict1)
print(product_info_list)
##############求单价大于10000的商品信息
product_filter = list(filter(lambda x: x['price'] > 10000, product_info_list))
print(product_filter)
