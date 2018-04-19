from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')

class listWidgetCLass(QListWidget):
    def __init__(self):
        super(listWidgetCLass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DragDrop)
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

    def startDrag(self, dropAction):
        drag = QDrag(self)
        mimedata = QMimeData()
        url = []
        for i in self.selectedItems():
            url.append(i.data(Qt.UserRole))
        mimedata.setUrls(QUrl.fromLocalFile(x) for x in url)
        drag.setMimeData(mimedata)
        pix = QPixmap(icon)
        drag.setPixmap(pix)
        r = drag.exec_()
        if r == 2: # or we can use Qt.TargetMoveAction
            self.deleteSelected()
        elif r == 32770: # or we can use Qt.TargetMoveAction
            self.deleteSelected()

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

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            pass
        elif event.button() == Qt.LeftButton:
            self.setDragDropMode(QAbstractItemView.NoDragDrop)
            super(listWidgetCLass, self).mousePressEvent(event)
        else:
            self.setDragDropMode(QAbstractItemView.DragDrop)
            super(listWidgetCLass, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragDropMode(QAbstractItemView.DragDrop)
        super(listWidgetCLass, self).mouseReleaseEvent(event)

if __name__== '__main__':
    app = QApplication([])
    w = listWidgetCLass()
    w.show()
    app.exec_()


