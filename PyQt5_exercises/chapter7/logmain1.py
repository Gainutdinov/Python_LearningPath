import sys
import random
import os, stat
import io
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
        # creating timer
        self.timer = QtCore.QTimer(self)
        # xml handling (read & mix)
        self.mixXml()
        # read to DOM
        self.readToDom()
        # assigning layout to the scrollarea
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # adding widgets to the scrollarea
        self.addWidgetsToInterface()
        self.timer.timeout.connect(lambda: self.updater(self.timeSeconds))
        # starting timer
        self.timer.start(1000)
                
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
        # reading timeout to a variable
        self.timeSeconds = int(self.collection.getElementsByTagName("time")[0].childNodes[0].data)
        self.timeConstant = self.timeSeconds
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
        self.result = float(counter/len(self.bgrs)*100)
        message = "Your result is " + "%.2f" % self.result + "%"
        self.ui.statusbar.setStyleSheet('color: navy; font-weight: bold;')
        self.ui.statusbar.showMessage(message)
        # creating log file
        self.log()
                
    def updater(self, val):
        val = self.timeSeconds
        if val == 0:
            self.timer.stop()
            self.check()
            self.ui.scrollArea.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
        self.ui.label.setText(self.intToTime(val))
        self.timeSeconds -= 1
        
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

    def log(self):
        # File is read-only, so make it writeable
        os.chmod(os.path.abspath("log.txt"), stat.S_IWRITE)
        file = open("log.txt", 'a', encoding='utf-8')
        file.write("Дата и время записи: ")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        file.write('\n')
        file.write("Результат: %.2f" % self.result + " %\n")
        file.write('Выполнено за %d секунд' % (self.timeConstant - self.timeSeconds))
        file.write('\n---------------\n')
        # File is writeable, so make it read-only
        os.chmod(os.path.abspath("log.txt"), stat.S_IREAD)      
        file.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
