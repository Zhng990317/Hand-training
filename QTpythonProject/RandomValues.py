# -*-coding:utf-8 -*-
# @Date: 2023/3/9 9:44
# @File: RandomValues

from faker import Faker

KEYS = ['number', 'name', 'mobile', 'email', 'idcard', 'address', 'department', 'position']

class RandomValues(object):
    def __init__(self):
        self.set_values()

    def set_values(self):
        fk = Faker(locale='zh-CN')
        setattr(self, 'number', fk.uuid4(cast_to=str))
        setattr(self, 'name', fk.name())
        setattr(self, 'mobile', fk.phone_number())
        setattr(self, 'email', fk.ascii_company_email())
        setattr(self, 'idcard', fk.ssn(min_age=18, max_age=45))
        setattr(self, 'address', fk.address())
        setattr(self, 'department', '其他')
        setattr(self, 'position', fk.job())

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def customer_params(self, keys: list):
        value_dict = {}
        if set(keys).issubset(KEYS):
            for key in keys:
                value_dict[key] = self.__dict__[key]
        return value_dict