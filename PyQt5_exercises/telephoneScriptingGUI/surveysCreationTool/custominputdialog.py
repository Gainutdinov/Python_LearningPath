from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QPushButton, QFormLayout, QMessageBox, QPlainTextEdit

class InputDialogWindow(QDialog):
    # def __init__(self, windowTitle, parent = None):
    #     super(inputdialogdemo, self).__init__(parent)
    def __init__(self, winTitle, slt=False, ansopts=None, parent=None):
        super(InputDialogWindow, self).__init__(parent)
        QDialog.__init__(self, parent)
        
        self.slt = slt
        print('slt --->', slt)        
        layout = QFormLayout()

        if self.slt==False:
            self.lb = QLabel("Пожалуйста напишите 'ans' аттрибут:")
            self.le = QLineEdit()
            self.le.setPlaceholderText("option1**?**option2**?**option3")
            layout.addRow(self.lb,self.le)

        self.lb1 = QLabel("Пожалуйста напишите 'text' аттрибут:")
        self.le1 = QLineEdit()
        self.le1.setPlaceholderText("Это текст вашего вопроса")
        if self.slt==True:
            self.le1 = QPlainTextEdit()
        layout.addRow(self.lb1,self.le1)

        if winTitle=="Вторичный вопрос в 'questionnaire' вопроснике" and self.slt==False:
            self.lb3 = QLabel("Пожалуйста выберите 'g_ans':")
            #self.btn1.clicked.connect(self.gettext)
            self.cb0 = QComboBox()
            self.cb0.addItems(ansopts.split("**?**"))
            layout.addRow(self.lb3,self.cb0)
        elif self.slt==True:
            self.le1.setPlaceholderText("Текст ответа")
            self.lb3 = QLabel("Пожалуйста, выберите 'g_ans'")
            self.cb0 = QComboBox()
            self.cb0.addItems(ansopts.split("**?**"))
            layout.addRow(self.lb3, self.cb0)


        self.lb2 = QLabel("Пожалуйста, выберите 'type' тип вопроса")
        #self.btn1.clicked.connect(self.gettext)
        self.cb = QComboBox()
        self.cb.addItems(["rb", "le"])
        layout.addRow(self.lb2,self.cb)


        self.btn1 = QPushButton("Создать тег")
        self.btn1.clicked.connect( lambda: (self.validateInfo(self.slt)) )
        self.btn2 = QPushButton("Отмена")
        self.btn2.clicked.connect(self.reject)
        #self.btn2.clicked.connect(self.getint)
        layout.addRow(self.btn1,self.btn2)
        self.setLayout(layout)
        #self.setWindowTitle(windowTitle)
    

    def validateInfo(self, sltCheck=False):
        print('проверка информации которая была введена...')
        if (sltCheck==True and self.le1.toPlainText()):
            self.accept()
        elif (sltCheck==False and self.le1.text() and self.le.text()):
            self.accept()
        else:
            QMessageBox.warning(self, "Недостаточно информации", "Пожалуйста, введите все поля",buttons=QMessageBox.Close, defaultButton=QMessageBox.Close)