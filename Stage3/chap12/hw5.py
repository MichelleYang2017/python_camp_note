#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/25 21:31
# @Author:Michelle Yang
# @File  :hw5.py
########################homework 5###################
"""作业说明：
简易王者荣耀：
    1.设计王者荣耀中的英雄类，每个英雄对象可以对其他影响对象使用技能
    2.英雄具备以下属性英雄名称，等级，血量和Q_hurt， W_hurt, E_hurt三个伤害属性，
      表示格技能的伤害量
    3.具备以下技能Q W E 三个技能都需要一个敌方英雄作为参数，当敌方血量小于等于0时角色死亡
"""


class Hero(object):
    def __init__(self, name, level, blood, Q_hurt, W_hurt, E_hurt):
        self.name = name
        self.level = level
        self.blood = blood
        self.Q_hurt = Q_hurt
        self.W_hurt = W_hurt
        self.E_hurt = E_hurt

    def W(self, obj):
        obj.blood -= self.W_hurt
        if obj.blood <= 0:
            print('{}已经死亡！'.format(obj.name))
            del obj
            return None
        else:
            info = """
            英雄{}W了{}
            {}掉血{},还剩{}
            """.format(self.name, obj.name, obj.name, self.W_hurt, obj.blood)
            print(info)
            return obj

    def Q(self, obj):
        obj.blood -= self.W_hurt
        if obj.blood <= 0:
            print('{}已经死亡！'.format(obj.name))
            del obj
            return None

        else:
            info = """
                            英雄{}Q了{}
                        {}掉血{},还剩{}
                        """.format(self.name, obj.name, obj.name, self.Q_hurt, obj.blood)
            print(info)
            return obj

    def E(self, obj):
        obj.blood -= self.E_hurt
        if obj.blood <= 0:
            print('{}已经死亡！'.format(obj.name))
            del obj
            return None
        else:
            info = """
                        英雄{}E了{}
                        {}掉血{},还剩{}
                        """.format(self.name, obj.name, obj.name, self.E_hurt, obj.blood)
            print(info)
            return obj


if __name__ == '__main__':
    hero1 = Hero('孙悟空', '战士', 20000, 1000, 1000, 1000)
    hero2 = Hero('项羽', '坦克', 1500, 1000, 1000, 1000)
    hero1.W(hero2)
    hero1.E(hero2)
