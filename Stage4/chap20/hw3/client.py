#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/15 10:34
# @Author:Michelle Yang
# @File  :client.py
from socket import *


def main():
    ip_port = ('127.0.0.1', 8080)
    buffer_size = 1024

    s2 = socket(AF_INET, SOCK_DGRAM)  # 数据报
    print('请输入回车获取当前完整时间，Y获取当前年份，m获取当前月份，d获取当前日期，X获取当前时间')
    while True:
        data = input('-->：')
        s2.sendto(data.encode('utf--8'), ip_port)  # udp发信息没有链接，所以每一个发送信息都需要指定ip和端口
        data1, addr = s2.recvfrom(buffer_size)
        print('标准时间:', data1.decode('utf-8'))


if __name__ == '__main__':
    main()
