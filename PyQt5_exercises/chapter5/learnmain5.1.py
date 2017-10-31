import sys
import random
import xml.dom.minidom
from learn3 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):

    text = []
    questions = []
    variants = []
    correct = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textEdit.setFontPointSize(12)  #Solution
        self.ui.textEdit_2.setFontPointSize(12) #Solution
        self.ui.textEdit_3.setFontPointSize(12) #Solution

        self.dom = xml.dom.minidom.parse('C:/Users/temp1/Desktop/git/Python_LearningPath/PyQt5_exercises/chapter5/learn.xml')
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName("text")

        for line in self.linesArr:
            self.text.append(line.childNodes[0].data)
            self.questions.append(line.getAttribute('question'))
            self.variants.append(line.getAttribute('answers').split('**?**'))
            self.correct.append(line.getAttribute('correct'))

        random.shuffle(self.variants[0])
        random.shuffle(self.variants[1])
        random.shuffle(self.variants[2])

        self.ui.textEdit.setText(self.text[0])
        self.ui.textEdit_2.setText(self.text[1])
        self.ui.textEdit_3.setText(self.text[2])

        self.ui.label.setText(self.questions[0])
        self.ui.label_2.setText(self.questions[1])
        self.ui.label_3.setText(self.questions[2])

        self.ui.radioButton.setText(self.variants[0][0])
        self.ui.radioButton_2.setText(self.variants[0][1])
        self.ui.radioButton_3.setText(self.variants[0][2])

        self.ui.radioButton_4.setText(self.variants[1][0])
        self.ui.radioButton_5.setText(self.variants[1][1])
        self.ui.radioButton_6.setText(self.variants[1][2])
        
        self.ui.radioButton_7.setText(self.variants[2][0])
        self.ui.radioButton_8.setText(self.variants[2][1])
        self.ui.radioButton_9.setText(self.variants[2][2])

        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)
        
        self.ui.buttonGroup.buttonClicked.connect(self.correctAns1)
        self.ui.buttonGroup_2.buttonClicked.connect(self.correctAns2)
        self.ui.buttonGroup_3.buttonClicked.connect(self.correctAns3)
        
    def correctAns1(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[0]:
                    self.ui.statusbar.showMessage("Correct! Tab 2 is enabled now.", 5000)
                    self.ui.tab_1.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(1, True)
        
    def correctAns2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[1]:
                    self.ui.statusbar.showMessage("Correct! Tab 3 is enabled now.", 5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(2, True)
        
    def correctAns3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[2]:
                    self.ui.statusbar.showMessage("Correct! Done!", 5000)
                    self.ui.tab_3.setEnabled(False)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
