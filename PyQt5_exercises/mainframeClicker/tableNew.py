import sys
from table import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pywinauto.application import Application
from pywinauto import keyboard
from time import sleep
import win32clipboard

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.installEventFilter(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.goToUserProfile)
        self.ui.pushButton_3.clicked.connect(self.GetDefGroup)
        self.ui.pushButton_4.clicked.connect(self.createNewUser)
        self.ui.pushButton_5.clicked.connect(self.forFastPass)
        self.ui.pushButton_6.clicked.connect(self.clickF3)
        self.ui.pushButton_7.clicked.connect(self.clickF4)
        self.ui.pushButton_8.clicked.connect(self.forMainV2)

    def _clipboardUpdate(self,text):
        # set clipboard data
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()

    def _clipboardGet(self):
        # set clipboard data
        win32clipboard.OpenClipboard()
        clipData = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return clipData

    # add event filter
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Copy)):
            self.copy()
            return True
        elif (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Delete)):
            self._clear()
            return True
        elif (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Cut)):
            self.copy()
            self._clear()
            return True
        elif (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Paste)):
            self.paste()
            return True
        return super(MyWin, self).eventFilter(source, event)


    def initialSetUp(self): # connect and setFocus on the MF window
        app = Application().Connect(title=u'mf_tcp (Read only) - RUMBA Mainframe Display - \\\\Remote', class_name='Transparent Windows Client')
        transparentwindowsclient = app[u'Transparent Windows Client']
        # app = Application().Connect(title=u'Argos_Mainframe - Pro Client - Windows Internet Explorer - \\\\Remote', class_name='Transparent Windows Client')
        # transparentwindowsclient = app[u'Transparent Windows Client']
        transparentwindowsclient.SetFocus()
        transparentwindowsclient.ClickInput()

    def cut(self):

        """Cuts text from the table into the clipboard (copy + clear = cut)"""

        self.copy()
        self._clear()

    def copy(self):
        """Copies data from the table into the clipboard."""

        if len(self.ui.tableWidget.selectedRanges()) == 0:
            return

        _range = self.ui.tableWidget.selectedRanges()[0]
        rows = []
        for row in range(_range.topRow(), _range.bottomRow()+1):
            columns = []
            for column in range(_range.leftColumn(), _range.rightColumn()+1):
                it = self.ui.tableWidget.item(row, column)
                value = u'' if it is None else it.text()
                columns.append(value)
            rows.append(u'\t'.join(columns))
        selection = u'\n'.join(rows)
        self._clipboardUpdate(selection)


    def paste(self):

        """Pastes text from the clipboard into the table."""

        selection = str(QtWidgets.QApplication.clipboard().mimeData().text())
        rows = selection.split(u'\n')
        current_row = self.ui.tableWidget.currentRow()
        rowTotal = self.ui.tableWidget.rowCount()
        if ( current_row+len(rows) > self.ui.tableWidget.rowCount() ):
            for i in range(0,current_row+len(rows)-self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.insertRow(rowTotal)
        for row in rows:
            cells = row.split(u'\t')
            current_column = self.ui.tableWidget.currentColumn()
            for cell in cells:
                if current_column >= self.ui.tableWidget.columnCount():
                    break
                item = QtWidgets.QTableWidgetItem()
                item.setText(cell)
                self.ui.tableWidget.setItem(current_row, current_column, item)
                current_column += 1
            current_row += 1

    def _clear(self):

        """Clears the selected cells."""

        selected_range = self.ui.tableWidget.selectedRanges()[0]
        for row in range(selected_range.topRow(), selected_range.bottomRow() + \
            1):
            for column in range(selected_range.leftColumn(), \
                selected_range.rightColumn() + 1):
                item = self.ui.tableWidget.item(row, column)
                if item != None:
                    item.setText(u'')

    def login(self):
        try:
            if (self.ui.lineEdit.text()=='' or self.ui.lineEdit_2.text()==''):
                pass
            else:
                self.initialSetUp()
                keyboard.SendKeys('{VK_TAB}')
                self._clipboardUpdate(self.ui.lineEdit.text())
                keyboard.SendKeys(r'^v') 
                keyboard.SendKeys('{VK_TAB}')
                self._clipboardUpdate(self.ui.lineEdit_2.text())
                keyboard.SendKeys(r'^v')
                sleep(1)
                keyboard.SendKeys('{ENTER}')
                sleep(5)
                keyboard.SendKeys('{ENTER}')
        except Exception:
            pass

    def goToUserProfile(self):
        try:
            self.initialSetUp()
            keyboard.SendKeys('{VK_TAB 14}')
            keyboard.SendKeys('{ENTER}')
            self._clipboardUpdate('a.r')
            sleep(7)
            self._clipboardUpdate('a.r')
            keyboard.SendKeys(r'^v')
            keyboard.SendKeys('{ENTER}')
            sleep(1)
            self._clipboardUpdate('4')
            keyboard.SendKeys(r'^v')
            keyboard.SendKeys('{ENTER}')
        except Exception:
            pass

    def GetDefGroup(self):
        try:
            row = self.ui.tableWidget.currentRow()
            item = self.ui.tableWidget.item(row, 2)
            if item:   # checks does cell contain information
                self.initialSetUp()
                keyboard.SendKeys('{VK_TAB}')
                self.ui.statusbar.showMessage(str(row)+'-------'+str(item.text()), 3000)
                defGroup = str(item.text())
                if (len(defGroup))<8:
	                defGroup = defGroup+' '*(8-len(defGroup))
                self._clipboardUpdate(defGroup)
                keyboard.SendKeys(r'^v')
                keyboard.SendKeys('{VK_TAB}')
                self._clipboardUpdate('d')
                keyboard.SendKeys(r'^v')
                keyboard.SendKeys('{ENTER}')
                sleep(2)
                keyboard.SendKeys('{ENTER}')
                sleep(2)
                keyboard.SendKeys(r'^a')
                keyboard.SendKeys(r'^c')
                data = self._clipboardGet()
                ind = (data.find('DEFAULT-GROUP=')+14)
                item = QtWidgets.QTableWidgetItem()
                item.setText(data[ind:ind+9].rstrip())
                self.ui.tableWidget.setItem(row, 3, item)
            else:
                pass
        except Exception:
            pass
            # print('eeror')
        #current_row = self.ui.tableWidget.currentRow()
        #item = self.ui.tableWidget.itemAt(row, column)
        #self.ID = item.text()

    def createNewUser(self):
        try:
            row = self.ui.tableWidget.currentRow()
            if self.ui.tableWidget.item(row, 0):
                if self.ui.tableWidget.item(row, 1):
                    if self.ui.tableWidget.item(row, 2):
                        if self.ui.tableWidget.item(row, 3):
                            values = [self.ui.tableWidget.item(row, 0).text(),self.ui.tableWidget.item(row, 1).text(),self.ui.tableWidget.item(row, 2).text(),self.ui.tableWidget.item(row, 3).text()]
                            self.ui.statusbar.showMessage(str(row) + '-------' + str(values), 3000)
                            self.initialSetUp()
                            keyboard.SendKeys('{VK_TAB}')
                            sleep(1)
                            keyboard.SendKeys('{DELETE 5}')
                            self._clipboardUpdate(str(values[1]))
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{VK_TAB}')
                            keyboard.SendKeys('{DELETE 5}')
                            self._clipboardUpdate('1')
                            keyboard.SendKeys(r'^v')
                            keyboard.SendKeys('{ENTER}')
                            sleep(1)
                            keyboard.SendKeys('{DELETE 5}')
                            self._clipboardUpdate('sec0007')
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{VK_TAB}')
                            keyboard.SendKeys('{DELETE 8}')
                            self._clipboardUpdate(str(values[0]))
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{VK_TAB}')
                            keyboard.SendKeys('{DELETE 8}')
                            self._clipboardUpdate(str(values[3]))
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{VK_TAB}')
                            self._clipboardUpdate('Pass1234')
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{VK_TAB}')
                            self._clipboardUpdate('Pass1234')
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{ENTER}')
                            sleep(1)
                            keyboard.SendKeys('{DELETE 8}')
                            self._clipboardUpdate(str(values[2]))
                            keyboard.SendKeys(r'^v')
                            sleep(1)
                            keyboard.SendKeys('{ENTER}')
        except Exception:
            self.ui.statusbar.showMessage('---One of the required fields are not filled----', 3000)

    def clickF3(self):
        try:
            self.initialSetUp()
            keyboard.SendKeys('{VK_F3}')
        except Exception:
            pass

    def clickF4(self):
        try:
            self.initialSetUp()
            keyboard.SendKeys('{VK_F4}')
        except Exception:
            pass
    
    def forFastPass(self):
        """Copies data from the table into the clipboard for FastPass"""
        rows = []
        try:
            for row in range(self.ui.tableWidget.rowCount()):
                columns = []
                for column in range(self.ui.tableWidget.columnCount()):
                    it = self.ui.tableWidget.item(row, column)
                    value = u'' if it is None else it.text()
                    if column == 4:
                        columns.append(str(self.ui.tableWidget.item(row, 6).text()))
                        columns.append(value)
                        columns.append('mfprod')
                        columns.append(str(self.ui.tableWidget.item(row, 1).text()))
                rows.append(u'\t'.join(columns))
            selection = u'\n'.join(rows)
            self._clipboardUpdate(selection)
        except Exception:
            pass


    def forMainV2(self):
        """Copies data from the table into the clipboard for FastPass"""
        rows = []
        try:
            for row in range(self.ui.tableWidget.rowCount()):
                columns = []
                for column in range(self.ui.tableWidget.columnCount()):
                    it = self.ui.tableWidget.item(row, column)
                    value = u'' if it is None else it.text()
                    if column == 5:
                        columns.append(str(self.ui.tableWidget.item(row, 5).text()))
                        columns.append('')
                        columns.append('')
                        columns.append(str(self.ui.tableWidget.item(row, 6).text()))
                        columns.append('')
                        columns.append(str(self.ui.tableWidget.item(row, 1).text()))
                        columns.append(str(self.ui.tableWidget.item(row, 0).text()))
                        columns.append('')
                        columns.append('')
                        columns.append('Mainframe')
                        columns.append(str(self.ui.tableWidget.item(row, 4).text()))
                rows.append(u'\t'.join(columns))
            selection = u'\n'.join(rows)
            self._clipboardUpdate(selection)
        except Exception:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())