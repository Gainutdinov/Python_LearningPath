from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from . import editorScene


class editorViewClass(QGraphicsView):
    def __init__(self):
        super(editorViewClass, self).__init__()
        self.s = editorScene.editorSceneClass()
        self.setScene(self.s)