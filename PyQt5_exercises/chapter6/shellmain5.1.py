import sys
import random
import os
import time
import xml.dom.minidom
from shell2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    
    lbs = []
    rbs = [[''] * 10] * 15 # emply list 15x10
    bgrs = []
    labels = [] 
    variants = []
    correct = []
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.progressBar = QtWidgets.QProgressBar(self.ui.centralwidget)
        #self.progressBar.setMaximumSize(QtCore.QSize(75, 75))
        self.progressBar.setObjectName("ProgressBar")
        self.progressBar.setGeometry(50, 50, 20, 25)
        self.ui.gridLayout.addWidget(self.progressBar,3,0,1,1)

        self.mythread1 = AThread()
        
        # xml handling (read & mix)
        self.mixXml()
        # read to DOM
        self.readToDom()
        # assigning layout to the scrollarea
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # adding widgets to the scrollarea
        self.addWidgetsToInterface()
        
        self.mythread1.partDone.connect(self.updater)
        self.start1()
                
        self.ui.pushButton.clicked.connect(self.check)
                
    def mixXml(self):
        # read xml and mix the lines
        self.linesMixed = []
        self.r = open("db1.xml", 'r', encoding='utf-8')
        self.fileRead = self.r.readlines()
        for line in range(2, len(self.fileRead)-1):
            self.linesMixed.append(self.fileRead[line])
        random.shuffle(self.linesMixed)
        self.r.close()
        
        # write temporary xml with new mixed lines
        self.w = open("temp.xml", 'w', encoding='utf-8')
        self.w.write('''<?xml version="1.0" encoding="utf-8"?>\n<content>\n''')
        for line in self.linesMixed:
            self.w.write('%s' % line)
        self.w.write('</content>')
        self.w.close()
        
    def readToDom(self):
        # read to DOM
        self.dom = xml.dom.minidom.parse('temp.xml')
        self.collection = self.dom.documentElement
        self.mythread1.timeSeconds = self.collection.getElementsByTagName("time")[0].childNodes[0].data
        self.linesArr = self.collection.getElementsByTagName("q")
        for line in range(0, len(self.linesArr)):
            # label's text
            self.labels.append(self.linesArr[line].childNodes[0].data)
            # variants' text
            self.variants.append(self.linesArr[line].getAttribute('ans').split('**?**'))
            # correct answer
            self.correct.append(self.linesArr[line].getAttribute('cor'))
        # Mix variants
        for variant in self.variants:
            random.shuffle(variant)
        # Deleting temporary file
        os.remove('temp.xml')
    
    def addWidgetsToInterface(self):
        # adding widgets to the scrollarea
        for line in range (0, len(self.labels)):
            self.lbs.append(QtWidgets.QLabel(self.ui.scrollAreaWidgetContents))
            self.lbs[line].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.lbs[line].setText('<b>%s</b>' % self.labels[line])
            self.verticalLayout.addWidget(self.lbs[line])
            self.bgrs.append(QtWidgets.QButtonGroup(self.ui.centralwidget))
            for v in range(0, len(self.variants[line])):
                self.rbs[line][v] = QtWidgets.QRadioButton(self.ui.scrollAreaWidgetContents)
                self.bgrs[line].addButton(self.rbs[line][v])
                self.rbs[line][v].setText(self.variants[line][v])
                self.verticalLayout.addWidget(self.rbs[line][v])
    
    def check(self):
        counter = 0
        for group in range(0, len(self.bgrs)):
            for rb in self.bgrs[group].buttons():
                if rb.isChecked():
                    if rb.text() == self.correct[group]:
                        counter += 1
        # And this is the result! Rounded to 2 decimal points
        message = "Your result is " + "%.2f" % float(counter/len(self.bgrs)*100) + "%"
        self.ui.statusbar.setStyleSheet('color: navy; font-weight: bold;')
        self.ui.statusbar.showMessage(message)
                
    def updater(self, val):
        #self.ui.label.setText(self.intToTime(val))
        self.progressBar.setValue( val )
        self.progressBar.setStyleSheet("QProgressBar::chunk { background-color: grey; } QProgressBar{ border: 2px solid grey; border-radius: 5px; text-align: center }")
        self.progressBar.update()
        if int(val) == 100:
            self.check()
            self.ui.scrollArea.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
        
    def start1(self):
        self.mythread1.start()

    # Additional function, if you need to terminate the thread    
    def stop1(self):
        self.mythread1.terminate()

    def intToTime(self, num):
        h = 0
        m = 0
        if num >= 3600:
            h = num // 3600
            num = num % 3600
        if num >= 60:
            m = num // 60
            num = num % 60
        s = num
        str1 = "%d." % h
        if m < 10:
            str1 += "0%d:" % m
        else:
            str1 += "%d:" % m
        if s < 10:
            str1 += "0%d" % s
        else:
            str1 += "%d" % s
        return str1 # returns time as a string

class AThread(QtCore.QThread):
    timeSeconds = 0
    partDone = QtCore.pyqtSignal(int)
    def run(self):
        count = int(self.timeSeconds)
        while count > -1:
            time.sleep(1)
            self.partDone.emit( (int(self.timeSeconds)-count)*100/int(self.timeSeconds) )
            count -= 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
