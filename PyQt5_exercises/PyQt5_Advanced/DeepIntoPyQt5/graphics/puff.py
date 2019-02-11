#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import (QPainter, QBrush, QColor, QPen, QFont, QFontMetrics)
from PyQt5.QtCore import QPoint
import sys

class Example(QWidget):
  
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.h = 1
        self.opacity = 1.0
        self.timerId = self.startTimer(15)
        
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Puff')     
        

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        self.doStep(painter)
        painter.end()


    def doStep(self, painter):

        text = "YourName"

        brush = QBrush(QColor("#575555"))
        painter.setPen(QPen(brush, 1))

        f = QFont("Verdana", self.h)
        f.setWeight(QFont.DemiBold)
        fm = QFontMetrics(f)
        textWidth = fm.width(text)

        painter.setFont(f)

        if self.h > 10:
            self.opacity -= 0.01
            painter.setOpacity(self.opacity)
        
        if self.opacity <= 0:
            self.killTimer(self.timerId)

        h = self.height()
        w = self.width()

        painter.translate(QPoint(w/2, h/2))
        painter.drawText(-textWidth/2, 0, text)
        

    def timerEvent(self, event):
        print('hhh')
        self.h = self.h + 1
        self.repaint()
                
    
       
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())