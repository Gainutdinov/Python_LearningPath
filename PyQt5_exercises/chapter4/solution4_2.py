import sys
from menu0 import *
from PyQt5 import QtCore, QtGui, QtWidgets
 
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.checker = False

        self.ui.actionExit.triggered.connect(self.closeProg)

    def closeProg(self):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.checker = True
            self.close()

    def closeEvent(self, e):
        if self.checker:
            e.accept()
        else:
            e.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())