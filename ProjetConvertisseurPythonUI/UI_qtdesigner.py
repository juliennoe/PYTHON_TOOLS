# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/Julien Noé/OneDrive/0_Bureau/CONVERT_UI_PYTHON\UI_qtdesigner.ui',
# licensing of 'c:/Users/Julien Noé/OneDrive/0_Bureau/CONVERT_UI_PYTHON\UI_qtdesigner.ui' applies.
#
# Created: Tue Oct  8 17:43:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 501)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))

