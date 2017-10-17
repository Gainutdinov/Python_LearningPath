import sys
from myinterface2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My Title')
        self.ui.PushButton.clicked.connect(self.myFunction)
    def myFunction(self):
        self.ui.label.setText("Length of the text is %d" % len(self.ui.lineEdit.text()))   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
