from PyQt5.QtWidgets import *
import os
path = os.path.dirname(os.path.abspath(__file__))
print(path)
class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.list = QListWidget()
        ly.addWidget(self.list)
        self.textBrowser = QTextBrowser()
        ly.addWidget(self.textBrowser)

        #connects
        self.list.itemClicked.connect(self.updateText)
        self.list.itemDoubleClicked.connect(self.openFile)

        #start
        self.resize(500, 400)
        self.fillList()

    def fillList(self):
        for f in os.listdir(path):
            self.list.addItem(f)

    def fullPath(self, item):
        return os.path.join(path,item.text())

    def updateText(self, item):
        text = open(os.path.join(path, item.text())).read()
        self.textBrowser.setText(text)

    def fullPath(self, item):
        return os.path.join(path, item.text())

    def openFile(self, item):
        path = self.fullPath(item)
        os.system(path)

if __name__=='__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()

    