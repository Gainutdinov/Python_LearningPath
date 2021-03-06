from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import window_ui

class exampleWindowClass(QWidget, window_ui.Ui_example):
    def __init__(self):
        super(exampleWindowClass, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ITEM LIST')
        self.count = 1
        self.additem_btn.clicked.connect(self.addItem)
        self.name_le.returnPressed.connect(self.addItem)
    
    def addItem(self):
        text = self.name_le.text()
        if text:
            lb = QLabel('%s: %s' %(self.count, text))
            self.items_ly.addWidget(lb)
            self.count += 1

if __name__=='__main__':
    app = QApplication([])
    w = exampleWindowClass()
    w.show()
    app.exec_()