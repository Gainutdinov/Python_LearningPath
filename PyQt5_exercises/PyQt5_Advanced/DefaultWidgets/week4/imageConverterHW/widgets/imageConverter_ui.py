# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Марат\Desktop\Code\week4\imageConverterHW\widgets\imageConverter.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from . import lineEdit

class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        imageConverter.setObjectName("imageConverter")
        imageConverter.resize(339, 418)
        self.centralwidget = QtWidgets.QWidget(imageConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconvert_lb = QtWidgets.QLabel(self.centralwidget)
        self.iconvert_lb.setObjectName("iconvert_lb")
        self.horizontalLayout.addWidget(self.iconvert_lb)
        self.browseIconvert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browseIconvert_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseIconvert_btn.setObjectName("browseIconvert_btn")
        self.horizontalLayout.addWidget(self.browseIconvert_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.files_ly = QtWidgets.QVBoxLayout()
        self.files_ly.setObjectName("files_ly")
        self.verticalLayout.addLayout(self.files_ly)
        self.OutDir_grbox = QtWidgets.QGroupBox(self.centralwidget)
        self.OutDir_grbox.setObjectName("OutDir_grbox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.OutDir_grbox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #self.out_le = QtWidgets.QLineEdit(self.OutDir_grbox)
        self.out_le = lineEdit.qlineEditClass(self.OutDir_grbox)
        self.out_le.setObjectName("out_le")
        self.out_le.setPlaceholderText("output directory")
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtWidgets.QPushButton(self.OutDir_grbox)
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseOut_btn.setObjectName("browseOut_btn")
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.verticalLayout.addWidget(self.OutDir_grbox)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)
        QtCore.QMetaObject.connectSlotsByName(imageConverter)

    def retranslateUi(self, imageConverter):
        _translate = QtCore.QCoreApplication.translate
        imageConverter.setWindowTitle(_translate("imageConverter", "MainWindow"))
        self.iconvert_lb.setText(_translate("imageConverter", "Path"))
        self.browseIconvert_btn.setText(_translate("imageConverter", "..."))
        self.OutDir_grbox.setTitle(_translate("imageConverter", "Out directory"))
        self.browseOut_btn.setText(_translate("imageConverter", "..."))
        self.start_btn.setText(_translate("imageConverter", "Start"))

