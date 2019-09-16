#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/16 19:08
# @Author:Michelle Yang
# @File  :client.py
from socket import *


def main():
    tcp_client = socket(AF_INET, SOCK_STREAM)
    tcp_client.connect(('127.0.0.1', 9090))
    content = tcp_client.recv(512)
    print(content.decode('utf-8'))
    while True:
        client_content = tcp_client.recv(512)
        print(client_content.decode('utf-8'))
        while True:
            choice = input('请输入您的选择>>').strip()
            if choice not in ['0', '1', '2', '3']:
                print('输入有误!重新输入！')
            else:
                break
        tcp_client.send(choice.encode('utf-8'))  # 先发送选择
        recv_msg = tcp_client.recv(512)
        if recv_msg.decode('utf-8')=='end':
            break


if __name__ == '__main__':
    main()
