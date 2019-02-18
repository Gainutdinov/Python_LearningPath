#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QApplication, QGraphicsView, 
        QGraphicsScene)
import sys

class Example(QGraphicsView):
    
    def __init__(self):        
        super().__init__()
              
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Simple")              
              
        self.init()               
        
        
    def init(self):

        self.scene = QGraphicsScene()        
        self.scene.addText("ZetCode")
        self.setScene(self.scene)        

if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())






