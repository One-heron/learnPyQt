# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 11:29
# @Author  : Wanghairui
# @function: 状态显示
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Statusbar")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()