# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(396, 407)
        self.verticalLayout = QtWidgets.QVBoxLayout(Server)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progress_pbr = QtWidgets.QProgressBar(Server)
        self.progress_pbr.setProperty("value", 0)
        self.progress_pbr.setObjectName("progress_pbr")
        self.verticalLayout.addWidget(self.progress_pbr)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_lb = QtWidgets.QLabel(Server)
        self.info_lb.setObjectName("info_lb")
        self.horizontalLayout.addWidget(self.info_lb)
        self.ip_le = QtWidgets.QLineEdit(Server)
        self.ip_le.setReadOnly(True)
        self.ip_le.setObjectName("ip_le")
        self.horizontalLayout.addWidget(self.ip_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.out_tb = QtWidgets.QTextBrowser(Server)
        self.out_tb.setObjectName("out_tb")
        self.verticalLayout.addWidget(self.out_tb)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.info_lb.setText(_translate("Server", "IP:"))

