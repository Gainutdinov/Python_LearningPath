from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class windowClass(QWidget):
    def __init__(self):
        super(windowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.button = QPushButton('Click me')
        layout.addWidget(self.button)
        self.resize(300,200)
        self.button.clicked.connect(self.showMessage2)



    def showMessage2(self):
        i = QInputDialog.getItem(self, 'Enter text', 'Name:', [str(x) for x in range(10)])

    def showMessage(self):
        msgBox = QMessageBox()
        msgBox.setText('The document has been modified.')
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons( QMessageBox.Save | QMessageBox.Retry | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detailed text here')
        retur = msgBox.exec_()
        print(retur)
        print(retur == QMessageBox.Save)

if __name__=='__main__':
    app = QApplication([])
    w = windowClass()
    w.show()
    app.exec_()