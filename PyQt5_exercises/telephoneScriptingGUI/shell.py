# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shell.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(459, 523)
        MainWindow.setMinimumSize(QtCore.QSize(414, 489))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mw_vrlt = QtWidgets.QVBoxLayout()
        self.mw_vrlt.setObjectName("mw_vrlt")
        self.qst_cmb = QtWidgets.QComboBox(self.centralwidget)
        self.qst_cmb.setObjectName("qst_cmb")
        self.mw_vrlt.addWidget(self.qst_cmb)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 437, 388))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scr_vrlt = QtWidgets.QVBoxLayout()
        self.scr_vrlt.setContentsMargins(0, -1, -1, -1)
        self.scr_vrlt.setObjectName("scr_vrlt")
        self.verticalLayout_3.addLayout(self.scr_vrlt)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mw_vrlt.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.mw_vrlt)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.svIntoFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.svIntoFile_btn.setEnabled(True)
        self.svIntoFile_btn.setObjectName("svIntoFile_btn")
        self.gridLayout.addWidget(self.svIntoFile_btn, 0, 2, 1, 1)
        self.clipboard_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clipboard_btn.setObjectName("clipboard_btn")
        self.gridLayout.addWidget(self.clipboard_btn, 0, 1, 1, 1)
        self.prevQues_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prevQues_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.prevQues_btn.setObjectName("prevQues_btn")
        self.gridLayout.addWidget(self.prevQues_btn, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telephone Assistant (TS)"))
        self.svIntoFile_btn.setText(_translate("MainWindow", "Сохранить в файл"))
        self.clipboard_btn.setText(_translate("MainWindow", "Скопировать в буфер обмена"))
        self.prevQues_btn.setText(_translate("MainWindow", "Перейти к пред. вопросу"))

