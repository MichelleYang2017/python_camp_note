#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/16 19:08
# @Author:Michelle Yang
# @File  :server.py
from socket import *
from project.python_camp_note.Stage4.stage4_hw.lib.user_choice import signup, login, exit_, uploadfile

user_choice = {
    '1': signup,
    '2': login,
    '3': uploadfile,
    '4': exit_,
}


def main():
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 9090))
    tcp_server.listen(5)
    while True:
        conn, addr = tcp_server.accept()
        conn.send('===欢迎使用简易版网盘管理系统==='.encode('utf-8'))
        while True:
            conn.send("""
                1 注册
                2 登陆
                3 上传文件
                0 退出
                """.encode('utf-8'))
            msg = conn.recv(512).decode('utf-8')  # 接收选择
            user_choice[msg]()
            conn.send(b'end')
        conn.close()
    tcp_server.close()


if __name__ == '__main__':
    main()
