# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 11:29
# @Author  : Wanghairui
# @function:
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Quit Button")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()