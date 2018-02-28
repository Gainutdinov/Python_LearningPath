import sys
import random
import os
import xml.dom.minidom
from shell import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    
    lbs = []
    rbs = [] # [[''] * 10] * 15 # emply list 15x10 (numQ x numV)
    numQ = 0
    numV = 0
    bgrs = []
    labels = [] 
    variants = []
    correct = []
    clickedAnswer = 0
    checkList = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.progressBar = QtWidgets.QProgressBar(self.ui.statusbar)
        #self.ui.statusbar.addWidget(self.progressBar)

        self.progressBar = QtWidgets.QProgressBar(self.ui.centralwidget)
        #self.progressBar.setMaximumSize(QtCore.QSize(75, 75))
        self.progressBar.setObjectName("ProgressBar")
        self.progressBar.setGeometry(50, 50, 20, 25)
        self.ui.gridLayout.addWidget(self.progressBar,1,0,1,1)
        
        
        #substitute statusbar with labelStasus cause statusbar doesn't support rich text
        self.labelStatus = QtWidgets.QLabel(self.ui.statusbar)
        self.ui.statusbar.addWidget(self.labelStatus)

        # xml handling (read & mix)
        self.mixXml()
        # read to DOM
        self.readToDom()
        # assigning layout to the scrollarea
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # dinamically set up 2d array depending on the xml.db
        self.rbs = [[''] * (self.numV+1)] * self.numQ


        # adding widgets to the scrollarea
        self.addWidgetsToInterface()
                
        self.ui.pushButton.clicked.connect(self.check)
                
    def mixXml(self):
        # read xml and mix the lines
        self.linesMixed = []
        self.r = open("db.xml", 'r', encoding='utf-8')
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
        self.linesArr = self.collection.getElementsByTagName("q")
        self.numQ = len(self.linesArr)  #added
        for line in range(0, len(self.linesArr)):
            # label's text
            self.labels.append(self.linesArr[line].childNodes[0].data)
            # variants' text
            if (len(self.linesArr[line].getAttribute('ans').split('**?**'))>self.numV):
                self.numV = len(self.linesArr[line].getAttribute('ans').split('**?**'))
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

            self.bgrs[line].buttonClicked.connect(self.progressUpdate) 

            for v in range(0, len(self.variants[line])):
                self.rbs[line][v] = QtWidgets.QRadioButton(self.ui.scrollAreaWidgetContents)
                self.bgrs[line].addButton(self.rbs[line][v])
                self.rbs[line][v].setText(self.variants[line][v])
                self.verticalLayout.addWidget(self.rbs[line][v])
    
    #group.buttonClicked['QAbstractButton *'].connect(self.groupButtonClicked)
    def progressUpdate(self):
        counterPrgr = 0
        for bg in self.bgrs:
            for rb in bg.buttons():
                if rb.isChecked():
                    counterPrgr += 1
                    self.progressBar.setValue( int(counterPrgr/len(self.labels)*100) )
                    self.progressBar.update() 


    def check(self):
        counter = 0
        for group in range(0, len(self.bgrs)):
            for rb in self.bgrs[group].buttons():
                if rb.isChecked():
                    #clickedAnswer +=1
                    if rb.text() == self.correct[group]:
                        counter += 1
        # And this is the result! Rounded to 2 decimal points
        result = round(float(counter/len(self.bgrs)*100),2)
        #if (clickedAnswer!=0): 
        #    self.progressBar.setValue((clickedAnswer*100)/self.numQ)
        if (result<=50): #red
            message = "Your result is " + "<b style=color:'red';>%.2f</b>" % float(counter/len(self.bgrs)*100) + "%" 
        elif (result<=75): #yellow
            message = "Your result is " + "<b style=color:'yellow';>%.2f</b>" % float(counter/len(self.bgrs)*100) + "%" 
        else: #green
            message = "Your result is " + "<b style=color:'green';>%.2f</b>" % float(counter/len(self.bgrs)*100) + "%" 

        self.labelStatus.setText(message)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
