import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from MainWindowsConn import MainDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dlg = MainDialog()
    Dlg.show()
    sys.exit(app.exec_())
