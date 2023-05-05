# -*-coding:utf-8 -*-
# @Date: 2023/4/13 10:08
# @File: test
import os
from configparser import ConfigParser
from selenium.webdriver.common.by import By
def tests():
    abp = os.path.abspath(os.path.dirname(__file__))
    abp = os.path.split(abp)[0]
    abp = abp + r'\sources\page_elements\elements.ini'
    print(abp, os.path.isabs(abp))

    conf = ConfigParser()
    conf.read(abp, encoding="utf-8")
    pwd_login_locator = conf.get("login", "pwd_login")
    print(pwd_login_locator)
    l = eval(pwd_login_locator)
    print(l, '\n', type(l))
    print(*l)

if __name__ == '__main__':
    tests()