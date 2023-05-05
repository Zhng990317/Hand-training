# -*-coding:utf-8 -*-
# @Date: 2023/3/31 14:13
# @File: login_page
'''登录功能'''
from configparser import ConfigParser
from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import os


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.conf = ConfigParser()
        self.conf.read(
            os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + r'\sources\page_elements\elements.ini',
            encoding="UTF-8")

    def switching_login_method(self):
        '''切换登录方式：账密登录'''
        self.click_method(*eval(self.conf.get('login', 'pwd_login')))

    def input_mobile(self, mobile):
        '''输入手机号'''
        self.sendkeys_method(mobile, *eval(self.conf.get('login', 'mobile')))

    def input_pwd(self, pwd):
        '''输入密码'''
        self.sendkeys_method(pwd, *eval(self.conf.get('login', 'pwd')))

    def click_login(self):
        '''点击登录'''
        self.click_method(*eval(self.conf.get('login', 'login_button')))
        sleep(5)

    def quit_login(self):
        '''强制退出'''
        self.click_method(*eval(self.conf.get('login', 'quit_login')))

    def select_company(self):
        '''企业登录'''
        self.click_method(*eval(self.conf.get('login', 'company_login')))

    toask1 = (By.XPATH,'//*[@id="layui-layer4"]/div')
    toask2 = (By.XPATH,'//*[@id="layui-layer5"]/div')
    def login(self, mobile, pwd):
        self.switching_login_method()
        self.input_mobile(mobile)
        self.input_pwd(pwd)
        self.click_login()
        self.driver.implicitly_wait(10)
        if self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-title").text == '提示':
            print(self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-title").text)
            self.quit_login()
            self.click_login()
        print(self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-title").text)
        self.select_company()
