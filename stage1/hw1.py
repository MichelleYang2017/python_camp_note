#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/7 10:10
# @Author:Michelle Yang
# @File  :hw1.py
""""要求：
    打印三级菜单，如汽车，种类，品牌，型号
    可返回上一级
    可随时退出程序
"""
menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            "奔驰": {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {},
            },
            '奥迪': {
                '奥迪A4L': {},
            },
        },
        '越野车': {
            "保时捷": {
                '保时捷Macan': {},
                '保时捷Cayenne': {}
            },
            '路虎': {},
            '黄菲蒂尼': {},
        },
        '卡车': {},
        '公交车': {}
    },
    '飞机': {
        '大飞机': {
            '大1': {
                'xxx': {},
            }
        },
        '小飞机': {
            '小1': {
                'xxx': {}
            }
        },
        '大炮': {}
    }
}

parent_layers = []  # parent layer
cur_layer = menu  # 当前层
head_flag = True  # 第一层菜单的标志，如果在顶层用户不能选择p
print("欢迎您，按'q'您可以随时退出，按'p'您可以返回上一层")
while True:
    cur_layer_list = []
    # 判断当前层是否有值，没值只能返回顶层或者退出
    if cur_layer:
        for key in cur_layer:
            cur_layer_list.append(key)
        print(cur_layer_list)
    else:
        print("到达底层，按'q'您可以随时退出，按'p'您可以返回上一层")
    # 用户选择
    choice = input('输入您的选择==>').strip()
    if choice in cur_layer:
        parent_layers.append(cur_layer_list)
        if cur_layer[choice]:
            cur_layer = cur_layer[choice]
        else:
            print("到达底层，按'q'您可以随时退出，按'p'您可以返回上一层")
    elif choice == 'q':
        print('再见！')
        break
    elif choice == 'p':  # 用户返回上一层
        # 判断是否返回了顶部
        if not head_flag:
            head_flag = False
            cur_layer = parent_layers.pop()
            # 判断pop完之后是否还有值，如果没有说明到达了顶部
            if not cur_layer:
                head_flag = True
                parent_layers.append(cur_layer)
        else:
            print("到达顶层，按'q'您可以随时退出,不能选择'p'")
            cur_layer = menu
    else:
        print('不合法的输入！')
#