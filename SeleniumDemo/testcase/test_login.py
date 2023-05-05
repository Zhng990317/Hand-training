# -*-coding:utf-8 -*-
# @Date: 2023/3/31 14:52
# @File: test_login
import json

from pageobject.login_page import LoginPage
from testcase.base_testcase import BaseTestCase
import os
import ddt

login_data = [
    {"mobile": "18871284112", "pwd": "zxc123..."}
]

@ddt.ddt()
class TestLogin(BaseTestCase):

    @ddt.data(*login_data)
    def test_login(self, value):
        # mobile = '18871284112'
        # pwd = 'zxc123...'
        print(value["mobile"], value["pwd"])
        page_handles = self.driver.window_handles
        login_page = LoginPage(self.driver)
        login_page.login(value["mobile"], value["pwd"])
        self.driver.switch_to.window(page_handles[-1])
        with open(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + r'\sources\cookie\cookie.txt',
                  'w') as f:
            f.write(json.dumps(self.driver.get_cookies()))
        try:
            # self.driver.switch_to.window('工作台')
            assert '工作台' in self.driver.title
        except Exception as e:
            raise e
