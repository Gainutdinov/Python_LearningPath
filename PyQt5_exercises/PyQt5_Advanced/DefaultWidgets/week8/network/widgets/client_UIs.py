# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(366, 107)
        self.verticalLayout = QtWidgets.QVBoxLayout(client)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ip_le = QtWidgets.QLineEdit(client)
        self.ip_le.setObjectName("ip_le")
        self.verticalLayout.addWidget(self.ip_le)
        self.connect_btn = QtWidgets.QPushButton(client)
        self.connect_btn.setObjectName("connect_btn")
        self.verticalLayout.addWidget(self.connect_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progress_sle = QtWidgets.QSlider(client)
        self.progress_sle.setOrientation(QtCore.Qt.Horizontal)
        self.progress_sle.setObjectName("progress_sle")
        self.horizontalLayout.addWidget(self.progress_sle)
        self.label = QtWidgets.QLabel(client)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(client)
        self.progress_sle.valueChanged['int'].connect(self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Client"))
        self.connect_btn.setText(_translate("client", "Connect"))
        self.label.setText(_translate("client", "0"))

