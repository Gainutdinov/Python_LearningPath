#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QFont
import sys

lyrics = [
"Some folks are born made to wave the flag",
"Ooh, they're red, white and blue",
"And when the band plays 'Hail to the chief'",
"Ooh, they point the cannon at you, Lord",
"It ain't me, it ain't me, I ain't no senator's son, son",
"It ain't me, it ain't me, I ain't no senator's son, son"
]

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 430, 240)
        self.setWindowTitle('Soulmate')
        

    def paintEvent(self, event):
        
        painter = QPainter()
        painter.begin(self)
        self.drawLyrics(painter)
        painter.end()
        
        
    def drawLyrics(self, painter):

        painter.setFont(QFont('Purisa', 11))
        painter.drawText(20, 30, lyrics[0])
        painter.drawText(20, 60, lyrics[1])
        painter.drawText(20, 120, lyrics[2])
        painter.drawText(20, 150, lyrics[3])
        painter.drawText(20, 180, lyrics[4])
        painter.drawText(20, 210, lyrics[5])

if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())
