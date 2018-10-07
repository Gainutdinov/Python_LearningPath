# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class splineRampWidget(QWidget):
    def __init__(self):
        super(splineRampWidget, self).__init__()
        self.resize(300,200)

        self.lineWidth = 3
        self.pointSize = 10

        self.point1 = QPointF(0, 0)
        self.point2 = QPointF(300, 200)
        self.point3 = QPointF(70, 100)
        self.point4 = QPointF(130, 100)

        self.factor1 = 0.0
        self.factor2 = 1.0
        self.factor3 = .3
        self.factor4 = .6

        self.dragged = None

        self.region1 = QRect()
        self.region2 = QRect()
        self.region3 = QRect()
        self.region4 = QRect()
        self.regionSize = 40
        self.updateRegions()

    
    def updateRegions(self):
        
        self.region1 = QRect(0,0, self.regionSize, self.regionSize)
        self.region1.moveCenter(self.point1.toPoint())
        
        self.region2 = QRect(0,0, self.regionSize, self.regionSize)
        self.region2.moveCenter(self.point2.toPoint())

        self.region3 = QRect(0,0, self.regionSize, self.regionSize)
        self.region3.moveCenter(self.point3.toPoint())

        self.region4 = QRect(0,0, self.regionSize, self.regionSize)
        self.region4.moveCenter(self.point4.toPoint())

        self.factor1 = self.point1.y() / float(self.size().height())
        self.factor2 = self.point2.y() / float(self.size().height())
        self.factor3 = self.point3.y() / float(self.size().height())
        self.factor4 = self.point4.y() / float(self.size().height())
        #print(self.factor1, self.factor2)

    
    def paintEvent(self, event):
        RGBint = self.size().height() * self.size().width()
        Green =  RGBint & 255
        Red = (RGBint >> 8) & 255
        Blue =   (RGBint >> 16) & 255
        # print(Blue,' ',Green,' ',Red)
        rec = event.rect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QColor(Red,Green,Blue)) #Qt.darkGray)
        path = QPainterPath()
        path.moveTo(self.point1)

        # draw vertical lines for the window
        painter.setPen(QPen(QBrush(Qt.black), 0.5))
        painter.setFont(QFont('Arial', 8))
        if rec.width() > 450:
            for i in range(0, rec.width(), int(rec.width()/20) ):
                painter.drawText(i, 15, str(i))
        painter.setPen(QPen(QBrush(Qt.black), 0.5))
        for i in range(0, rec.width(), int(rec.width()/20) ): # self.grid = 10
            painter.drawLine(i, 0, i, rec.height())

        path.lineTo(self.point3)
        path.lineTo(self.point4)
        path.lineTo(self.point2)
        painter.setPen(QPen(QBrush(Qt.white), self.lineWidth))
        painter.drawPath(path)
        painter.setBrush(QBrush(Qt.green))
        painter.drawEllipse(self.point1, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point2, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point3, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point4, self.pointSize, self.pointSize)

        painter.setPen(QPen(QBrush(Qt.blue), 1))
        painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.region1)
        # painter.drawRect(self.region2)
        # painter.drawRect(self.region3)
        # painter.drawRect(self.region4)
        painter.end()

    def mousePressEvent(self, event):
        if self.region1.contains(event.pos()):
            self.dragged = self.point1
        elif self.region2.contains(event.pos()):
            self.dragged = self.point2
        elif self.region3.contains(event.pos()):
            self.dragged = self.point3
        elif self.region4.contains(event.pos()):
            self.dragged = self.point4
        super(splineRampWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not self.dragged is None:
            if self.dragged == self.point3:
                y = event.pos().y()
                x = event.pos().x()
                s = self.size()
                self.dragged.setY(min(max(y, 1), s.height()))
                self.dragged.setX(min(max(x, 1), self.point4.x()))
                # self.dragged.setX(min(max(x, 1), self.point4.y()))
                self.update()
            elif self.dragged == self.point4:
                y = event.pos().y()
                x = event.pos().x()
                s = self.size()
                self.dragged.setY(min(max(y, 1), s.height()))
                self.dragged.setX(min(max(x, self.point3.x()), s.width()))
                self.update()
            else:
                y = event.pos().y()
                s = self.size()
                self.dragged.setY(min(max(y, 1), s.height()))
                self.update()
        super(splineRampWidget, self).mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.dragged = None
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).mouseMoveEvent(event)
    
    def resizeEvent(self, event):
        self.point1.setY(event.size().height() * self.factor1)
        self.point2.setY(event.size().height() * self.factor2)
        self.point3.setX(self.size().width()*(self.point3.x() / float(self.size().width())))
        self.point4.setX(self.size().width()*(self.point4.x() / float(self.size().width())))
        self.point2.setX(event.size().width())

        self.updateRegions()
        self.update()
        super(splineRampWidget, self).resizeEvent(event)

    def drawVerticalLines(self):
        print('drawVerticalLines')

if __name__ == "__main__":
    app = QApplication([])
    w = splineRampWidget()
    w.show()
    app.exec_()