from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import iconWidget_ui as ui
from icons.icons import icons
import random
import os
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

class iconWidgetClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(iconWidgetClass, self).__init__()
        self.setupUi(self)
        # ui
        self.setWindowIcon(QIcon(icons['create']))
        self.fill_btn.setText('')
        self.fill_btn.setFixedSize(QSize(40,40))
        self.fill_btn.setIconSize(QSize(32,32))
        self.fill_btn.setFlat(1)
        self.fill_btn.setIcon(QIcon(icons['create']))
        self.clear_btn.setText('')
        self.clear_btn.setFixedSize(QSize(40,40))
        self.clear_btn.setIconSize(QSize(32,32))
        self.clear_btn.setFlat(1)
        self.clear_btn.setIcon(QIcon(icons['clear']))
        self.fill_act.setIcon(QIcon(icons['create']))
        self.clear_act.setIcon(QIcon(icons['clear']))
        self.open_act.setIcon(QIcon(icons['open']))
        self.save_act.setIcon(QIcon(icons['save']))
        self.exit_act.setIcon(QIcon(icons['close']))


        pix = QPixmap(icons['sphere']).scaled( 40, 40,
                                               Qt.KeepAspectRatio,
                                               Qt.SmoothTransformation )
        self.image_lb.setPixmap(pix)

        self.list_lwd.setViewMode(QListView.IconMode)
        self.list_lwd.setIconSize(QSize(64,64))
        self.list_lwd.setResizeMode(QListWidget.Adjust)
        self.list_lwd.setDragDropMode(QAbstractItemView.NoDragDrop)

        # connects
        self.fill_btn.clicked.connect(self.fillList)
        self.clear_btn.clicked.connect(self.clearList)
        self.fill_act.triggered.connect(self.fillCombo)
        self.clear_act.triggered.connect(self.clearCombo)
        self.list_lwd.itemDoubleClicked.connect(self.viewImage)

    def fillList(self):
        path = os.path.join(os.path.dirname(__file__), 'textures')
        self.clearList()
        for i in os.listdir(path):
            item = QListWidgetItem(i)
            item.setIcon(QIcon( os.path.join(path, i)) )
            self.list_lwd.addItem(item)

    def clearList(self):
        self.list_lwd.clear()

    def fillCombo(self):
        self.clearCombo()
        for i in range(10):
            self.combo_cbb.addItem('Item %s' % i)
            self.combo_cbb.setItemIcon(i, self.getRandomIcon())

    def clearCombo(self):
        self.combo_cbb.clear()

    def getRandomIcon(self):
        return QIcon(icons[random.choice(['item1','item2','item3'])])

    def viewImage(self):
        if self.findChild(QLabel, "custom_lb") is None:
            self.custom_lb = QLabel()
            self.custom_lb.setObjectName("custom_lb")
            self.custom_lb.setText('My custom label')
            self.horizontalLayout_2.addWidget(self.custom_lb)
        item = self.list_lwd.currentItem()
        path = os.path.join(os.path.dirname(__file__), 'textures')
        item_path = os.path.join(path, item.text())
        pix = QPixmap(item_path).scaled( 400, 400,
                                               Qt.KeepAspectRatio,
                                               Qt.SmoothTransformation )
        self.custom_lb.setPixmap(pix)


if __name__=='__main__':
    app = QApplication([])
    w = iconWidgetClass()
    w.show()
    app.exec_()

