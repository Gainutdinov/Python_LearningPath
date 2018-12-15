from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, time
import subprocess


class folderSizeCompute(QWidget):
    def __init__(self):
        super(folderSizeCompute, self).__init__()
        self.ly = QVBoxLayout(self)
        self.start_btn = QPushButton('Compute')
        self.ly.addWidget(self.start_btn)
        self.start_btn.clicked.connect(self.compute)
        self.path_le = QLineEdit()
        self.ly.addWidget(self.path_le)
        self.info_lb = QLabel()
        self.ly.addWidget(self.info_lb)
        self.path_le.setText('/home/marat/Desktop/PyQt5_Cookbooks/')
        self.resize(300, 100)


    def compute(self):
        path = self.path_le.text()
        self.obj = worker(path)
        self.t = QThread()
        self.obj.moveToThread(self.t)
        self.t.started.connect(self.obj.start)
        self.obj.finishSignal.connect(self.t.quit)
        self.obj.updateSignal.connect(self.setInfo)

        self.t.start()
        # path = '.'
        # size = subprocess.check_output(['du','-sh', str(self.path_le.text())]).split()[0].decode('utf-8')
        # print(size)
        # print("Directory size: " + size)
        # self.setInfo(size)

    
    def setInfo(self, i):
        print('hhh')
        self.info_lb.setText('%s bytes' % i)

class worker(QObject):
    finishSignal = pyqtSignal()
    updateSignal = pyqtSignal(int)
    def __init__(self, path):
        super(worker, self).__init__()
        self.path = path
    def start(self):
        size = 0
        st = time.time()
        for path, dirs, files in os.walk(self.path):
            for f in files:
                b = os.path.getsize(os.path.join(path,f))
                size += int(b/1024.0)
                if (time.time() - st) > 0.5:
                    print(size)
                    self.updateSignal.emit(size)
                    st = time.time()

        self.finishSignal.emit()



if __name__=='__main__':
    app = QApplication([])
    w = folderSizeCompute()
    w.show()
    app.exec()