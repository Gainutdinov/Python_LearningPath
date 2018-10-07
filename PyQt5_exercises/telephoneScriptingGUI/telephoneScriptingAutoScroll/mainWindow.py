import sys
import random
import os
import io
import time
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
    logStr = ''
    triggeredNum = 0
    timeRes = 0

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # self.ui.comboBox.currentIndexChanged.connect(self.selectSurvey, self.ui.comboBox.currentIndex())
        self.ui.qst_cmb.currentIndexChanged.connect(self.selectSurvey, self.ui.qst_cmb.currentIndex())

        # read xmlDOM and fill the scrArea
        self.readToDom()

    
    def readToDom(self):
        
        self.tree = ET.parse(os.getcwd() + os.sep + 'Surveys.xml')
        self.root = self.tree.getroot()
        #print(len(self.root[0].getchildren())) # number of "questionnaire" nodes
        for index, ques in enumerate(self.root[0].getchildren()):
            #print(ques.get("name"))
            self.ui.qst_cmb.addItem(str( str(index) +" "+ques.get("name") ))

        # QBgroup=QButtonGroup()
        # for _ in self.root[0].getchildren()[self.ui.qst_cmb.currentIndex()]:
        #     label = QLabel(_.get("text"))
        #     label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        #     self.ui.scr_vrlt.addWidget(label)
        #     for an in _.get("ans").split("**?**"):
        #         rdButton = QRadioButton(an)
        #         QBgroup.addButton(rdButton)
        #         self.ui.scr_vrlt.addWidget(rdButton)
        #         print(QBgroup)
        #     qspacerItem = QtWidgets.QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #self.selectSurvey(self.ui.qst_cmb.get)
        #self.ui.scr_vrlt.addItem(qspacerItem)
            
                #self.ui.scr_vrlt.addWidget(QBgroup)
        #print(self.root[0].getchildren())
        # button.clicked.connect( lambda: self.nextButton(q_tag, self.i) )
        # self.verticalLayout.addWidget(button)   

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt( i ).widget()
            # remove it from the layout list
            layout.removeWidget( widgetToRemove )
            # remove it from the gui
            widgetToRemove.setParent( None )

    def selectSurvey(self, currIndex):
        #print('changed')
        #print( (self.root[0])[currIndex] )
        self.i = 0
        print(self.ui.scrollArea)
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
            self.lEdit = QLineEdit(self.ui.scrollArea)
            self.lEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
            self.lEdit.setPlaceholderText( q_tag.get('holder') )
            self.ui.scr_vrlt.addWidget( self.lEdit )
        # add next button
        button = QPushButton('Next --->', self)
        button.clicked.connect( lambda: self.nextButton(q_tag, self.i) )
        self.ui.scr_vrlt.addWidget(button)   
        self.i += 1
        self.ui.statusbar.clearMessage()

        qspacerItem = QtWidgets.QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.scr_vrlt.addItem(qspacerItem)

    def nextButton(self, tag, i):
        #print('nextButton ---> ', i-1)
        #print(tag.get("type"))
        #print(type(self.bgrs[i-1].buttons()))
        #print(self.sender())
        if tag.get("type")=="rb":
            if self.bgrs[i-1].checkedButton() is not None:
                # for but in self.bgrs[i-1].buttons():
                #     but.setEnabled(False)
                buttonWhichWasClicked = self.sender()
                buttonWhichWasClicked.setEnabled(False)
                
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
                self.lEdit.setEnabled(False)
                buttonWhichWasClicked = self.sender()
                buttonWhichWasClicked.setEnabled(False)
                if len(tag.getchildren())!=0:
                    self.addWidgetsToInterface((tag.getchildren())[0])
                    buttonWhichWasClicked.setParent(None)
                else:
                    self.ui.statusbar.showMessage("You have reached the end of the survey :)",20000)

        QTimer.singleShot(10, self.show_last)
        # vbar = self.ui.scrArea.verticalScrollBar().maximum() #.verticalScrollBar()
        # if vbar != 0:
        #     print('000')
        #     self.ui.scrArea.scroll(vbar)
        #     self.ui.scrArea.update()
        #self.ui.scrArea.update()
        #self.ui.scrArea.scrollContentsBy(self,)
        #vbar.ensureWidgetVisible(self.verticalLayout.itemAt(self.verticalLayout.count()-1).widget())
        #print( vbar )
        #vbar.ensureWidgetVisible(self.verticalLayout.itemAt(self.verticalLayout.count()-1).widget())      
                

    def addWidgetsToInterface(self, question):
        q_tag = question
        print(q_tag.get("text"))
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
            self.lEdit = QLineEdit(self.ui.centralwidget)
            self.lEdit.setPlaceholderText( q_tag.get('holder') )
            self.ui.scr_vrlt.addWidget( self.lEdit )


        # add next button
        button = QPushButton('Next |--->', self)
        button.clicked.connect( lambda: self.nextButton(q_tag, self.i) )
        self.ui.scr_vrlt.addWidget(button)
        self.i += 1

        
        # vbar = self.ui.scrArea().QtWidget()

        # print(vbar)(
        
        # vbar.setValue(vbar.maximum())

    def show_last(self):
        print('hhhhh')
        self.ui.scrollArea.ensureWidgetVisible(self.ui.scr_vrlt.itemAt(self.ui.scr_vrlt.count()-1).widget())
        bar = self.ui.scrollArea.verticalScrollBar()
        bar.setValue(bar.maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWin()
    w.show()
    QTimer.singleShot(1000, w.addWidgetsToInterface)
    app.exec_()


# https://gist.github.com/altendky/42323d70323b982ab511feb208abcb64

