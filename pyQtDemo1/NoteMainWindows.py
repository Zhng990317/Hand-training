# -*-coding:utf-8 -*-
# @Date: 2022/9/30 10:19
# @File: NoteMainWindows
import sys

from PyQt5.QtWidgets import *
from untitled import Ui_Dialog
import faker

class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    def load(self):
        fk = faker.Faker(locale='zh_CN')
        name = fk.name()
        phone = fk.phone_number()
        idcard = fk.ssn(min_age=18, max_age=90)
        info_str = name + ' , ' + idcard + ' , ' + phone
        self.ui.plainTextEdit.setPlainText(info_str)


    def clear(self):
        self.ui.plainTextEdit.clear()






