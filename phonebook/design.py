#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base_example.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import functools

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):

    def __init__(self):
        self.address_book = [
            {
                "name": "Ivan",
                "surname": "Yurochko",
                "phone": "000-00-00",
                "address": "Lviv"
            },
            {
                "name": "Andrew",
                "surname": "Zanevych",
                "phone": "000-001-00",
                "address": "Kiev"
            }

        ]

    @pyqtSlot()
    def add_new(self):
        # append input text to address book and clear input
        tmp_entry = dict()
        tmp_entry["name"] = self.name.text()
        tmp_entry["surname"] = self.surname.text()
        tmp_entry["phone"] = self.phone.text()
        tmp_entry["address"] = self.address.text()
        self.address_book.append(tmp_entry)
        self.name.setText("")
        self.surname.setText("")
        self.phone.setText("")
        self.address.setText("")

    @pyqtSlot()
    def filter_by(self, pred_key):
        pred_value = getattr(self, "{}_search".format(pred_key))
        tmp_address_book = [row for row in self.address_book if pred_value.text() in row[pred_key]]
        
        self.show_all(tmp_address_book)
        # return functools.partial(self.show_all, tmp_address_book)
    
    @pyqtSlot()
    def show_all(self, filtered_book):
        # iterate over phone book and show in table
        self.phone_book_table.setRowCount(len(filtered_book))
        for row_num, row  in enumerate(filtered_book):
            for col_num, value  in enumerate(row.values()):
                self.phone_book_table.setItem(row_num, col_num, QTableWidgetItem(value))
        self.phone_book_table.resizeColumnsToContents()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.address_search = QtWidgets.QLineEdit(self.centralwidget)
        self.address_search.setObjectName("address_search")
        self.gridLayout.addWidget(self.address_search, 5, 0, 1, 1)
        self.btn_address_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_address_search.setObjectName("btn_address_search")
        self.btn_address_search.clicked.connect(functools.partial(self.filter_by, "address"))
        self.gridLayout.addWidget(self.btn_address_search, 6, 0, 1, 1)

        self.name_search = QtWidgets.QLineEdit(self.centralwidget)
        self.name_search.setObjectName("name_search")
        self.gridLayout.addWidget(self.name_search, 1, 0, 1, 1)
        self.btn_name_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_name_search.setObjectName("btn_name_search")
        self.btn_name_search.clicked.connect(functools.partial(self.filter_by, "name"))
        self.gridLayout.addWidget(self.btn_name_search, 2, 0, 1, 1)

        self.surname_search = QtWidgets.QLineEdit(self.centralwidget)
        self.surname_search.setObjectName("surname_search")
        self.gridLayout.addWidget(self.surname_search, 7, 0, 1, 1)
        self.btn_surname_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_surname_search.setObjectName("btn_surname_search")
        self.btn_surname_search.clicked.connect(functools.partial(self.filter_by, "surname"))
        self.gridLayout.addWidget(self.btn_surname_search, 8, 0, 1, 1)

        self.phone_search = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_search.setObjectName("phone_search")
        self.gridLayout.addWidget(self.phone_search, 3, 0, 1, 1)
        self.btn_phone_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_phone_search.setObjectName("btn_phone_search")
        self.btn_phone_search.clicked.connect(functools.partial(self.filter_by, "phone"))
        self.gridLayout.addWidget(self.btn_phone_search, 4, 0, 1, 1)

        # related to show all
        self.phone_book_table = QtWidgets.QTableWidget(self.centralwidget)
        self.phone_book_table.setRowCount(0)
        self.phone_book_table.setColumnCount(4)
        self.phone_book_table.setHorizontalHeaderLabels(["Name", "Surname", "Phone", "Address"])
        self.phone_book_table.setObjectName("phone_book_table")
        self.gridLayout.addWidget(self.phone_book_table, 0, 0, 1, 1)
        self.btn_show_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_all.setObjectName("btn_show_all")
        self.btn_show_all.clicked.connect(functools.partial(self.show_all, self.address_book))
        self.gridLayout.addWidget(self.btn_show_all, 10, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # section related to add new section
        self.add_entry = QtWidgets.QDockWidget(MainWindow)
        self.add_entry.setObjectName("add_entry")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_new = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btn_add_new.setObjectName("btn_add_new")
        self.btn_add_new.clicked.connect(self.add_new)
        self.horizontalLayout.addWidget(self.btn_add_new)
        
        self.name = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)

        self.surname = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.surname.setObjectName("surname")
        self.horizontalLayout.addWidget(self.surname)

        self.phone = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.phone.setObjectName("phone")
        self.horizontalLayout.addWidget(self.phone)

        self.address = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.address.setObjectName("address")
        self.horizontalLayout.addWidget(self.address)

        self.add_entry.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.add_entry)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_address_search.setText(_translate("MainWindow", "Address"))
        self.btn_name_search.setText(_translate("MainWindow", "Name"))
        self.btn_surname_search.setText(_translate("MainWindow", "Surname"))
        self.btn_phone_search.setText(_translate("MainWindow", "Phone"))
        self.btn_show_all.setText(_translate("MainWindow", "Show All"))
        self.btn_add_new.setText(_translate("MainWindow", "Add new"))
