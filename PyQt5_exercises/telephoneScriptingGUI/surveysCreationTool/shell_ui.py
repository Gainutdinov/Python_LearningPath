# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shell_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.xml_trView = QtWidgets.QTreeView(self.centralwidget)
        self.xml_trView.setObjectName("xml_trView")
        self.verticalLayout.addWidget(self.xml_trView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.getValue_btn = QtWidgets.QPushButton(self.centralwidget)
        self.getValue_btn.setObjectName("getValue_btn")
        self.verticalLayout_2.addWidget(self.getValue_btn)
        self.obtainSel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.obtainSel_btn.setEnabled(False)
        self.obtainSel_btn.setObjectName("obtainSel_btn")
        self.verticalLayout_2.addWidget(self.obtainSel_btn)
        self.insertQsre_btn = QtWidgets.QPushButton(self.centralwidget)
        self.insertQsre_btn.setEnabled(False)
        self.insertQsre_btn.setObjectName("insertQsre_btn")
        self.verticalLayout_2.addWidget(self.insertQsre_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SurveysCreationTool(CST)"))
        self.getValue_btn.setText(_translate("MainWindow", "Get value"))
        self.obtainSel_btn.setText(_translate("MainWindow", "Obtain selected tag value"))
        self.insertQsre_btn.setText(_translate("MainWindow", "Insert new questionnaire"))

