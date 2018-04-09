from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class simpleWindowClass(QWidget):
    def __init__(self):
        super(simpleWindowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel('Text')
        layout.addWidget(self.label)
        self.button = QPushButton('Press')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action)
    
    def action(self):
        self.label.setText('New Text')
        self.button.setText('Pressed!')
        self.button.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindowClass()
    w.show()
    app.exec_()