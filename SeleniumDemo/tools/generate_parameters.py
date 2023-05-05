# -*-coding:utf-8 -*-
# @Date: 2023/4/3 14:57
# @File: generate_parameters
import faker


class GenerateParameters:
    def __init__(self):
        self.fk = faker.Faker(locale='zh-CN')

    def create_name(self):
        return self.fk.name()

    def create_phone(self):
        return self.fk.phone_number()

    def create_idcard(self):
        return self.fk.ssn(min_age=18, max_age=55)

    def create_other(self):
        pass


_gp_ = GenerateParameters()
