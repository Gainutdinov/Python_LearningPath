from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os, json
settingsFileName = 'converterSettings.json'

class qlineEditClass(QLineEdit):
    # def __init__(self):
    #     super(qlineEditClass, self).__init__()
    def mouseDoubleClickEvent(self, QMouseEvent):
        #self.pyqtSignal().emit()
        #print(QMouseEvent.button())
        self.setText('')
        self.setPlaceholderText('...')

