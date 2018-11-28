# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QPushButton, QFormLayout, QMessageBox, QMainWindow, QApplication, QWidget, QMenu, QInputDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from shell_ui import *
import xml.etree.ElementTree as ET
from custominputdialog import InputDialogWindow

class MyWin(QMainWindow):    

    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.getValue_btn.clicked.connect(self.readToDom)
        self.ui.obtainSel_btn.clicked.connect(self.showQTagInfo)
        self.ui.insertQsre_btn.clicked.connect(self.newQstre)

        self.file = os.getcwd() + os.sep + 'Surveys.xml'
        self.tree = ''
        self.parent_map = {}
        self.model_ = ''
        self.roditel_ = ''
        # initialize QTreeViewWidget

        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(0, Qt.Horizontal, "type")
        model.setHeaderData(1, Qt.Horizontal, "Tag")
        model.setHeaderData(2, Qt.Horizontal, "text")
        model.setHeaderData(3, Qt.Horizontal, "ans")
        model.setHeaderData(4, Qt.Horizontal, "type")
        self.ui.xml_trView.setModel(model)

        # create context menu
        self.popMenu = QMenu(self)
        self.popMenu.addAction('Добавить <q>...</q>', self.addQTag)
        self.popMenu.addAction('Добавить <slt>...</slt>', self.addSltTag)
        self.popMenu.addSeparator()
        self.popMenu.addAction('Удалить <q>...</q>', self.removeQTag)
        self.popMenu.addAction('Показать информацию <q>...</q>', self.showQTagInfo)
        self.popMenu.addAction('Сохранить XML документ', self.saveXMLdoc)


        # set treeview context menu policy
        self.ui.xml_trView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.xml_trView.customContextMenuRequested.connect(self.on_context_menu_tree)
      

    def on_context_menu_tree(self, point):
        # show context menu
        self.popMenu.exec_(self.ui.xml_trView.mapToGlobal(point))        


    def readToDom(self):
        if not os.path.isfile(self.file):
            QMessageBox.warning(w, "Ошибка файла", "Не могу найти файл Surveys.xml в текущией директории",buttons=QtWidgets.QMessageBox.Close, defaultButton=QtWidgets.QMessageBox.Close)
        else:
            self.tree = ET.parse(self.file)
            root = self.tree.getroot()
            self.parent_map = dict((c, p) for p in self.tree.getiterator() for c in p)

            chara = "\_"
            dash = "_"
            indentation = 1
            def innerLook(listOfTags, dash_number, _item, _parent):
                _parent = _item
                for tag in listOfTags:
                    # tagWithText = tag.tag, ' - ', tag.attrib['text']

                    _item = QStandardItem(tag.tag+' - '+tag.attrib['text'])
                    _item.setData(tag)
                    _parent.appendRow(_item)
                    #_parent = _item
                    if list(tag):
                        # print(list(tag))
                        innerLook(list(tag),dash_number+1, _item, _parent)
                #print()

            model = QStandardItemModel()

            parent = model.invisibleRootItem()
            parent.setData('DATAAAAAA')

            for sub_root in list(root[0]):
                item = QStandardItem(chara + sub_root.tag + ' - ' + sub_root.attrib['name'])
                item.setData(sub_root)
                #print(chara + sub_root.tag,'+++')
                parent.appendRow(item)
                if list(sub_root):
                    innerLook(list(sub_root), indentation, item, parent)
                    # sub_indentation += 1
                    # for _ in list(sub_root):
                    #     print(chara + (dash*sub_indentation) + _.tag)
                else:
                    pass # parent.appendRow(sub_root)


            self.ui.xml_trView.setModel(model)
            self.ui.xml_trView.expandAll()

            self.model_ = model
            self.roditel_ = parent

            self.ui.obtainSel_btn.setEnabled(True)
            self.ui.insertQsre_btn.setEnabled(True)

    def ContentShow(self):
        if self.ui.xml_trView.selectedIndexes():
            index = self.ui.xml_trView.selectedIndexes()[0]   
            crawler = index.model().itemFromIndex(index)
            return crawler.data()
    
    def addQTag(self):
        if self.ui.xml_trView.selectedIndexes():
            e = self.ContentShow()
            par = self.parent_map.get(e)
            if e.tag == 'slt':
                QMessageBox.warning(self, "ошибка при создании тега 'slt'",  "Здесь нельзя создать тег <q></> под тегом 'slt'!")
            elif par.tag == "questionnaire":
                ex = InputDialogWindow("Вторичный вопрос в questionnaire", False, e.attrib['ans'])
                ex.setModal(True)
                ex.show()
                ex.resize(400,100)
                result = ex.exec()
                if result:
                    child = ET.Element("q")

                    ex.lb.text()
                    #ss = ss.replace("\"", "")

                    child.set('g_ans', ex.cb0.currentText())
                    child.set('ans', ex.le.text())
                    child.set('text', ex.le1.text())
                    child.set('type', ex.cb.currentText())

                    e.append(child)

                    index_ = self.ui.xml_trView.selectedIndexes()[0] 
                    crawler_ = index_.model().itemFromIndex(index_)
                    item = QStandardItem('q'+' - '+ child.attrib['text'])
                    item.setData(child)
                    crawler_.appendRow(item)
                    self.parent_map.update({child: e})
            elif e.tag == "q":
                #print(e.attrib['text'])
                ex = InputDialogWindow("Вторичный вопрос в questionnaire", False, e.attrib['ans'])
                ex.setModal(True)
                ex.show()
                ex.resize(400,100)
                result = ex.exec()
                if result:
                    #par = self.parent_map.get(e)
                    child = ET.Element("q")

                    ex.lb.text()
                    #ss = ss.replace("\"", "")

                    child.set('g_ans', ex.cb0.currentText())
                    child.set('ans', ex.le.text())
                    child.set('text', ex.le1.text())
                    child.set('type', ex.cb.currentText())

                    e.append(child)
                    index_ = self.ui.xml_trView.selectedIndexes()[0] 
                    crawler_ = index_.model().itemFromIndex(index_)
                    item = QStandardItem('q'+' - '+ child.attrib['text'])
                    item.setData(child)
                    crawler_.appendRow(item)
                    self.parent_map.update({child: e})
            elif par.tag == "survey":
                ex = InputDialogWindow("Первый вопрос в questionnaire", False)
                #ex = InputDialogWindow("Secondary question in questionnaire", e.attrib['ans'])
                ex.setModal(True)
                ex.show()
                ex.resize(400,100)
                result = ex.exec()
                if result:

                    # par = self.parent_map.get(e)
                    child = ET.Element("q")
                    child.set('ans', ex.le.text())
                    child.set('text', ex.le1.text())
                    child.set('type', ex.cb.currentText())

                    e.append(child)
                    index_ = self.ui.xml_trView.selectedIndexes()[0] 
                    crawler_ = index_.model().itemFromIndex(index_)
                    item = QStandardItem('q'+' - '+ child.attrib['text'])
                    item.setData(child)
                    crawler_.appendRow(item)
                    self.parent_map.update({child: e})

                #print(ex.le.text(),'returned code', result)

    def addSltTag(self):
        # insert option if parent element is a <SLT></SLT> tag then we should not be able to create the element.
        if self.ui.xml_trView.selectedIndexes():
            e = self.ContentShow()
            print(e)
            par = self.parent_map.get(e)
            if e.tag == "slt" or e.tag=="questionnaire":
                QMessageBox.warning(self, "ошибка при создании тега 'slt'",  "Создание тега <slt></> под элементом с тегом 'slt' невозможно!")
            elif par.tag=="questionnaire" or e.tag == "q":
                ex = InputDialogWindow("Этот тег <slt></slt> для ответа", True, e.attrib['ans'])
                ex.setModal(True)
                ex.resize(400,100)
                ex.show()
                result = ex.exec()
                if result:
                    #par = self.parent_map.get(e)
                    child = ET.Element("slt")
                    #ss = ss.replace("\"", "")

                    child.set('g_ans', ex.cb0.currentText())
                    child.set('text', ex.le1.toPlainText())
                    child.set('type', ex.cb.currentText())

                    e.append(child)
                    index_ = self.ui.xml_trView.selectedIndexes()[0] 
                    crawler_ = index_.model().itemFromIndex(index_)
                    item = QStandardItem('slt'+' - '+ child.attrib['text'])
                    item.setData(child)
                    crawler_.appendRow(item)
                    self.parent_map.update({child: e})
            elif par.tag == "survey":
                QMessageBox.warning(self, "ошибка при создании тега 'slt'",  "Здесь нельзя создать <slt></> тег ")
    def showQTagInfo(self):
        if self.ui.xml_trView.selectedIndexes():
            tagElement = self.ContentShow()
            QMessageBox.about(self, "Информация по тегу", '  {0} \n Тег: {1} \n <b>Аттрибуты тега:</b> {2}'.format(tagElement, tagElement.tag, tagElement.attrib))
            #print(tagElement,'---', tagElement.tag, '---', tagElement.attrib)
    
    def removeQTag(self):
        e = self.ContentShow()
        par = self.parent_map.get(e)
        par.remove(e)
        #print('--->',self.ui.xml_trView.selectionModel(),'<---')
        #print('--->',self.model_,'<---')

        if self.ui.xml_trView.selectedIndexes():
            index = self.ui.xml_trView.selectedIndexes()[0]   
            crawler = index.model().itemFromIndex(index)
            # print('!!!','!!!','!!!',crawler)
            # print('!!!','!!!',crawler.rowCount())
            # print('parent!!!!!',crawler.parent())

            if crawler.parent() is not None:
                crawler.parent().removeRow(crawler.row())
            else:
                self.model_.removeRow(crawler.row())
        # print('removeQTag')


    def saveXMLdoc(self):
        self.tree.write(self.file, encoding="utf-8", xml_declaration=True, short_empty_elements=False)
        QMessageBox.information(w, "Surveys.xml сохраняется...", "Surveys.xml был сохранен", buttons=QMessageBox.Close, defaultButton=QMessageBox.Close)
        # print('XML file was saved')

    def newQstre(self):
        text, okPressed = QInputDialog.getText(self, "Новый 'questionnaire'","Имя для опросника :'questionnaire'", QLineEdit.Normal)
        while okPressed and text == '':
            text, okPressed = QInputDialog.getText(self, "Новый 'questionnaire'","Имя для опросника :'questionnaire'", QLineEdit.Normal)
        if okPressed:
            newXMLNode = ET.Element("questionnaire")
            newXMLNode.set('name', text)
            self.parent_map.update({newXMLNode: self.tree.getroot()[0]})
            parent = self.roditel_
            item = QStandardItem('\_questionnaire'+' - ' + newXMLNode.attrib['name'])
            item.setData(newXMLNode)
            #item.setData('sub_root')
            parent.appendRow(item)
            self.tree.getroot()[0].append(newXMLNode)

        # print('newQstre')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ico = QWidget().style().standardIcon(QtWidgets.QStyle.SP_FileDialogContentsView)
    app.setWindowIcon(ico)
    w = MyWin()
    w.show()
    sys.exit(app.exec())