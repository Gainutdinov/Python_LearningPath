from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import window_UIs as ui
import os

style = os.path.join(os.path.dirname(__file__), 'style.css')

class styleWidgetClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(styleWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.treeWidget.setAlternatingRowColors(0)
        self.pushButton.clicked.connect(self.applyStyle)

    
    def applyStyle(self):
        self.setStyleSheet(open(style).read())
    

if __name__=='__main__':
    app = QApplication([])
    w = styleWidgetClass()
    w.show()
    app.setStyle(QStyleFactory.create('plastique'))
    app.exec()