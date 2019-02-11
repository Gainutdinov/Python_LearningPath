#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter 
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):        
        
        self.setGeometry(300, 300, 590, 90)
        self.setWindowTitle('Transparent rectangles')

        

    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        self.drawRectangles(painter)
        painter.end()
        
        
    def drawRectangles(self, painter):
 
        for i in range(1, 11):
            
            painter.setOpacity(i*0.1)
            painter.fillRect(50*i, 20, 40, 40, 
                Qt.darkGray)
    
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())
