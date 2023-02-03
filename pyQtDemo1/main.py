# -*-coding:utf-8 -*-
# @Date: 2022/10/27 15:57
# @File: main
import sys

from PyQt5.QtWidgets import QApplication

from NoteMainWindows import MainDialog

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())