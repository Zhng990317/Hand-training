# -*-coding:utf-8 -*-
# @Date: 2023/2/16 15:39
# @File: __init__.py
from AuthFrame.CreateFile import Create


class AuthFrame(object):

    def __init__(self):
        pass

    def create_file(self, file_path, sheet_name, labels: list = None):
        Create(file_path, sheet_name, labels).set_up_excel()
