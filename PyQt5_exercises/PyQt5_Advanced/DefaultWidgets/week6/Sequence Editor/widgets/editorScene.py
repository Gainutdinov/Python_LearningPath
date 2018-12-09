from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from . import editorItem

class editorSceneClass(QGraphicsScene):
    def __init__(self):
        super(editorSceneClass, self).__init__()
        self.setSceneRect(-1000, -1000, 2000, 2000)
        self.grid = 30

    def drawBackground(self, painter, rect):
        if False:
            painter = QPainter()
        painter.fillRect(rect, QColor(30, 30, 30))
        left = int(rect.left()) - int(rect.left() % self.grid)
        top = int(rect.top()) - int(rect.top() % self.grid)
        right = int(rect.right())
        bottom = int(rect.bottom())
        lines = []
        for x in range(left, right, self.grid):
            lines.append(QLineF(x, top, x, bottom))
        for y in range(top, bottom, self.grid):
            lines.append(QLineF(left, y, right, y))
        
        painter.setPen(QPen(QColor(100,100,100), 1))
        painter.drawLines(lines)