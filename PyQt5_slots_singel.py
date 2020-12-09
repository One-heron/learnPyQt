# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 11:00
# @Author  : Wanghairui
# @function: 信号与槽简单实现
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Quit Button")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()