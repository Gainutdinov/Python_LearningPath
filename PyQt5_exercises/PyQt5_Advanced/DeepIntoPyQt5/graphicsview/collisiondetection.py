#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsItem, 
        QGraphicsScene, QGraphicsView)
from PyQt5.QtGui import QPainter, QPainterPath, QPolygonF, QBrush
from PyQt5.QtCore import Qt, QPointF
import sys


class Item(QGraphicsItem):

    def __init__(self):
        super().__init__()
        
        self.brush = None
        self.createPolygon()
        
        
    def createPolygon(self):
    
        self.polygon = QPolygonF()
        self.polygon.append(QPointF(130, 140))
        self.polygon.append(QPointF(180, 170))
        self.polygon.append(QPointF(180, 140))
        self.polygon.append(QPointF(220, 110))
        self.polygon.append(QPointF(140, 100))
        
 
    def shape(self):
    
        path = QPainterPath()
        path.addPolygon(self.polygon)
        return path
        

    def paint(self, painter, option, widget):
    
        if self.brush:
            painter.setBrush(self.brush)
            
        painter.drawPolygon(self.polygon)
        

    def setBrush(self, brush):
    
        self.brush = brush
        

    def boundingRect(self):
        
        return self.polygon.boundingRect()


class MyView(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.initView()
        self.initScene()
        self.checkCollisions()        
        
        
    def initView(self):
    
        self.setWindowTitle("Collision detection")
        self.setRenderHint(QPainter.Antialiasing)
        self.setGeometry(300, 300, 300, 250)

        
    def initScene(self):
    
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 300, 250)
        
        self.item = Item()
        
        self.scene.addEllipse(160, 60, 40, 40)
        self.scene.addEllipse(80, 80, 80, 80)
        self.scene.addEllipse(150, 120, 60, 60)
        self.scene.addEllipse(150, 165, 50, 50)

        self.scene.addItem(self.item)
        self.setScene(self.scene)
        
        
    def checkCollisions(self):
        
        items = self.scene.items()
        
        brush = QBrush(Qt.SolidPattern)
        brush.setStyle(Qt.HorPattern)
        
        for i in range(len(items)):
            item = items[i]

            if self.scene.collidingItems(item):
                item.setBrush(brush)

if __name__ == "__main__":
    app = QApplication([])
    view = MyView()
    view.show()
    sys.exit(app.exec())
