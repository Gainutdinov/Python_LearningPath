from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        layout = QVBoxLayout(self)
        button = QPushButton('Print')
        label = QLabel('adfafd')
        layout.addWidget(label)
        layout.addWidget(button)
        line = QLineEdit()
        layout.addWidget(line)

        line.textChanged.connect(self.text)
        
        # work with signal via connect signal
        #button.clicked.connect(self.action)

        # work with signal via decorator
        @button.clicked.connect
        def click():
            if line.text() != '':
                label.setText(line.text())
            self.action()


    def action(self):
        print('ACTION')

    def text(self, arg):
        print(arg)

app = QApplication([])
window = MyWidget()
window.show()
app.exec_()
