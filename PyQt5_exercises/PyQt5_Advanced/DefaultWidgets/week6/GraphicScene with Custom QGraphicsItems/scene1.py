from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sceneWidget

class exampleViewClass(QGraphicsView):
    def __init__(self):
        super(exampleViewClass, self).__init__()
        self.s = sceneWidget.exampleSceneClass()
        self.setScene(self.s)
        

    

if __name__=='__main__':
    app = QApplication([])
    w = exampleViewClass()
    w.show()
    app.exec()