#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/16 16:08
# @Author:Michelle Yang
# @File  :common.py.py
from socket import *
import hashlib


class File(object):
    def __init__(self, filepath=None):
        super(File, self).__init__()
        self.filepath = [filepath]
        self.md5_file = [self.file_to_md5(self.filepath)]

    def file_to_md5(self, filepath):
        m = hashlib.md5()
        with open(filepath, 'rb') as f:
            for line in f:
                m.update(line)
            file_md5 = m.hexdigest()
        return file_md5

    def add_file(self, filename):
        self.filepath.append(filename)
        self.md5_file.append(self.file_to_md5(filename))

    def files_to_dict(self):
        files_dict = {}
        for md5, filename in zip(self.md5_file, self.filepath):
            files_dict[md5] = filename
        return files_dict


class User(object):
    def __init__(self, name, pwd, stat=0):
        super(User, self).__init__()
        self.name = name
        self.pwd = pwd
        self.login = stat
        self.file = File()
