import sys
import random
import os
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
    value = []
    tp = []
    picName = []
    lblPic = []
    logStr = ''
    triggeredNum = 0
    timeRes = 0
    
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
                
        self.ui.pushButton.clicked.connect(self.finish)
                
    def finish(self):
        self.timeRes = self.timeSeconds
        self.timeSeconds = 0
                
    def mixXml(self):
        # read xml and mix the lines
        self.linesMixed = []
        self.r = open("db4.xml", 'r', encoding='utf-8')
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
            # value
            self.value.append(int(self.linesArr[line].getAttribute('pnt')))
            # reading type
            self.tp.append(self.linesArr[line].getAttribute('type'))
            # adding picture name if any
            if self.linesArr[line].hasAttribute('pic'):
                self.picName.append(self.linesArr[line].getAttribute('pic'))
            else:
                self.picName.append('empty')
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
            # adding picture
            if self.picName[line] != 'empty':
                self.lblPic.append(QtWidgets.QLabel(self.ui.scrollAreaWidgetContents))
                self.lblPic[line].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.lblPic[line].setPixmap(QtGui.QPixmap(os.getcwd() + "/" + self.picName[line]))
                self.verticalLayout.addWidget(self.lblPic[line])
            else:
                self.lblPic.append(QtWidgets.QLabel(self.ui.scrollAreaWidgetContents))
            # adding button group
            self.bgrs.append(QtWidgets.QButtonGroup(self.ui.centralwidget))
            if self.tp[line] == 'chb':
                self.bgrs[line].setExclusive(False)
                self.correct[line] = self.correct[line].split('**?**')
            # click counter
            self.bgrs[line].buttonClicked.connect(self.increaseNum)
            for v in range(0, len(self.variants[line])):
                # check br/chb
                if self.tp[line] == 'rb':
                    self.rbs[line][v] = QtWidgets.QRadioButton(self.ui.scrollAreaWidgetContents)
                elif self.tp[line] == 'chb':
                    self.rbs[line][v] = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents)
                self.bgrs[line].addButton(self.rbs[line][v])
                self.rbs[line][v].setText(self.variants[line][v])
                self.verticalLayout.addWidget(self.rbs[line][v])
    
    def increaseNum(self):
        self.triggeredNum += 1

    def check(self):
        counter = 0
        for group in range(0, len(self.bgrs)):
            # adding questions
            self.logStr += self.labels[group] + '\n'
            # check rb/chb
            if self.tp[group] == 'rb':
                correctThis = '--'
                for rb in self.bgrs[group].buttons():
                    # adding variants
                    self.logStr += '\t' + rb.text() + '\n'
                    if rb.isChecked():
                        if rb.text() == self.correct[group]:
                            correctThis = rb.text()
                            counter += self.value[group]
            elif self.tp[group] == 'chb':
                correctThis = []
                chbCor = []
                for rb in self.bgrs[group].buttons():
                    # adding variants
                    self.logStr += '\t' + rb.text() + '\n'
                    if rb.isChecked():
                        # marked checkboxes
                        chbCor.append(rb.text())
                if len(chbCor) == 0:
                    chbCor.append('none')
                chbCor.sort()
                self.correct[group].sort()
                if self.correct[group] == chbCor:
                    counter += self.value[group]
                correctThis = chbCor
                        
            self.logStr += 'Правильный ответ: %s' % self.correct[group] + '\n'
            self.logStr += 'Ответ пользователя: %s' % correctThis + '\n'
            self.logStr += '\n'
        # And this is the result! Rounded to 2 decimal points
        self.result = float(counter/sum(self.value)*100)
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
        file = open("log.txt", 'w', encoding='utf-8')
        file.write("Дата и время записи: ")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        file.write('\n\n')
        file.write(self.logStr)
        file.write('\n')
        file.write("Результат: %.2f" % self.result + " %\n")
        file.write('Выполнено за %d с\n' % (self.timeConstant - self.timeRes))
        file.write('Количество действий: %d' % self.triggeredNum)
        file.close()
        self.triggeredNum = 0
        self.logStr = ''
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
