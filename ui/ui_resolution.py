# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resolution.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 272)
        self.closeBtn = QtWidgets.QPushButton(dialog)
        self.closeBtn.setGeometry(QtCore.QRect(290, 230, 91, 33))
        self.closeBtn.setObjectName("closeBtn")
        self.selectBtn = QtWidgets.QPushButton(dialog)
        self.selectBtn.setGeometry(QtCore.QRect(20, 230, 91, 33))
        self.selectBtn.setObjectName("selectBtn")
        self.resoList = QtWidgets.QListWidget(dialog)
        self.resoList.setGeometry(QtCore.QRect(10, 10, 381, 192))
        self.resoList.setSelectionRectVisible(True)
        self.resoList.setObjectName("resoList")
        self.resoEdit = QtWidgets.QLineEdit(dialog)
        self.resoEdit.setGeometry(QtCore.QRect(140, 230, 121, 31))
        self.resoEdit.setObjectName("resoEdit")

        self.retranslateUi(dialog)
        self.closeBtn.clicked.connect(dialog.close)
        self.selectBtn.clicked.connect(self.save)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Select Resolution"))
        self.closeBtn.setText(_translate("dialog", "Close"))
        self.selectBtn.setText(_translate("dialog", "Select"))

    def save(self):
        sys.exit()
