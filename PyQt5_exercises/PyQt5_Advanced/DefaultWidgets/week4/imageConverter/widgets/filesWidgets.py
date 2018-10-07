from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')

class listWidgetCLass(QListWidget):
    def __init__(self):
        super(listWidgetCLass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files = []
    
    def dropEvent(self, event):
        event.accept()
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())

    def dragEnterEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()     
    
    def dragMoveEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def addFile(self, path):
        if not path in self.files:
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)

    def deleteSelected(self):
        for s in self.selectedItems():
            # The first role that can be used for application-specific purposes.

            # For user roles, it is up to the developer to decide which types to use and ensure that components use the correct types when accessing and setting data.
            self.files.remove(s.data(Qt.UserRole)) # or we can use 256
            self.takeItem(self.indexFromItem(s).row())

    def getAllFiles(self):
        return self.files

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.deleteSelected()