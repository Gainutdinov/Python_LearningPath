import sys
import random
import os
import io
import time
import stat
import xml.dom.minidom
from shell2 import *
from diatwo import Ui_Dialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5 import QtCore, QtGui, QtWidgets

class StartDialog(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setupUi(self)

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
    minNum = 0
    name1 = ''
    group1 = ''
    timeRes = 0
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
		
        while self.name1 == '' or self.group1 == '':
            dialog = StartDialog(self)
            if dialog.exec_():
                self.name1 = dialog.lineEdit.text()
                self.group1 = dialog.lineEdit_2.text()

        self.duration = 0
        self.playerState = QMediaPlayer.StoppedState
        self.timerAud = QtCore.QTimer(self)
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        # frame with buttons play and stop, and duration label
        self.frame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.labelDuration = QtWidgets.QLabel(self.frame)
        self.labelDuration.setText('0')
        self.horizontalLayout.addWidget(self.labelDuration)

        # creating timer
        self.timer = QtCore.QTimer(self)
        # xml handling (read & mix)
        self.mixXml()
        # read to DOM
        self.readToDom()
        # assigning layout to the scrollarea
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # adding title
        self.trTitle = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.trTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.trTitle.setText('')
        # adding standart widgets for listening
        self.verticalLayout.addWidget(self.trTitle)
        self.lblAud = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.lblAud.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblAud.setText('')
        self.horizontalSlider = QtWidgets.QSlider(self.ui.scrollAreaWidgetContents)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        # adding frame
        self.verticalLayout.addWidget(self.lblAud)
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout.addWidget(self.frame)

        self.pushButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.pushButton_3.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.pushButton_3.setEnabled(False)
        
        # adding widgets to the scrollarea
        self.addWidgetsToInterface()
        self.timer.timeout.connect(lambda: self.updater(self.timeSeconds))
        # starting timer
        self.timer.start(1000)

        self.player.durationChanged.connect(self.durationChanged1)
        self.player.positionChanged.connect(self.positionChanged1)
        self.player.stateChanged.connect(self.setState)
        
        self.horizontalSlider.setRange(0, self.player.duration() / 1000)
        
        self.pushButton.clicked.connect(self.play1)
        self.pushButton_3.clicked.connect(self.stop1)
        
        #self.horizontalSlider.sliderMoved.connect(self.changePosition)
                
        self.ui.pushButton.clicked.connect(self.finish)
                
    def open1(self, filename):
        self.audiofile = filename
        fileInfo = QtCore.QFileInfo(self.audiofile)
        url = QtCore.QUrl.fromLocalFile(fileInfo.absoluteFilePath())
        self.playlist.addMedia(QMediaContent(url))
        self.pushButton.setEnabled(True)

    def play1(self):
        if self.playerState in (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
            self.player.play()
        elif self.playerState == QMediaPlayer.PlayingState:
            self.player.pause()

    def stop1(self):
        self.player.stop()

    def positionChanged1(self, progress):
        progress = progress / 1000
        if not self.horizontalSlider.isSliderDown():
            self.horizontalSlider.setValue(progress)
        self.updateDurationInfo(progress)

    def durationChanged1(self, duration):
        duration = duration / 1000
        self.duration = duration
        self.horizontalSlider.setMaximum(duration)

    def updateDurationInfo(self, currentInfo):
        duration = self.duration
        if currentInfo or duration:
            currentTime = QtCore.QTime((currentInfo/3600)%60, (currentInfo/60)%60, currentInfo%60, (currentInfo*1000)%1000)
            totalTime = QtCore.QTime((duration/3600)%60, (duration/60)%60, duration%60, (duration*1000)%1000);
            format1 = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
            tStr = currentTime.toString(format1) + " / " + totalTime.toString(format1)
        else:
            tStr = ''
        self.labelDuration.setText(tStr)

    def setState(self,state):
        if state != self.playerState:
            self.playerState = state
            if state == QMediaPlayer.StoppedState:
                self.horizontalSlider.setEnabled(False)
                self.pushButton_3.setEnabled(False)
                self.pushButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
            elif state == QMediaPlayer.PlayingState:
                self.horizontalSlider.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
            elif state == QMediaPlayer.PausedState:
                self.horizontalSlider.setEnabled(False)
                self.pushButton_3.setEnabled(True)
                self.pushButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

    def changePosition(self, seconds):
        if self.playerState == QMediaPlayer.PausedState:
            pass
        elif self.playerState == QMediaPlayer.PlayingState:
            self.player.setPosition(seconds * 1000)

    def finish(self):
        self.timeRes = self.timeSeconds
        self.timeSeconds = 0
                
    def mixXml(self):
        # read xml and mix the lines
        self.linesMixed = []
        self.r = open("db6.xml", 'r', encoding='utf-8')
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
        # reading title
        self.title = self.collection.getElementsByTagName("ttl")[0].childNodes[0].data
        self.questAudio = self.collection.getElementsByTagName("aud")[0].childNodes[0].data
        aud = self.collection.getElementsByTagName("aud")[0]
        audFile = aud.getAttribute('src')
        self.open1(audFile)
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
        self.trTitle.setText("Тренажер %s" % self.title)
        self.lblAud.setText("<b>%s</b>" % self.questAudio)
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
            self.logStr += 'Сложность: %d\n' % self.value[group]
            # check rb/chb
            if self.tp[group] == 'rb':
                self.minNum += 1
                correctThis = '--'
                for rb in self.bgrs[group].buttons():
                    # adding variants
                    self.logStr += '\t' + rb.text() + '\n'
                    if rb.isChecked():
                        if rb.text() == self.correct[group]:
                            correctThis = rb.text()
                            counter += self.value[group]
            elif self.tp[group] == 'chb':
                if self.correct[group][0] != 'none':
                    self.minNum += len(self.correct[group])
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
                        
            self.logStr += 'Правильный ответ: %s' % self.listToString(self.correct[group]) + '\n'
            self.logStr += 'Ответ пользователя: %s' % self.listToString(correctThis) + '\n'
            if self.listToString(self.correct[group]) == self.listToString(correctThis):
                self.logStr += 'TRUE\n'
            else:
                self.logStr += 'FALSE\n'
            self.logStr += '\n'
        # And this is the result! Rounded to 2 decimal points
        self.result = float(counter/sum(self.value)*100)
        message = "Your result is " + "%.2f" % self.result + "%"
        self.ui.statusbar.setStyleSheet('color: navy; font-weight: bold;')
        self.ui.statusbar.showMessage(message)
        # creating log file
        self.log()
                
    def listToString(self, getlist):
        if type(getlist).__name__ == 'list':
            string = ''
            for i in getlist:
                string += i + '; '
            string = string[:-2] + '.'
            return string
        else:
            return getlist

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
        logFileName = self.name1 + '_' + self.group1 + '_%.2f' % self.result + '_' + str(self.timeConstant - self.timeRes) + '_%.2f' % (self.triggeredNum/self.minNum*100) + '_' + str(int(round(time.time() * 1000))) + '.txt'
        file = open(logFileName, 'w', encoding='utf-8')
        file.write("Тренажер: %s\n" % self.title)
        file.write("Имя: %s\nГруппа: %s\n" % (self.name1, self.group1))
        file.write("Дата и время записи: ")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        file.write('\n\n')
        file.write(self.logStr)
        file.write('\n')
        file.write("Результат: %.2f" % self.result + " %\n")
        file.write('Выполнено за %d с\n' % (self.timeConstant - self.timeRes))
        # Nubmer of iteractions in percent relative to minimal number of interactions.
        # Minimal number of iteractions equals the quantity of radio buttons
        # multiplied by the quantity of correct variants in questions with check boxes
        # see line 140 and 150-151.
        file.write('Коэффициент интеракций: %.2f' % (self.triggeredNum/self.minNum*100) + ' %')
        # makes log file read only
        os.chmod(os.path.abspath(logFileName), stat.S_IREAD)
        file.close()
        self.triggeredNum = 0
        self.logStr = ''
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
