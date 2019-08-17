#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/8/17 13:49
# @Author:Michelle Yang
# @File  :start.py
import json
from python_camp_note.Stage2.stage2_hw.conf import settings

config = settings.Configuration()


def load_user_info(filepath=config.user_info_file):
    with open(filepath, 'rt', encoding='utf-8') as f:
        try:
            user_info = json.load(f)
            return user_info
        except json.decoder.JSONDecodeError as err:
            return []


def load_logger_file(filepath=config.log_file_path):
    f = open(filepath, 'a', encoding='utf-8')
    return f
