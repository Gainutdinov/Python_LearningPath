from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import editorView

class editorWindowClass(QWidget):
    def __init__(self):
        super(editorWindowClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.view = editorView.editorViewClass()
        self.ly.addWidget(self.view)
        # start
        self.resize(500, 200)



if __name__=='__main__':
    app = QApplication([])
    w = editorWindowClass()
    w.show()
    app.exec()



