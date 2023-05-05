# -*-coding:utf-8 -*-
# @Date: 2023/3/24 16:26
# @File: MainWindowsConn
# -*-coding:utf-8 -*-
# @Date: 2023/3/9 14:11
# @File: MainWindows
import json

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.mainWindows import Ui_MainWindow

class MainDialog(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        '''背景图设置'''
        painter = QPainter(self)
        pixmap = QPixmap("./Resource/images/1.jpg")
        #rect(left,top,width,height)
        painter.drawPixmap(self.rect(), pixmap)



