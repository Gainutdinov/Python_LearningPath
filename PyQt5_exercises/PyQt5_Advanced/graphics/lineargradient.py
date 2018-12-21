#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QLinearGradient
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):        
                
        self.setGeometry(300, 300, 350, 260)
        self.setWindowTitle('Linear gradients')        
        self.show()
        
       
    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.drawGradients(painter)
        painter.end()               
        

    def drawGradients(self, painter):    

        grad1 = QLinearGradient(0, 20, 0, 110)

        grad1.setColorAt(0.1, Qt.black)
        grad1.setColorAt(0.5, Qt.yellow)
        grad1.setColorAt(0.9, Qt.black)

        painter.fillRect(20, 20, 300, 90, grad1)

        grad2 = QLinearGradient(0, 55, 250, 0)

        grad2.setColorAt(0.2, Qt.black)
        grad2.setColorAt(0.5, Qt.red)
        grad2.setColorAt(0.8, Qt.black)

        painter.fillRect(20, 140, 300, 100, grad2)
        
    
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())
