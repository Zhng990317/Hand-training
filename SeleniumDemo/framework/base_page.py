# -*-coding:utf-8 -*-
# @Date: 2023/3/31 13:50
# @File: base_page
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        '''打开页面'''
        self.driver.get(url)

    def find_element(self, *loc):
        '''查找元素'''
        try:
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*loc))
            element = self.driver.find_element(*loc)
            print('找到页面元素:%s', loc)
            return element
        except:
            print('%s 页面没有找到元素:%s' % (self, loc))

    def click_method(self, *loc):
        '''点击操作'''
        try:
            element = self.find_element(*loc)
            element.click()
            print('此元素:%s 已被点击' % element.text)
        except Exception as e:
            print('点击失败,原因:%s' % e)

    def sendkeys_method(self, inputStr, *loc):
        '''输入操作'''
        element = self.find_element(*loc)
        try:
            element.send_keys(inputStr)
            print(inputStr)
        except Exception as e:
            raise e

    def get_page_url(self):
        '''获取当前页面url'''
        return self.driver.current_url

    def get_windows_handle(self):
        '''获取当前窗口句柄'''
        return self.driver.current_windows_handle

