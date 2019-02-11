#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QImage, QLinearGradient
from PyQt5.QtCore import Qt, QRect
import sys


class Example(QWidget):
  
    def __init__(self):
        super().__init__()

        self.loadImage()
        self.initUI()
        self.createReflectedImage()
        
        
    def loadImage(self):
        
        self.img = QImage("slanec.png")
        
        if self.img.isNull():
            print("Error loading image")
            sys.exit(1)
            
        
    def initUI(self):
        
        self.iw = self.img.width()
        self.ih = self.img.height()
        
        self.setGeometry(200, 200, 300, 400)
        self.setWindowTitle('Reflection')
        self.show()        
        
        
    def createReflectedImage(self):        
    
        self.refImage = QImage(self.iw, self.ih, 
            QImage.Format_ARGB32)
        
        painter = QPainter()
        painter.begin(self.refImage)
        
        painter.drawImage(0, 0, self.img)
        
        mode = QPainter.CompositionMode_DestinationIn
        painter.setCompositionMode(mode)
        
        gradient = QLinearGradient(self.iw/2, 0, self.iw/2, self.ih)

                
        gradient.setColorAt(1, QColor(0, 0, 0))
        gradient.setColorAt(0, Qt.transparent)        
        
        painter.fillRect(0, 0, self.iw, self.ih, gradient)

        painter.end()
        

    def paintEvent(self, event):
      
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()
        
        
    def drawImages(self, painter):
    
        w = self.width()
        h = self.height()
        
        gradient = QLinearGradient(w/2, 0, w/2, h)
        
        gradient.setColorAt(0, Qt.black)
        gradient.setColorAt(1, Qt.darkGray)

        painter.fillRect(0, 0, w, h, gradient)
        
        gap = 30

        rect = QRect(25, 15, self.iw, self.ih)
        painter.drawImage(rect, self.img)
        painter.translate(0, 2*self.ih + gap)
        painter.scale(1, -1)
        
        painter.drawImage(25, 0, self.refImage)
              

if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())

