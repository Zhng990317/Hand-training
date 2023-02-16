# -*-coding:utf-8 -*-
# @Date: 2023/2/6 16:02
# @File: FindLargeFile
import os


def get_file(filepath=r'F:\工具文件\安装包', filesize=500 * 1024 * 1024):
    for dirpath, dirnames, filenames in os.walk(filepath):
        '''
        @:param dirpath 文件路径 string
        @:param dirnames 文件夹名称 list
        @:param filenames 文件名称 list
        '''
        for filename in filenames:
            if os.path.isfile(str(dirpath) + '\\' + filename):
                size = os.path.getsize(str(dirpath) + '\\' + filename)
                if size > filesize:
                    print(dirpath + "\\" + filename, "{:.2f}M".format(size / 1024 / 1024))


get_file()
