from PyQt5.QtWidgets import *

class inputdialogdemo(QDialog):
    # def __init__(self, windowTitle, parent = None):
    #     super(inputdialogdemo, self).__init__(parent)
    def __init__(self, winTitle, ansopts=None, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(winTitle)

        layout = QFormLayout()
        self.lb = QLabel("Please write 'ans' attribute:")
        #self.btn.clicked.connect(self.getItem)
        self.le = QLineEdit()
        self.le.setPlaceholderText("option1**?**option2**?**option3")
        layout.addRow(self.lb,self.le)

        self.lb1 = QLabel("Please write 'text' attribute:")
        #self.btn1.clicked.connect(self.gettext)
        self.le1 = QLineEdit()
        self.le1.setPlaceholderText("This is the text of your question")
        layout.addRow(self.lb1,self.le1)

        if winTitle=="Secondary question in questionnaire":
            self.lb3 = QLabel("Please choose 'g_ans':")
            #self.btn1.clicked.connect(self.gettext)
            self.cb0 = QComboBox()
            self.cb0.addItems(ansopts.split("**?**"))
            layout.addRow(self.lb3,self.cb0)

        self.lb2 = QLabel("please choose 'type' of the question")
        #self.btn1.clicked.connect(self.gettext)
        self.cb = QComboBox()
        self.cb.addItems(["rb", "le"])
        layout.addRow(self.lb2,self.cb)


        self.btn1 = QPushButton("Create tag")
        self.btn1.clicked.connect(self.validateInfo)
        self.btn2 = QPushButton("Cancel")
        self.btn2.clicked.connect(self.reject)
        #self.btn2.clicked.connect(self.getint)
        layout.addRow(self.btn1,self.btn2)
        self.setLayout(layout)
        #self.setWindowTitle(windowTitle)
    

    def validateInfo(self):
        print('validating information which you typed...')
        if self.le.text() and self.le1.text():
            self.accept()
        else:
            QMessageBox.warning(self, "Insufficient information", "Please fill all the fields",buttons=QMessageBox.Close, defaultButton=QMessageBox.Close)
            #print('bad')
        #print(self.le.text())
        #print(self.le1.text())
        #self.close()