import sys
import random
from learn2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):

    correct1 = "формальная знаковая система, предназначенная для записи компьютерных программ"
    correct2 = "и естественным языкам, и языкам программирования"
    correct3 = "В программе на языке Python смыслоразличительную роль играет количество отступов от левого края"

    variants1 = ["любая знаковая система", correct1, "любая формальная знаковая система"]
    variants2 = ["только естественным языкам", "только языкам программирования", correct2]
    variants3 = ["В конце каждой строки программы на языке Python должна стоять точка с запятой", "В программе на языке Python не должно быть пустых строк", correct3]

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        random.shuffle(self.variants1)
        random.shuffle(self.variants2)
        random.shuffle(self.variants3)

        self.ui.radioButton.setText(self.variants1[0])
        self.ui.radioButton_2.setText(self.variants1[1])
        self.ui.radioButton_3.setText(self.variants1[2])

        self.ui.radioButton_4.setText(self.variants2[0])
        self.ui.radioButton_5.setText(self.variants2[1])
        self.ui.radioButton_6.setText(self.variants2[2])

        self.ui.radioButton_7.setText(self.variants3[0])
        self.ui.radioButton_8.setText(self.variants3[1])
        self.ui.radioButton_9.setText(self.variants3[2])

        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)

        self.ui.buttonGroup.buttonClicked.connect(self.correctAns1)
        self.ui.buttonGroup_2.buttonClicked.connect(self.correctAns2)
        self.ui.buttonGroup_3.buttonClicked.connect(self.correctAns3)

    def correctAns1(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text() == self.correct1:
                    self.ui.statusbar.showMessage("Correct! Tab 2 is enabled now.", 5000)
                    self.ui.tab_1.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(1, True)

    def correctAns2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct2:
                    self.ui.statusbar.showMessage("Correct! Tab 3 is enabled now.", 5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(2, True)

    def correctAns3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct3:
                    self.ui.statusbar.showMessage("Correct! Done!", 5000)
                    self.ui.tab_3.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
