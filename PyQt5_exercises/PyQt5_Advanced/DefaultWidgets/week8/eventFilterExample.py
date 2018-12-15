from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class simpleWidget(QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        ly = QVBoxLayout(self)
        self.label = QLabel('OUT')
        ly.addWidget(self.label)
        self.installEventFilter(self) # obligatory method to enable eventFilter() method
        # self.removeEventFilter(self) this method used to remove using installEventFilter

    def eventFilter(self, obj, event): # obligatory method to catch events  
        if event.type() == QEvent.Enter:
            self.label.setText('IN')
            return True # used to stop catching the event by another function, additionally, cause event is raised earlier before information send to our object (in our case to simpletWidget class) we need to explain to engine that we handled this event and there is no need to send event to another object (we return True), then we do not handle event it should be received by original object and by returning False we literally say that we will not handle the event our object (simpleWidget instance)
        elif event.type() == QEvent.Leave:
            self.label.setText('OUT')
            return True
        return False # used to contintinue searching for next function which will catch this event

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWidget()
    w.show()
    app.exec()