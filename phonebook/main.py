#!/usr/bin/env python3.6

import sys
from PyQt5 import QtWidgets
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        self.addr_book = []
        # initialize all parent object
        super().__init__()
        # initialize design here
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
