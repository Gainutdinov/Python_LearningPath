from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import createProject_ui as ui

class projectManagerClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent): # указзываем parent'а чтобы знать кого перекрывать этим диалогом
        '''
        в параметре parent указывается ссылка на родительское окно. Если параметр не указан или имеет значение None, то диалоговое окно будет центр. относительно экрана. Если указана ссылка на родительское окно, то диалоговое окно будет центрироваться относительно родительского окна, - это также позволяет создать модальное окно, которое будет блокировать окно родителя, а не все окна приложения.
        '''
        super(projectManagerClass, self).__init__(parent)
        self.setupUi(self)
        
        # connect
        self.create_btn.clicked.connect(self.doCreate)
        self.cancel_btn.clicked.connect(self.reject)

    def doCreate(self):
        if self.name_lb.text():
            self.accept()
    
    def getDialogData(self):
        return dict(
            name= self.name_lb.text(),
            comment=self.comment_te.toPlainText()
        )