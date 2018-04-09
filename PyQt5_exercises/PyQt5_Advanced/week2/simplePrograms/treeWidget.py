from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
path = os.path.dirname(os.path.abspath(__file__))

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.tree = QTreeWidget()
        ly.addWidget(self.tree)

        #connects
        self.tree.itemChanged.connect(self.action)

        # start
        self.resize(500,400)
        self.updateTree()

    def updateTree(self):
        self.tree.blockSignals(True)
        self.fillTree()
        self.tree.blockSignals(False)

    def fillTree(self, parent=None, root=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        if not root:
            root = path
        for f in os.listdir(root):
            if f[0] in ['.', '_']: continue
            item = QTreeWidgetItem()
            item.setText(0, f)
            parent.addChild(item)
            fullpath = os.path.join(root, f)
            if os.path.isdir(fullpath):
                self.fillTree(item, fullpath)
                item.setExpanded(1)
            else:
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable )
                item.setData(0, Qt.UserRole, os.path.normpath(fullpath))


    def action(self, item):
        print(item.text(0))
        # rename files
        oldFile = os.path.join(os.path.dirname(oldFile), os.path.basename(oldFile))
        newFile = os.path.join(os.path.dirname(oldFile), item.text(0))
        os.rename(oldFile, newFile)

if __name__=='__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()

    