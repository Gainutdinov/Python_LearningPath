import sys
from learn1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)
        self.ui.radioButton_2.clicked.connect(self.correctAns1)
        self.ui.radioButton_6.clicked.connect(self.correctAns2)
        self.ui.radioButton_9.clicked.connect(self.correctAns3)

    def correctAns1(self):
        self.ui.statusbar.showMessage("Correct! Tab 2 is enabled now.", 5000)
        self.ui.tab_1.setEnabled(False)
        self.ui.Tab3.setTabEnabled(1, True)

    def correctAns2(self):
        self.ui.statusbar.showMessage("Correct! Tab 3 is enabled now.", 5000)
        self.ui.tab_2.setEnabled(False)
        self.ui.Tab3.setTabEnabled(2, True)

    def correctAns3(self):
        self.ui.statusbar.showMessage("Correct! Done!", 5000)
        self.ui.tab_3.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
