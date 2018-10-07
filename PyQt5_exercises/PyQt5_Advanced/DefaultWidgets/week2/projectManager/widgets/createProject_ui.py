# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Марат\Desktop\Code\week2\projectManager\widgets\createProject.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(288, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(createDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_lb = QtWidgets.QLineEdit(createDialog)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(createDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comment_te = QtWidgets.QPlainTextEdit(createDialog)
        self.comment_te.setObjectName("comment_te")
        self.gridLayout.addWidget(self.comment_te, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtWidgets.QPushButton(createDialog)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.cancel_btn = QtWidgets.QPushButton(createDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        _translate = QtCore.QCoreApplication.translate
        createDialog.setWindowTitle(_translate("createDialog", "Dialog"))
        self.label.setText(_translate("createDialog", "Name"))
        self.label_2.setText(_translate("createDialog", "Comment"))
        self.create_btn.setText(_translate("createDialog", "Create"))
        self.cancel_btn.setText(_translate("createDialog", "Cancel"))

