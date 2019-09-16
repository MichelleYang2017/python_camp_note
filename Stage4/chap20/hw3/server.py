#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/15 10:34
# @Author:Michelle Yang
# @File  :server.py

import time
from socket import *


def main():
    ip_port = ('127.0.0.1', 8080)
    buffer_size = 1024

    s1 = socket(AF_INET, SOCK_DGRAM)  # 数据报
    s1.bind(ip_port)

    while True:
        data, addr = s1.recvfrom(buffer_size)
        if not data:
            fmt = '%Y-%m-%d %X'  # udp服务可以接收空信息，如果为空信息，则为默认格式
        else:
            fmt = '%' + data.decode('utf-8')  # 自定义格式

        back_time = time.strftime(fmt)
        s1.sendto(back_time.encode('utf-8'), addr)


if __name__ == '__main__':
    main()