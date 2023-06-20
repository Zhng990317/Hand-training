# -*-coding:utf-8 -*-
# @Date: 2023/6/20 11:16
# @File: request_method.py
import requests
from requests import *


class RequestMethod(object):
    """请求方式"""

    def __init__(
            self,
            method=None,
            url=None,
            headers=None,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            json=None,
    ):
        data = [] if data is None else data
        files = [] if files is None else files
        headers = {} if headers is None else headers
        params = {} if params is None else params

        self.method = method
        self.url = url
        self.headers = headers
        self.files = files
        self.data = data
        self.json = json
        self.params = params
        self.auth = auth
        self.cookies = cookies

    def base_method(self):
        """"""
        pass

    def get_method(self):
        get_res = get(self.url)
        return get_res

url = 'http://www.baidu.com'
res = RequestMethod(url).get_method()
print(res)