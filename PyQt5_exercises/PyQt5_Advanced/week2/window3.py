from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import dialog

class windowClass(QWidget):
    def __init__(self):
        super(windowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.button = QPushButton('Click me')
        layout.addWidget(self.button)
        self.resize(300,200)
        self.button.clicked.connect(self.showMessage)

    def showMessage(self):
        self.dial = dialog.dialogClass()
        r = self.dial.exec_()
        if r:
            print(self.dial.getData())

if __name__=='__main__':
    app = QApplication([])
    w = windowClass()
    w.show()
    app.exec_()