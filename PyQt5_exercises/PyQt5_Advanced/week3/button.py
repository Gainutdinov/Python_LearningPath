from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

textArray = ['Click', 'Press', 'Enter']

class myButton(QPushButton):
    def __init__(self, text):
        super(myButton, self).__init__(text)
        # self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.line.setContextMenuPolicy(Qt.CustomContextMenu)

    def mousePressEvent(self, event):
        if event.button()== 1:
            super(myButton, self).mousePressEvent(event)
        elif event.button()== 2:
            pos = event.globalPos()
            menu = QMenu()
            for i in textArray:
                menu.addAction( QAction (i, self) )
            a = menu.exec_( pos)
            if a:
                self.setText(a.text())
        elif event.button()== 4:
            pass