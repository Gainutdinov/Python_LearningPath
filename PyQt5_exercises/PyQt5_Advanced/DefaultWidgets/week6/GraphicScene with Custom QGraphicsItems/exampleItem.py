from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class exampleItemClass(QGraphicsItem):
    def __init__(self):
        super(exampleItemClass, self).__init__()
        self.x = 0
        self.y = 0
        self.h = 50
        self.w = 70
        self.width = 8
        self.text = 'None' 
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRectF(self.x, self.y, self.w, self.h)
    
    def paint(self, painter, options, widget):
        painter.setPen(QPen(Qt.black, self.width))
        if self.isSelected():
            painter.setBrush(Qt.red)
        else:
            painter.setBrush(Qt.gray)
        rec = self.boundingRect().adjusted(self.width/2, self.width/2, -self.width/2, -self.width/2)
        painter.drawRect(rec)
        
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.text)
