import sys
import os
import io
import time
from analyzer import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    
    resD = []
    timeD = []
    interD = []
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionSave.setEnabled(False)
        
        self.ui.actionOpen.triggered.connect(self.openFunction)
        self.ui.actionSave.triggered.connect(self.saveFunction)
    
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
            r.write('<p>Средн. коэф. интеракций: <b>%s</b></p><table>\n' % self.ui.avgInter.text())
            r.write('<tr><th>No.</th><th>Имя</th><th>Группа</th><th>Результат</th><th>Время (c)</th><th>Интеракции</th></tr>')
            strTbl = ''
            for row in range (0, self.ui.tableWidget.rowCount()):
                strTbl += '<tr>'
                strTbl += '<td>%d.</td>' % (row+1)
                for col in range (0, self.ui.tableWidget.columnCount()):
                    strTbl += '<td>%s</td>' % self.ui.tableWidget.item(row, col).text()
                strTbl += '</tr>\n'
            r.write(strTbl)
            r.write('</table></body></html>')
            r.close()
    
    def openFunction(self):
        options = QtWidgets.QFileDialog.DontResolveSymlinks | QtWidgets.QFileDialog.ShowDirsOnly
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                "Choose Folder with Logfiles",
                "some text", options=options)
        if directory:
            # set row quantity
            self.ui.tableWidget.setRowCount(len(os.listdir(directory)))
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
