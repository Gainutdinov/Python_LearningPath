# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Марат\Desktop\Code\week2\projectManager\widgets\templateEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        templateEditor.setObjectName("templateEditor")
        templateEditor.resize(331, 371)
        self.verticalLayout = QtWidgets.QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(templateEditor)
        self.add_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QPushButton(templateEditor)
        self.remove_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout.addWidget(self.remove_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tree = QtWidgets.QTreeWidget(templateEditor)
        self.tree.setEnabled(True)
        self.tree.setObjectName("tree")
        self.tree.header().setVisible(False)
        self.verticalLayout.addWidget(self.tree)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_btn = QtWidgets.QPushButton(templateEditor)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.close_btn = QtWidgets.QPushButton(templateEditor)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(templateEditor)
        QtCore.QMetaObject.connectSlotsByName(templateEditor)

    def retranslateUi(self, templateEditor):
        _translate = QtCore.QCoreApplication.translate
        templateEditor.setWindowTitle(_translate("templateEditor", "Form"))
        self.add_btn.setText(_translate("templateEditor", "+"))
        self.remove_btn.setText(_translate("templateEditor", "-"))
        self.save_btn.setText(_translate("templateEditor", "Save"))
        self.close_btn.setText(_translate("templateEditor", "Close"))

