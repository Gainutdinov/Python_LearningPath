# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Марат\Desktop\Code\week2\projectManager\widgets\projectManager.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(368, 303)
        self.centralwidget = QtWidgets.QWidget(projectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.projectList_ly = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.projectList_ly.setContentsMargins(0, 0, 0, 0)
        self.projectList_ly.setObjectName("projectList_ly")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_btn = QtWidgets.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.templateEditor_btn = QtWidgets.QPushButton(self.widget)
        self.templateEditor_btn.setObjectName("templateEditor_btn")
        self.verticalLayout.addWidget(self.templateEditor_btn)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_lb = QtWidgets.QLabel(self.groupBox)
        self.info_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_lb.setObjectName("info_lb")
        self.verticalLayout_3.addWidget(self.info_lb)
        self.verticalLayout.addWidget(self.groupBox)
        self.settings_btn = QtWidgets.QPushButton(self.widget)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.verticalLayout_2.addWidget(self.splitter)
        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        _translate = QtCore.QCoreApplication.translate
        projectManager.setWindowTitle(_translate("projectManager", "Project Manager"))
        self.create_btn.setText(_translate("projectManager", "Create Project"))
        self.templateEditor_btn.setText(_translate("projectManager", "Template Editor"))
        self.groupBox.setTitle(_translate("projectManager", "Info"))
        self.info_lb.setText(_translate("projectManager", "TextLabel"))
        self.settings_btn.setText(_translate("projectManager", "Settings"))

