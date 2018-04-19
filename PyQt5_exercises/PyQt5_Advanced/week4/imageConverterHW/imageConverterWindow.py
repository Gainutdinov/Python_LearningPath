from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import imageConverter_ui as ui
from widgets import filesWidgets
from widgets import lineEdit
from icons.icons import icons
import converter
import settings
import os

class imageConverterClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(imageConverterClass, self).__init__()
        self.setupUi(self)
        self.list = filesWidgets.listWidgetCLass()
        self.setWindowIcon(QIcon(icons['main']))
        self.files_ly.addWidget(self.list)
        self.start_btn.clicked.connect(self.start)
        self.browseIconvert_btn.clicked.connect(self.openCurrentFolderDialog)
        self.browseOut_btn.clicked.connect(self.selectOutputDirectory)
        self.convertType_cmb = QComboBox()
        self.convertType_cmb.addItems(["PNG", "JPG", "GIF"])
        self.horizontalLayout_2.addWidget(self.convertType_cmb)
        self.includeFolders_cb = QCheckBox()
        self.includeFolders_cb.setText('Include folders')
        self.horizontalLayout_2.addWidget(self.includeFolders_cb)
        # initilize from converterSettings.json
        self.initialize()

    def initialize(self):
        data = settings.settingsClass().load()
        if data.get('path'):
            self.iconvert_lb.setText('%s' % data['path'])
            self.out_le.setText(data['outputDirectory'])
        else:
            tmpdata = dict()
            tmpdata["path"] = os.path.dirname(__file__)
            tmpdata["outputDirectory"] = self.out_le.text()
            settings.settingsClass().save(tmpdata)
            self.iconvert_lb.setText('Current path is not selected')
            self.out_le.setText('Output folder is not selected...')


    def start(self):
        if (self.out_le.text() != '' and self.iconvert_lb.text() != '' and len(self.list.getAllFiles()) != 0):
            fileList = self.list.getAllFiles()
            for count, item in enumerate(fileList, start=1):
                self.progressBar.setValue(count/len(fileList) * 100)
                if (os.path.isdir(item)):
                    if (self.includeFolders_cb.isChecked() == True):
                        for root, dirs, files in os.walk(item):
                            for file in files:
                                new_file = os.path.basename(file).split('.')[0] + '.' + self.convertType_cmb.currentText()
                                open(self.out_le.text() + '/' + new_file, 'w').close()
                else:
                    new_file = os.path.basename(item).split('.')[0] + '.' + self.convertType_cmb.currentText()
                    open(self.out_le.text() + '/' + new_file, 'w').close()


    def openCurrentFolderDialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        tmpdata = dict()
        tmpdata["path"] = os.path.normpath(folder)
        tmpdata["outputDirectory"] = self.out_le.text()
        settings.settingsClass().save(tmpdata)
        self.initialize()

    def selectOutputDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        tmpdata = dict()
        tmpdata["outputDirectory"] = os.path.normpath(folder)
        tmpdata["path"] = self.iconvert_lb.text()
        settings.settingsClass().save(tmpdata)
        self.out_le.setText(os.path.normpath(folder))
        self.initialize()

    


if __name__=='__main__':
    app = QApplication([])
    w = imageConverterClass()
    w.show()
    app.exec_()

