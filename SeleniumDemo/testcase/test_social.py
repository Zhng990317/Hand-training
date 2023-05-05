# -*-coding:utf-8 -*-
# @Date: 2023/4/3 15:04
# @File: test_social
import json

from pageobject.social_page import SocialPage
from testcase.base_testcase import BaseTestCase
from tools.generate_parameters import _gp_
import os


class TestSocial(BaseTestCase):

    def setUp(self):
        super().setUp()
        with open(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + r'\sources\cookie\cookie.txt', 'r') as f:
            cookie_list = json.loads(f.read())
            for cookie in cookie_list:
                if 'expiry' in cookie:
                    cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)
        self.driver.refresh()

    def test_social(self):
        handles = self.driver.window_handles
        name = _gp_.create_name()
        phone = _gp_.create_phone()
        idcard = _gp_.create_idcard()
        social_page = SocialPage(self.driver)
        social_page.social(name, phone, idcard)
        try:
            assert '订单' == self.driver.title
        except Exception as e:
            raise e
