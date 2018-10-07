import sys
import random
import os
import io
import time
import subprocess
from functools import partial
import xml.dom.minidom
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from shell import *




class MyWin(QMainWindow):
    lbs = []
    rbs = [''] *100 #[[''] * 10] * 15 # emply list 15x10
    bgrs = []
    labels = []
    variants = []
    correct = []
    value = []
    lEdit = []
    tp = []
    picName = []
    lblPic = []
    triggeredNum = 0
    timeRes = 0
    qu_tag = []   #'self.....qu_tag'

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # self.ui.comboBox.currentIndexChanged.connect(self.selectSurvey, self.ui.comboBox.currentIndex())
        self.ui.qst_cmb.currentIndexChanged.connect(self.selectSurvey, self.ui.qst_cmb.currentIndex())
        self.ui.clipboard_btn.clicked.connect(self.copyIntoClipboard)
        self.ui.svIntoFile_btn.clicked.connect(self.saveFileWindow)
        self.ui.prevQues_btn.clicked.connect(self.goToPrevQuestion)
        # read xmlDOM and fill the scrArea
        self.readToDom()
        
    
    def readToDom(self):
        
        self.tree = ET.parse(os.getcwd() + os.sep + 'Surveys.xml')
        self.root = self.tree.getroot()
        #print(len(self.root[0].getchildren())) # number of "questionnaire" nodes
        for index, ques in enumerate(self.root[0].getchildren()):
            #print(ques.get("name"))
            self.ui.qst_cmb.addItem(str( str(index) +" "+ques.get("name") ))

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            #print(layout.itemAt( i ), '<------->',layout.count())
            widgetToRemove = layout.itemAt( i ).widget()
            if widgetToRemove is not None:
                # remove it from the layout list
                layout.removeWidget( widgetToRemove )
                print(widgetToRemove)
                # remove it from the gui
                widgetToRemove.setParent(None)
        # initially there is no spacer to remove
        try:
            self.removeSpacer()
        except:
            pass

    def copyIntoClipboard(self, infoIntoFile=False):
        info = ""
        for _ in range(self.ui.scr_vrlt.count()):
            wid = self.ui.scr_vrlt.itemAt(_)
            if isinstance(wid, QWidgetItem):
                if isinstance(wid.widget(),  QRadioButton):
                    if wid.widget().isChecked():
                        info +=wid.widget().text()
                        info +='<br/>\n'
                elif isinstance(wid.widget(),  QLabel):
                    info +=wid.widget().text()
                    info +='<br/>\n'
        if infoIntoFile!=True:
            subprocess.run(['clip.exe'], input=info.strip().encode('utf-16'), check=True)
        else:
            return info
        #print(clipb)


    def selectSurvey(self, currIndex):
        # start from readng first question in questionarre
        self.i = 0
        # print(self.ui.scrollArea)
        self.clearLayout(self.ui.scr_vrlt)
        for q_tag in (self.root[0])[currIndex].getchildren():
            q_tag = (self.root[0])[currIndex].getchildren()
            q_tag = q_tag[0]
        self.lbs.append(QLabel(self.ui.scrollAreaWidgetContents))
        self.lbs[self.i].setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbs[self.i].setText('<b>%s</b>' % q_tag.get("text"))
        self.ui.scr_vrlt.addWidget(self.lbs[self.i])
        self.bgrs.append(QButtonGroup(self.ui.scrollArea))

        if q_tag.get('type')=='rb':
            variants = q_tag.get('ans').split("**?**")
            for v in range(0, len( variants )):
                self.rbs[v] = QRadioButton(self.ui.scrollAreaWidgetContents)
                self.bgrs[self.i].addButton(self.rbs[v])
                self.rbs[v].setText( variants[v] )
                self.ui.scr_vrlt.addWidget(self.rbs[v])
        elif q_tag.get('type')=='le':
            self.lEdit = QLineEdit(self.ui.scrollAreaWidgetContents)
            self.lEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
            self.lEdit.setPlaceholderText( q_tag.get('holder') )
            self.ui.scr_vrlt.addWidget( self.lEdit )
        # add next button
        button = QPushButton('Next --->', self)
        self.qu_tag.append(q_tag) # this variable to store previous question tag :)
        button.clicked.connect( lambda: self.nextButton(q_tag, self.i) )
        self.ui.scr_vrlt.addWidget(button)   
        self.i += 1
        self.ui.statusbar.clearMessage()
        self.addSpacer()


    def nextButton(self, tag, i):
        self.removeSpacer()
        self.qu_tag.append(tag) # this variable to store previous question tag :)
        if tag.get("type")=="rb":
            if self.bgrs[i-1].checkedButton() is not None:
                # for but in self.bgrs[i-1].buttons():
                #     but.setEnabled(False)
                buttonWhichWasClicked = self.sender()
                buttonWhichWasClicked.setEnabled(False)
                # if there is no proper question with proper answer
                ques = []
                for qu in tag.getchildren():
                    ques.append(qu.get("g_ans"))
                    #print(qu.get("g_ans"))
                if len(tag.getchildren())!=0 and (self.bgrs[i-1].checkedButton().text() in ques):
                    desired_xml_sibling = ques.index(self.bgrs[i-1].checkedButton().text())
                    self.addWidgetsToInterface( tag[desired_xml_sibling] )
                    buttonWhichWasClicked.setParent(None)
                else:
                    # make button disabled
                    self.ui.statusbar.showMessage("You have reached the end of the survey :)",20000)
        elif tag.get("type")=="le":
            if self.lEdit.text()!="":
                print("is not None")
                #self.lEdit.setEnabled(False)
                buttonWhichWasClicked = self.sender()
                buttonWhichWasClicked.setEnabled(False)
                if len(tag.getchildren())!=0:
                    self.addWidgetsToInterface((tag.getchildren())[0])
                    buttonWhichWasClicked.setParent(None)
                else:
                    self.ui.statusbar.showMessage("You have reached the end of the survey :)",20000)
        last_widget = self.ui.scr_vrlt.itemAt(self.ui.scr_vrlt.count()-1).widget()
        #print(last_widget.isEnabled())
        self.show()
        self.ui.scrollArea.ensureWidgetVisible(last_widget)
        self.addSpacer() 
        #QTimer.singleShot(0, partial(self.ui.scrollArea.ensureWidgetVisible, last_widget))

    def addSpacer(self):
        self.spacer = QtWidgets.QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.scr_vrlt.addItem(self.spacer)
    
    def removeSpacer(self):
        self.ui.scr_vrlt.removeItem(self.spacer)

    def addWidgetsToInterface(self, question):
        q_tag = question
        #print(q_tag.get("text")) ------------------------------------------------
            #print( q_tag.text, " ------ ", q_tag.get('type') )
        self.lbs.append(QLabel(self.ui.scrollAreaWidgetContents))
        self.lbs[self.i].setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbs[self.i].setText('<b>%s</b>' % q_tag.get("text"))
        self.ui.scr_vrlt.addWidget(self.lbs[self.i])
        self.bgrs.append(QButtonGroup(self.ui.centralwidget))

        if q_tag.get('type')=='rb':
            variants = q_tag.get('ans').split("**?**")
            for v in range(0, len( variants )):
                self.rbs[v] = QRadioButton(self.ui.scrollAreaWidgetContents)
                self.bgrs[self.i].addButton(self.rbs[v])
                self.rbs[v].setText( variants[v] )
                self.ui.scr_vrlt.addWidget(self.rbs[v])
        elif q_tag.get('type')=='le':
            self.lEdit = QLineEdit(self.ui.scrollAreaWidgetContents)
            self.lEdit.setPlaceholderText( q_tag.get('holder') )
            self.ui.scr_vrlt.addWidget( self.lEdit )


        # add next button
        button = QPushButton('Next |--->', self)
        button.setParent(self.ui.scrollAreaWidgetContents)
        button.clicked.connect( lambda: self.nextButton(q_tag, self.i) )
        self.ui.scr_vrlt.addWidget(button)
        self.i += 1

    def saveFileWindow(self):
        f, l = QFileDialog.getSaveFileName(parent=w,
            caption="Заголовок окна", directory=QDir.homePath(),
            filter="All (*);;Text file (*.txt *.md)")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(self.copyIntoClipboard(infoIntoFile=True))

    def goToPrevQuestion(self):
        print(self.i)
        if self.i != 1: # check does current question is the first one
            self.removeSpacer()
            ind = self.ui.scr_vrlt.count()-1
            #print(self.ui.scr_vrlt.itemAt(ind).widget())

            while not isinstance(self.ui.scr_vrlt.itemAt(ind).widget(), QLabel):
                widgetToRemove = self.ui.scr_vrlt.itemAt(ind).widget()
                self.ui.scr_vrlt.itemAt(ind).widget().setParent(None)
                self.ui.scr_vrlt.removeWidget( widgetToRemove )
                ind -= 1
            # remove label from the GUI
            self.ui.scr_vrlt.itemAt(ind).widget().setParent(None)
            self.ui.scr_vrlt.removeWidget( widgetToRemove )

            # print('bg')

            # print('end')
            self.i -=1
            button = QPushButton('Next |--->', self)
            button.setParent(self.ui.scrollAreaWidgetContents)
            #print(self.qu_tag)
            # need to use self.qu_tag
            button.clicked.connect(lambda: self.nextButton(self.qu_tag[-1], self.i))
            self.ui.scr_vrlt.addWidget(button)
            self.addSpacer()
            self.qu_tag.pop(-1)
        else:
            print('I will not do it')
        print('goToPrevQuestion')
        # add here code to go for previous q_tag!!!!!!!!!!!!!!
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
