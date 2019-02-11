from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class drawCustomWidget(QWidget):
    def __init__(self):
        super(drawCustomWidget, self).__init__()
        self.resize(300,200)
        self.setWindowTitle('Custom Widget')
    
    def paintEvent(self, event):
        rec = event.rect()
        painter = QPainter()
        painter.begin(self)
        ###
        painter.end(self)

if __name__=='__main__':
    app = QApplication([])
    w = drawCustomWidget()
    w.show()
    app.exec_()
