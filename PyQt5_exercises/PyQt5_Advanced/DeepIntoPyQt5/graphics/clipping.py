#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect
import sys

class Example(QWidget):
  
    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):
        
        self.rotate = 1
        self.pos_x = 8
        self.pos_y = 8
        self.radius = 60

        self.delta = [1, 1]
        self.timerId = self.startTimer(15)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Clipping')
        self.show()


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawObjects(painter)
        painter.end()


    def drawObjects(self, painter):

        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        rect = QRect(-100, -40, 200, 80)      

        painter.translate(w/2, h/2)
        painter.rotate(self.rotate)
        painter.drawRect(rect)
 
        brush = QBrush(QColor(110, 110, 110))
        painter.setBrush(brush)
        
        painter.setClipRect(rect)

        painter.resetTransform()
        painter.drawEllipse(self.pos_x, self.pos_y, 
                self.radius, self.radius)
        
        painter.setBrush(Qt.NoBrush)
        
        painter.setClipping(False)
        painter.drawEllipse(self.pos_x, self.pos_y, 
                self.radius, self.radius)

        
    def timerEvent(self, event):
        
        self.step()
        self.repaint()
        
        
    def step(self):
    
        w = self.width()
        h = self.height()
         
        if self.pos_x < 0:
            self.delta[0] = 1
            
        elif self.pos_x > w - self.radius:
            self.delta[0] = -1
       
        if self.pos_y < 0:
            self.delta[1] = 1
            
        elif self.pos_y > h - self.radius:
            self.delta[1] = -1
       
        self.pos_x += self.delta[0]
        self.pos_y += self.delta[1]
        
        self.rotate = self.rotate + 1
        
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())