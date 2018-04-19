import sys
import xlrd
from learn import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fillTable1)
        self.ui.pushButton_2.clicked.connect(self.colorCell1)


    # set label
    # table.setHorizontalHeaderLabels(QString("H1;H2;").split(";"))
    # table.setVerticalHeaderLabels(QString("V1;V2;V3;V4").split(";"))
    def fillTable1(self):
        self.ui.statusbar.showMessage('Button Clicked')
        book = xlrd.open_workbook('C:/Users/temp1/Desktop/export(1).xls')
        self.ui.tableWidget.setRowCount(book.sheet_by_index(0).nrows - 1)
        self.ui.tableWidget.setColumnCount(book.sheet_by_index(0).ncols - 1)

        # set up vertical labels
        FirstRowList = book.sheet_by_index(0).row_values(0)
        myString = ";".join(FirstRowList)
        self.ui.tableWidget.setHorizontalHeaderLabels(myString.split(";"))

        # fill table cells from excel file
        for row_index in range(1, book.sheet_by_index(0).nrows - 1):
            for column_index in range(book.sheet_by_index(0).ncols - 1):
                item = book.sheet_by_index(0).row_values(row_index)[column_index]
                self.ui.tableWidget.setItem(row_index-1,column_index, QtWidgets.QTableWidgetItem(item))


    # colorize cell
    def colorCell1(self):
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        self.ID = [row, column]
        self.ui.statusbar.showMessage(str(self.ID))
        self.ui.tableWidget.item(row,column).setBackground(QtGui.QColor(32, 237, 9))
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
