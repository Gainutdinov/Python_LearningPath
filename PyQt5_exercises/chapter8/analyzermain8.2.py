import sys
import os
import io
import time
from analyzer1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    
    checker = False
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionSave.setEnabled(False)
        
        self.ui.actionOpen.triggered.connect(self.openFunction)
        self.ui.actionSave.triggered.connect(self.saveFunction)
        self.ui.actionExit.triggered.connect(self.closeProg)
        self.ui.actionQuestions_Statistics.triggered.connect(self.questFunction)

    def closeProg(self):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.checker = True
            self.close()
            
    def closeEvent(self, e):
        if self.checker:
            e.accept()
        else:
            e.ignore()
    
    def questFunction(self):
        options = QtWidgets.QFileDialog.DontResolveSymlinks | QtWidgets.QFileDialog.ShowDirsOnly
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                "Choose Folder with Logfiles",
                "some text", options=options)
        if directory:
            path = os.path.abspath(directory + '\\' + os.listdir(directory)[0])
            r = open(path, 'r', encoding='utf-8')
            content = r.read()
            # counts how many questions there are in log
            occur = content.count("Сложность: ")
            questions = []
            valueQ = []
            content = content.split('\n')
            for i in range(0, len(content)):
                if content[i] == '':
                    questions.append(content[i+1])
                    valueQ.append(content[i+2].split()[1])
            r.close()
            # here are the question
            questions = questions[0:-2]
            counterQ = [0] * occur
            # iterate files
            for i in range (0, len(os.listdir(directory))):
                path = os.path.abspath(directory + '\\' + os.listdir(directory)[i])
                # open files one by one
                r = open(path, 'r', encoding='utf-8')
                content = r.read()
                content = content.split('\n')

                if (i == 0):
                    title = content[0].split(":")[1][1:]

                # iterate questions in a file
                for q in range (0, len(questions)):
                    index = content.index(questions[q])
                    while (content[index] != ''):
                        index += 1
                    if content[index-1] == 'TRUE':
                        counterQ[q] += 1
                r.close()
            #for q in range (0, len(questions)):
                #print(questions[q] + ', ' + str(counterQ[q]) + ', ' + valueQ[q] + '\n')
            # output tableview
            # set row quantity
            self.ui.tableWidget.setRowCount(occur)
            self.ui.tableWidget.setColumnCount(3)
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(0, item)
            header = self.ui.tableWidget.horizontalHeaderItem(0)
            header.setText('Вопрос')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(1, item)
            header = self.ui.tableWidget.horizontalHeaderItem(1)
            header.setText('Отвечено раз')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(2, item)
            header = self.ui.tableWidget.horizontalHeaderItem(2)
            header.setText('Сложность')
            self.item = [[''] * 3] * occur
            for row in range (0, self.ui.tableWidget.rowCount()):
                for col in range (0, self.ui.tableWidget.columnCount()):
                    self.item[row][col] = QtWidgets.QTableWidgetItem()
                    if col == 0: 
                        self.item[row][col].setText(questions[row])
                    elif col == 1:
                        self.item[row][col].setData(QtCore.Qt.EditRole, int(counterQ[row]))
                    else:
                        self.item[row][col].setData(QtCore.Qt.EditRole, int(valueQ[row]))
                    self.ui.tableWidget.setItem(row, col, self.item[row][col])
        
        self.ui.trTitle.setText(title)
        #self.ui.avgInter.setText('')
        #self.ui.avgRes.setText('')
        #self.ui.avgTime.setText('')
        #self.ui.maxRes.setText('')
        #self.ui.minRes.setText('')
        self.ui.actionSave.setEnabled(True)
    
    # Save as HTML
    def saveFunction(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                "Save Data To HTML File", "", "HTML Files (*.html)", options=options)
        if fileName:
            r = open(fileName, 'w', encoding='utf-8')
            r.write('''<!DOCTYPE HTML><html><head><META HPPT-EQIUV="Content-Type" CONTENT="text/html; charset=utf-8"><style>table {border: 1px solid black; border-collapse: collapse;} td {border: 1px solid black;} th {border: 1px solid black; background: #CCC;}</style></head>\n''')
            r.write('<h3>Тренажер: %s</h3>\n' % self.ui.trTitle.text())
            r.write('<p>Время записи файла: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '</p>\n')
            r.write('<p>Результат: Мин. <b>%s</b>\tСредн. <b>%s</b>\tМакс. <b>%s</b></p>\n' % (self.ui.minRes.text(), self.ui.avgRes.text(), self.ui.maxRes.text()))
            r.write('<p>Средн. время выполнения: <b>%s</b></p>\n' % self.ui.avgTime.text())
            r.write('<p>Средн. коэф. интеракций: <b>%s</b></p><table>\n<tr><th>No.</th>' % self.ui.avgInter.text())
            headerT = ''
            for col in range (0, self.ui.tableWidget.columnCount()):
                headerT += '<th>%s</th>' % self.ui.tableWidget.horizontalHeaderItem(col).text()
            r.write(headerT)
            strTbl = ''
            for row in range (0, self.ui.tableWidget.rowCount()):
                strTbl += '</tr><tr>'
                strTbl += '<td>%d.</td>' % (row+1)
                for col in range (0, self.ui.tableWidget.columnCount()):
                    strTbl += '<td>%s</td>' % self.ui.tableWidget.item(row, col).text()
                strTbl += '</tr>\n'
            r.write(strTbl)
            r.write('</table></body></html>')
            r.close()
    
    def openFunction(self):
        
        self.resD = []
        self.timeD = []
        self.interD = []
        
        options = QtWidgets.QFileDialog.DontResolveSymlinks | QtWidgets.QFileDialog.ShowDirsOnly
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                "Choose Folder with Logfiles",
                "some text", options=options)
        if directory:
            # set row quantity
            self.ui.tableWidget.setRowCount(len(os.listdir(directory)))
            self.ui.tableWidget.setColumnCount(5)
            
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(0, item)
            header = self.ui.tableWidget.horizontalHeaderItem(0)
            header.setText('Имя')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(1, item)
            header = self.ui.tableWidget.horizontalHeaderItem(1)
            header.setText('Группа')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(2, item)
            header = self.ui.tableWidget.horizontalHeaderItem(2)
            header.setText('Результат')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(3, item)
            header = self.ui.tableWidget.horizontalHeaderItem(3)
            header.setText('Время выполнения')
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setHorizontalHeaderItem(4, item)
            header = self.ui.tableWidget.horizontalHeaderItem(4)
            header.setText('Интеракции')
            
            self.item = [[''] * 6] * len(os.listdir(directory))
            path = os.path.abspath(directory + '\\' + os.listdir(directory)[0])
            r = open(path, 'r', encoding='utf-8')
            title = r.readlines()[0].split(":")[1][1:]
            r.close()
            for file in range (0, len(os.listdir(directory))):
                if os.listdir(directory)[file].endswith('.txt'):
                    dataFromName = os.listdir(directory)[file].split('.txt')[0].split('_')
                    for data in range (0, len(dataFromName)):
                        self.item[file][data] = QtWidgets.QTableWidgetItem()
                        if data == 0 or data == 1: 
                            self.item[file][data].setText(dataFromName[data])
                        else:
                            self.item[file][data].setData(QtCore.Qt.EditRole, float(dataFromName[data]))
                        self.ui.tableWidget.setItem(file, data, self.item[file][data])
                    self.resD.append(float(dataFromName[2]))
                    self.timeD.append(float(dataFromName[3]))
                    self.interD.append(float(dataFromName[4]))

            self.ui.minRes.setText(str(min(self.resD)))
            self.ui.maxRes.setText(str(max(self.resD)))
            self.ui.avgRes.setText('%.2f' % (sum(self.resD)/len(self.resD)))
            self.ui.avgTime.setText('%.2f' % (sum(self.timeD)/len(self.timeD)))
            self.ui.avgInter.setText('%.2f' % (sum(self.interD)/len(self.interD)))
            self.ui.trTitle.setText(title)
            self.ui.actionSave.setEnabled(True)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
