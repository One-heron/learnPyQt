# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 11:29
# @Author  : Wanghairui
# @function: 勾选框
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction("View statusbar", self, checkable=True)
        viewStatAct.setStatusTip("View statusbar")
        viewStatAct.setCheckable(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Check menu")
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()