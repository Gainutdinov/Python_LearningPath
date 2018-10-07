from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import computerArea_ui as ui
import math

class computeAreaClass(QMainWindow, ui.Ui_computeArea):
    def __init__(self):
        super(computeAreaClass, self).__init__()
        self.setupUi(self)
        # variables
        self.live = False        
        #connects
        self.shape_cbb.currentIndexChanged.connect(self.updateUi)
        self.compute_btn.clicked.connect(self.compute)

        if self.live:
            self.compute_btn.setVisible(0)
            self.sq_heigth_spx.valueChanged.connect(self.compute)
            self.sq_width_spx.valueChanged.connect(self.compute)
            self.cr_radius_spx.valueChanged.connect(self.compute)

        #start
        self.updateUi()


    def compute(self):
        if (self.shape_cbb.currentIndex() == 0):
            self.computeSquare()
        elif (self.shape_cbb.currentIndex() == 1):
            self.computeCircle()

    def computeSquare(self):
        w = self.sq_width_spx.value()
        h = self.sq_heigth_spx.value()
        area = w * h
        self.showResult(area)

    def computeCircle(self):
        r = self.cr_radius_spx.value()
        area = math.pi * (r**2)
        self.showResult(area)

    

    def updateUi(self):
        self.sq_gb.setVisible(self.shape_cbb.currentIndex() == 0)
        self.cr_gb.setVisible(self.shape_cbb.currentIndex() == 1)
        self.compute()

    def showResult(self, result):
        self.result_lb.setText('Result: %.3f' % result)

if __name__=='__main__':
    app = QApplication([])
    w = computeAreaClass()
    w.show()
    app.exec_()
