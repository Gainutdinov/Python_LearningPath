#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import QPoint
import sys


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):    
        
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Donut')
        

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawDonut(painter)
        painter.end()
        
        
    def drawDonut(self, painter):
        brush = QBrush(QColor("#535353"))
        painter.setPen(QPen(brush, 0.5))

        painter.setRenderHint(QPainter.Antialiasing)

        h = self.height()
        w = self.width()

        painter.translate(QPoint(w/2, h/2))
         
        rot = 0
       
        while rot < 360.0:
            painter.drawEllipse(-125, -40, 250, 80)
            painter.rotate(5.0)
            rot += 5.0

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
    