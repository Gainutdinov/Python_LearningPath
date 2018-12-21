#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys

trs = (
    ( 0.0, 0.15, 0.30, 0.5, 0.65, 0.80, 0.9, 1.0 ),
    ( 1.0, 0.0,  0.15, 0.30, 0.5, 0.65, 0.8, 0.9 ),
    ( 0.9, 1.0,  0.0,  0.15, 0.3, 0.5, 0.65, 0.8 ),
    ( 0.8, 0.9,  1.0,  0.0,  0.15, 0.3, 0.5, 0.65 ),
    ( 0.65, 0.8, 0.9,  1.0,  0.0,  0.15, 0.3, 0.5 ),
    ( 0.5, 0.65, 0.8, 0.9, 1.0,  0.0,  0.15, 0.3 ),
    ( 0.3, 0.5, 0.65, 0.8, 0.9, 1.0,  0.0,  0.15 ),
    ( 0.15, 0.3, 0.5, 0.65, 0.8, 0.9, 1.0,  0.0, )
)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()               


    def initUI(self):
    
        self.count = 0
        self.timerId = self.startTimer(105)
        
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Waiting')


    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.drawLines(painter)
        painter.end()


    def drawLines(self, painter):

        pen = QPen()
        pen.setWidth(3)
        pen.setCapStyle(Qt.RoundCap)

        w = self.width()
        h = self.height()

        painter.translate(w/2, h/2)
        painter.setPen(pen)

        for i in range(8):
            painter.setOpacity(trs[self.count%8][i])
            painter.drawLine(0.0, -10.0, 0.0, -80.0)
            painter.rotate(45)


    def timerEvent(self, event):
        self.count = self.count + 1
        self.repaint()        

       
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())


