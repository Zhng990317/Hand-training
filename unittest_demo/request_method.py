# -*-coding:utf-8 -*-
# @Date: 2023/6/20 11:16
# @File: request_method.py
import requests
from requests import *


class RequestMethod():
    """请求方式"""

    def __init__(self, url):
        self.url = url

    def base_method(self):
        """"""
        pass

    def get_method(self):
        get_res = get(self.url)
        return get_res


print(RequestMethod('https://www.baidu.com').get_method())
