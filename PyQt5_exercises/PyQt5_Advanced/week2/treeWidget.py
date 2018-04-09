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

        # start
        self.resize(500,400)
        self.fillTree()

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
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                self.fillTree(item, fullpath)
                item.setExpanded(1)
            else:
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable )
            

if __name__=='__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()

    