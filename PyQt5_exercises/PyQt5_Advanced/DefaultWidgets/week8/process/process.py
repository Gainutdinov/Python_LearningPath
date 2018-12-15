from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

worker = 'python3 '+ '"'+os.path.join(os.path.dirname(__file__),'worker.py')+'"'

class workerClass(QWidget):
    def __init__(self):
        super(workerClass, self).__init__()
        self.ly = QVBoxLayout(self)

        self.start_btn = QPushButton('Start')
        self.ly.addWidget(self.start_btn)
        self.start_btn.clicked.connect(self.start)

        self.out = QTextBrowser()
        self.ly.addWidget(self.out)

        self.progress = QProgressBar()
        self.ly.addWidget(self.progress)
        self.progress.setValue(0)
        
    def start(self):
        self.p = QProcess()
        self.p.finished.connect(self.finish)
        self.p.readyRead.connect(self.readOut)
        self.p.start(worker)
        self.start_btn.setEnabled(0)
    
    def finish(self):
        print('Finish')
        self.showMessage('Complete')
        self.p.deleteLater()
        self.start_btn.setEnabled(1)
    
    def readOut(self):
        out = str(self.p.readAll()).strip()
        #print(out)
        self.showMessage(out)
    
    def showMessage(self, msg):
        self.out.append(msg)

if __name__=='__main__':
    app = QApplication([])
    w = workerClass()
    w.show()
    app.exec()