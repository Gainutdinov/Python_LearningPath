from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widgets import templateEditor_ui as ui
import os, json

templateFile = os.path.join(os.path.dirname(__file__), 'template.json')

class templateEditorClass(QDialog, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditorClass, self).__init__()
        self.setupUi(self)
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # connects
        self.add_btn.clicked.connect(self.addItem)
        self.remove_btn.clicked.connect(self.removeItem)
        self.save_btn.clicked.connect(self.saveTemplate)
        self.close_btn.clicked.connect(self.close)
        #load template
        self.loadTemplate()

    def addItem(self, name='Folder',parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        item = QTreeWidgetItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        item.setText(0, name)
        parent.addChild(item)
        item.setExpanded(1)
        return item

    def removeItem(self):
        items = self.tree.selectedItems()
        for i in items:
            (i.parent() or self.tree.invisibleRootItem()).takeChild(self.tree.indexFromItem(i).row())
    
    def saveTemplate(self):
        template = self.getStructure()
        with open(templateFile, 'w') as f:
            json.dump(template, f, indent=4)
        self.close
    
    def getStructure(self, parent=None):
        level = []
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in range(parent.childCount()):
            ch = parent.child(i)
            content = self.getStructure(ch)
            level.append({'name':ch.text(0),
                          'content': content})
        return level

    def loadTemplate(self):
        if os.path.exists(templateFile):
            with open(templateFile) as f:
                template = json.load(f)
                self.restoreStructure(template)
    
    def restoreStructure(self, data, parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in data:
            item = self.addItem(i['name'], parent)
            self.restoreStructure(i['content'], item)

