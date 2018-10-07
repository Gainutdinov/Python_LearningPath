from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class dialogClass(QDialog):
    def __init__(self):
        super(dialogClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.label = QLineEdit()
        self.ly.addWidget(self.label)

        self.ok_btn = QPushButton('OK')
        self.ly.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton('Cancel')
        self.ly.addWidget(self.cancel_btn)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def getData(self):
        return dict(text_qlineedit=self.label.text())

if __name__=='__main__':
    app = QApplication([])
    w = dialogClass()
    w.show()
    app.exec_()