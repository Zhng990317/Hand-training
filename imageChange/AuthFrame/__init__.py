# -*-coding:utf-8 -*-
# @Date: 2023/2/16 15:39
# @File: __init__.py
from AuthFrame.Utils.OperationFile import Operation


class AuthFrame(object):

    def __init__(self, file_path, sheet_name):
        self.Operation = Operation(file_path, sheet_name)

    def create_file(self, labels: list = None):
        self.Operation.create_file(labels)

    def read_file(self, row=None, col=None):
        return self.Operation.read_file(row, col)