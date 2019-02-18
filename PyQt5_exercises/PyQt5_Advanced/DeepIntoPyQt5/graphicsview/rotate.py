#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QApplication, QSlider,
        QGraphicsRectItem, QGraphicsScene, QGraphicsItem, 
        QGraphicsView, QVBoxLayout)
from PyQt5.QtGui import QPainter, QTransform, QColor
from PyQt5.QtCore import Qt
import sys
      

class Rectangle(QGraphicsRectItem):
    
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        
        self.setBrush(QColor(250, 50, 0))
        self.setPen(QColor(250, 50, 0))
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setCursor(Qt.SizeAllCursor)
        
        self.tx = 200
        self.ty = 200
        
        
    def doRotate(self, alfa):
        
        tr = QTransform()
        tr.translate(self.tx, self.ty)
        tr.rotate(alfa)
        tr.translate(-self.tx, -self.ty)
        
        self.setTransform(tr)
                       

class View(QGraphicsView):
    
    def __init__(self):
        super(View, self).__init__()
             
        self.setRenderHint(QPainter.Antialiasing)
        
        self.initScene()
        
        
    def initScene(self):     

        self.scene = QGraphicsScene()
        self.setSceneRect(0, 0, 400, 400)  
             
        self.rect = Rectangle(150, 150, 100, 100)        
        self.scene.addItem(self.rect)

        self.setScene(self.scene)  


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Rotation")
        self.setGeometry(150, 150, 300, 300)
       
        self.initUI()
       
       
    def initUI(self):   

        vbox = QVBoxLayout()
        
        self.view = View()
        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(-180, 180)
        
        sld.valueChanged[int].connect(self.changeValue)                      
        
        vbox.addWidget(self.view)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        
    
    def changeValue(self, value):

        self.view.rect.doRotate(value)     


if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())
