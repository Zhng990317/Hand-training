# -*-coding:utf-8 -*-
# @Date: 2023/3/31 14:38
# @File: base_testcase
import os.path
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class BaseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        dir = os.path.dirname(os.path.abspath('.'))
        edge_driver_path = Service(os.path.join(dir, '\msedgedriver.exe'))

        self.option = Options()
        self.option.add_argument(
            "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'")
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Edge(service=edge_driver_path, options=self.option)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        url = 'https://ers-user.test-01.54test.cn/Account/Login'
        self.driver.get(url)
        self.driver.refresh()

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()
        self.driver.quit()
