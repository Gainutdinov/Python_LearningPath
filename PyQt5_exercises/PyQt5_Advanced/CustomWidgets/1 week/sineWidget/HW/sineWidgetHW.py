from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sin, cos, tan
import sineWindowHW as ui

class sineWidgetClass(QWidget):
    def __init__(self):
        super(sineWidgetClass, self).__init__()
        self.setWindowTitle('sineWidgetClass')
        self.resize(400,200)

        self.wave_height = 30
        self.wave_len = 20
        self.penWidth = 3
        self.grid = 10
        self.func = sin



    def paintEvent(self, event):
        rec = event.rect()
        painter = QPainter()
        painter.begin(self)

        # paint
        painter.fillRect(rec, Qt.black)

        

        # for i in range(0, rec.height(), self.grid):
        #     painter.drawLine(i, 0, i, rec.height())

        
        painter.setPen(QPen(QBrush(Qt.yellow), self.penWidth))
        prevx = 0
        prevy = (0*self.wave_height) + (rec.height()/2)

        # draw horizontal line
        #for i in range(0, rec.width(), self.grid):
        #        painter.drawLine(0, i, rec.width(), i)

        painter.setPen(QPen(QBrush(Qt.gray), 0.5))
        painter.drawLine(0, prevy, rec.width(), prevy)
        painter.drawLine(rec.width()/2, 0, rec.width()/2, rec.height())
        painter.setFont(QFont('Arial', 8))
        for i in range( int(rec.width()/2), rec.width(), self.grid):
            #painter.drawLine(i, 0, i, rec.height())
            if self.grid > 30:
                painter.drawText( i+3, prevy, str(i-int(rec.width()/2)) )
                painter.drawText( rec.width()-i-6, prevy, str(-(i-int(rec.width()/2))))

        for j in range( 0, rec.height(), self.wave_height):
            #print(j)
            if self.wave_height > 30:
                painter.drawText( rec.width()/2, rec.height()/2+j+8, str(j) )
                painter.drawText( rec.width()/2, rec.height()/2-j-8, str(-(j)) )

        painter.setPen(QPen(QBrush(Qt.yellow), self.penWidth))

        for x in range(1, rec.width()):
            s = self.func((x*0.1)*self.wave_len*0.1)
            #painter.drawPoint( x, s*self.wave_height+(rec.height()/2))
            y = (s*self.wave_height)+(rec.height()/2)
            painter.drawLine(QPointF(prevx, prevy), QPointF(x, y))
            prevx = x
            prevy = y
            
            
        painter.setRenderHint(QPainter.Antialiasing)
        #end
        painter.end()
    
    def setHeight(self, v):
        self.wave_height = v
        self.update()

    def setLength(self, v):
        self.wave_len = v
        self.update()

    def setWidth(self, v):
        self.penWidth = v
        self.update()
    
    def setGrid(self, v):
        self.grid = v
        self.update()

    def setFunc(self,v):
        if v=='Sine':
            self.func = sin
        elif v=='Cosine':
            self.func = cos
        else:
            self.func = tan
        self.update()

class sineWindowClass(QMainWindow, ui.Ui_sineWidgetWindow):
    def __init__(self):
        super(sineWindowClass, self).__init__()
        self.setupUi(self)
        self.sine = sineWidgetClass()
        self.sine_ly.addWidget(self.sine)
        self.hgt_sld.setValue(20)
        self.wdt_sld.setValue(20)


        self.hgt_sld.valueChanged.connect(self.sine.setHeight)
        self.len_sld.valueChanged.connect(self.sine.setLength)
        self.wdt_sld.valueChanged.connect(self.sine.setWidth)
        self.grid_sld.valueChanged.connect(self.sine.setGrid)
        self.func_cmb.currentIndexChanged.connect(lambda: self.sine.setFunc(self.func_cmb.currentText()))
        #self.func_cmb.changeEvent.connect( lambda: self.sine.setGridself.sine.setFunc(self.func_cmb.currentText()))
        #self.func_cmb.valueChanged.connect( lambda self.func_cmb.currentText() : self.sine.setGridself.sine.setFunc)

if __name__=='__main__':
    app = QApplication([])
    w = sineWindowClass()
    w.show()
    app.exec_()