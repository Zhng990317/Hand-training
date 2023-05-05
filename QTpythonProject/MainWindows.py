# -*-coding:utf-8 -*-
# @Date: 2023/3/9 14:11
# @File: MainWindows
import json

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import *

from RandomValues import RandomValues
from tool1 import Ui_MainWindow


class MainDialog(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def changed_any(self):
        pass

    def created(self):
        text_list = []
        for cb in self.ui.groupBox.findChildren(QCheckBox):
            if cb.isChecked():
                text_list.append(cb.text())
        value_dict = RandomValues().customer_params(text_list)
        value_str = str(value_dict).replace("'", '"')
        self.ui.show_params.setPlainText(value_str)

    def clear(self):
        self.ui.show_params.clear()
        for cb in self.ui.groupBox.findChildren(QCheckBox):
            cb.setCheckState(Qt.Unchecked)
