from PyQt5.QtWidgets import QTextEdit, QPushButton, QFormLayout, QDialog, QSizePolicy
import pyperclip

class SolutionDialogWindow(QDialog):
    def __init__(self, textSolution, parent=None):
        super(SolutionDialogWindow, self).__init__(parent)
        #QDialog.__init__(self, parent)
        self.setWindowTitle('Инструкция/Решение')
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout = QFormLayout()
        self.te = QTextEdit()
        self.te.setText(textSolution)
        self.layout.addRow(self.te)
        self.btn1 = QPushButton("Скопировать в буфер")
        self.btn1.clicked.connect(self.copyToClipboard)
        self.layout.addRow(self.btn1)
        self.setLayout(self.layout)

    def copyToClipboard(self):        
        pyperclip.copy(self.te.toPlainText())
