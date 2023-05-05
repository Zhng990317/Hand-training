# -*-coding:utf-8 -*-
# @Date: 2023/4/3 14:28
# @File: social_page
'''社保功能'''
from configparser import ConfigParser
from time import sleep
import os

from framework.base_page import BasePage
from selenium.webdriver.common.by import By as by


class SocialPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.conf = ConfigParser()
        self.conf.read(
            os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + r'\sources\page_elements\elements.ini',
            encoding="UTF-8")

    def switch_to_social(self):
        '''切换进行社保功能'''
        self.click_method(*eval(self.conf.get('social', 'social_menu')))

    def add_insured(self):
        '''新增参保'''
        self.click_method(*eval(self.conf.get('social', 'add_social')))

    def name_parma(self, name):
        '''输入姓名'''
        self.sendkeys_method(name, *eval(self.conf.get('social', 'name')))

    def phone_parma(self, phone):
        '''输入手机号'''
        self.sendkeys_method(phone, *eval(self.conf.get('social', 'phone')))

    def idcard_parma(self, idcard):
        '''选择证件类型，输入证件号'''
        self.click_method(*eval(self.conf.get('social', 'iDCardType')))
        self.click_method(*eval(self.conf.get('social', 'select_iDCardType')))
        self.sendkeys_method(idcard, *eval(self.conf.get('social', 'iDCardNumber')))

    def city_parma(self):
        '''选择参保城市'''
        self.click_method(*eval(self.conf.get('social', 'city')))
        sleep(5)
        self.click_method(*eval(self.conf.get('social', 'select_city')))

    def social_type_pamra(self):
        '''选择社保类型'''
        self.click_method(*eval(self.conf.get('social', 'social_type')))
        self.click_method(*eval(self.conf.get('social', 'select_social_type')))

    def is_insured_as_city_parma(self):
        '''是否在此城市参保'''
        self.click_method(*eval(self.conf.get('social', 'is_insured_as_city')))
        self.click_method(*eval(self.conf.get('social', 'insured_city_yes')))

    _confirm_button_locator = (by.XPATH, "//a[@id='confirmBtn']")

    def social_number_parma(self):
        '''最小社保基数'''
        self.click_method(*eval(self.conf.get('social', 'min_social')))
        if self.driver.find_element(by.XPATH, "//h3[contains(.,'预收费提示')]").text == "预收费提示":
            self.click_method(*self._confirm_button_locator)

    def sendkeys_insured_social_values(self, name, phone, idcard):
        '''社保参保信息'''
        self.name_parma(name)
        self.phone_parma(phone)
        self.idcard_parma(idcard)
        self.city_parma()
        self.social_type_pamra()
        self.is_insured_as_city_parma()
        self.social_number_parma()

    _confirm_button_shenyang_locator = (by.XPATH, "//a[@id='confirmBtn']")

    def sendkeys_insured_house_values(self):
        '''公积金参保信息'''
        sleep(2)
        self.click_method(*eval(self.conf.get('social', 'is_house_as_city')))  # 是否曾在本市参缴公积金：是
        self.click_method(*eval(self.conf.get('social', 'house_city_yes')))
        sleep(2)
        self.click_method(*eval(self.conf.get('social', 'house_scale')))  # 点击公积金比例
        self.click_method(*eval(self.conf.get('social', 'select_house_scale')))  # 选择公积金比例
        sleep(1)
        self.click_method(*eval(self.conf.get('social', 'min_house')))  # 最小公积金基数
        if self.driver.find_element(by.XPATH, "//h3[contains(.,'预收费提示')]").text == "预收费提示":
            self.click_method(*self._confirm_button_locator)
        if self.driver.find_element(by.XPATH, '//*[@id="modal-shenyang"]/div/h3').text == "提示":
            self.click_method(*self._confirm_button_shenyang_locator)

    def next_step(self):
        '''下一步'''
        self.click_method(*eval(self.conf.get('social', 'next')))  # 下一步

    _go_submit_locator = (by.XPATH, "//button[@id='go-submit']")

    def supplementary_information(self):
        '''补充资料'''
        self.click_method(*self._go_submit_locator)

    _place_order_locator = (by.XPATH, "//button[contains(.,'提交订单')]")

    def place_order(self):
        '''提交订单'''
        self.click_method(*self._place_order_locator)
        sleep(2)

    def social(self, name, phone, idcard):
        self.switch_to_social()
        sleep(2)
        self.add_insured()
        sleep(2)
        self.sendkeys_insured_social_values(name, phone, idcard)
        sleep(2)
        self.sendkeys_insured_house_values()
        self.next_step()
        sleep(2)
        self.supplementary_information()
        sleep(2)
        self.place_order()
