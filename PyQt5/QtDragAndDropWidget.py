from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
import sys
import os

class DragAndDropWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setUpUI()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls() and e.mimeData().urls().__len__() == 1:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.tedit_path.setText(e.mimeData().urls()[0].toLocalFile())

    def setUpUI(self):
        self.setObjectName("DragAndDropWidget")
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        self.btn_browse = QtWidgets.QPushButton(self)
        self.btn_browse.setGeometry(QtCore.QRect(255, 150, 131, 31))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_browse.clicked.connect(self.browsefiles)

        self.lbl_drag = QtWidgets.QLabel(self)
        self.lbl_drag.setGeometry(QtCore.QRect(100, 50, 440, 91))
        self.lbl_drag.setObjectName("lbl_drag")

        self.tedit_path = QtWidgets.QLineEdit(self)
        self.tedit_path.setEnabled(False)
        self.tedit_path.setGeometry(QtCore.QRect(20, 200, 591, 31))
        self.tedit_path.setObjectName("tedit_path")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("DragAndDropWidget", "DragAndDropWidget"))
        self.btn_browse.setText(_translate("DragAndDropWidget", "Browse"))
        self.lbl_drag.setText(_translate("DragAndDropWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Drag and Drop the file here<br/>or</span></p></body></html>"))

    def browsefiles(self):
        file = QFileDialog.getOpenFileName(self,'Browse File',os.getcwd())
        self.tedit_path.setText(file[0])
