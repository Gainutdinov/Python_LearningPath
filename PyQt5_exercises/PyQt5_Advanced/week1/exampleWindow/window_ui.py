# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Марат\Desktop\Code\exampleWindow\window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_example(object):
    def setupUi(self, example):
        example.setObjectName("example")
        example.resize(321, 240)
        self.widget = QtWidgets.QWidget(example)
        self.widget.setGeometry(QtCore.QRect(10, 10, 301, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.additem_btn = QtWidgets.QPushButton(self.widget)
        self.additem_btn.setObjectName("additem_btn")
        self.verticalLayout_2.addWidget(self.additem_btn)
        self.name_le = QtWidgets.QLineEdit(self.widget)
        self.name_le.setObjectName("name_le")
        self.verticalLayout_2.addWidget(self.name_le)
        self.items_ly = QtWidgets.QVBoxLayout()
        self.items_ly.setObjectName("items_ly")
        self.verticalLayout_2.addLayout(self.items_ly)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(example)
        QtCore.QMetaObject.connectSlotsByName(example)

    def retranslateUi(self, example):
        _translate = QtCore.QCoreApplication.translate
        example.setWindowTitle(_translate("example", "Form"))
        self.additem_btn.setText(_translate("example", "Add"))

