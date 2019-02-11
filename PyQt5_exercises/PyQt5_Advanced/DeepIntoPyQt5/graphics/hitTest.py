#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QThread, QRect
import time
import sys


class MyThread(QThread):
  
    fading = pyqtSignal(float, name='fading') 
    
    def __init__(self):
        super().__init__()
        
        self.alpha = 1
        

    def run(self):
    
        print("Thread started")
        
        while self.alpha >= 0:
	  
            self.alpha -= 0.01
            self.fading.emit(self.alpha)
            time.sleep(0.1)
            
        print("Thread ended")


class Example(QWidget):
  
    def __init__(self):
        super().__init__()

        self.initUI()
        
    
    def initUI(self):
        self.rect = QRect(20, 20, 80, 80)
        self.alpha = 1
        self.m = MyThread()
        self.m.fading.connect(self.fade)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Hit test')

        
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        self.drawRectangle(painter)
        painter.end()
        
        
    def fade(self, alpha):
    
        self.alpha = alpha
        self.repaint()
        
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton \
            and self.alpha==1:
            x = e.x()
            y = e.y()
            if self.rect.contains(x, y):
               if not self.m.isRunning():   
                   self.m.start()


    def drawRectangle(self, painter):
        painter.setOpacity(self.alpha)
        painter.setBrush(QBrush(Qt.black))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect)
        
        
    def closeEvent(self, e):
        
        if self.m.isRunning():
            self.m.quit()
    
    
       
if __name__=='__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())