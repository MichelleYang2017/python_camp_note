#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/16 15:31
# @Author:Michelle Yang
# @File  :hw.py
####################作业说明：八皇后问题################
"""
八皇后问题指的是象棋中的皇后可以横向 纵向 斜向移动，如何在一个8*8的棋盘上放置8个皇后，
使得任意两个皇后都不在一条横线、竖线、斜线方向上。
"""
#########################思路解析#################
"""
思路：八个皇后在不同行，不同列，求出所有排列的可能
    遍历每一行，给每一行的皇后确定一个可能的位置，该位置与已经排列好的皇后不冲突，如果可能的位置为0，则说明
该路行不通，需要返回上一个皇后的位置，重新摆放上一个皇后的位置，以此类推。其中，在一行内给一个皇后安排一个位置这是个递归的过程，
该过程需要知道两个量：之前皇后的位置 以及 当前行
    停止条件：棋盘前8行每一行都正确安排了一个皇后，说明该方案是可行。
"""

###############说明：代码参考：https://www.cnblogs.com/franknihao/p/9416145.html
import numpy as np


def check_board(board, pos):
    """返回当前棋盘board的状态
    :param board: 8*8的棋盘
    :param pos: 在pos位置放置一个皇后是否冲突
    :return: True(不冲突)/False(冲突)
    """
    row, col = pos
    for i in range(row):
        for j in range(len(board)):
            if board[i][j] == 1:  # 说明之前某行某列有一个皇后
                if j == col or abs(j - col) == abs(i - row):  # 查看皇后所在的列以及是否在其对角线上
                    return False
    return True


def solution_queue(board, row):
    """ 计算皇后的多有可能方案
    :param board: 棋盘的状态
    :param row: 当前行
    :return:
    """
    if row == len(board):  # 终止条件
        # 可行方案打印
        print(board)
        return True
    # 不满足终止条件需要寻找一个可行的方案
    col_possible = 0
    for col_possible in range(len(board[0])):  # 遍历每一列
        if check_board(board, (row, col_possible)):
            board[row][col_possible] = 1  # 该位置可行，可以放置皇后
            if not solution_queue(board, row + 1):  # 如果下一行，没有皇后的位置，需要返回上一个皇后，重新找位置
                board[row][col_possible] = 0
            else:
                return True
    return False


def check_board_1dim(board, row, col):
    """检查该棋子棋盘是否可以放下
    :param board: 一维度的皇后的放置列数
    :param row: 棋子要放的当前行
    :param col: 棋子要放的当前列
    :return: 是否可以放置
    """
    i = 0
    while i < row:
        # 目标格子(row, col)和本格子(i,j)在同一条斜线上等价于 |row - i| == |col - j|
        if abs(col - board[i]) in (0, abs(row - i)):
            return False
        i += 1
    return True


def all_solution_queue(board, row):
    """ 计算皇后的多有可能方案
    :param board: 每一个皇后所在的列数，一位数组
    :param row: 当前行
    :return:
    """
    if row == len(board):  # 终止条件
        global count
        # 可行方案打印
        print(board)
        count += 1
        return True
    # 不满足终止条件需要寻找一个可行的方案
    col = 0
    while col < len(board):
        if check_board_1dim(board, row, col):
            board[row] = col
            if all_solution_queue(board, row + 1):
                pass
        col += 1
    return False


if __name__ == '__main__':
    board = np.zeros((8, 8))
    #################8个皇后摆放的一种方案##############
    solution_queue(board, 0)
    #################8个皇后摆放的所有方案##############
    board_1 = [0] * 8
    count = 0
    all_solution_queue(board_1, 0)
    print("总共有%d种方案！" % count)  # 92
