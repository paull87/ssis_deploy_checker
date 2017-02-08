# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeployWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DeployWindow(object):
    def setupUi(self, DeployWindow):
        DeployWindow.setObjectName(_fromUtf8("DeployWindow"))
        DeployWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        DeployWindow.setWindowFlags(QtCore.Qt.Window |
                                  QtCore.Qt.WindowTitleHint |
                                  QtCore.Qt.WindowCloseButtonHint)
        DeployWindow.resize(400, 200)
        DeployWindow.setFixedSize(DeployWindow.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/compare.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeployWindow.setWindowIcon(icon)
        DeployWindow.setStyleSheet(_fromUtf8("QDialog {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0     #e0effa, stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QFrame#frame {\n"
"    border: 2px solid #386bd2;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    color: #555;\n"
"    font-family: Tahoma, Verdana, Segoe, sans-serif;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 14px;\n"
"    border: 2px solid transparent;\n"
"    border-radius: 4px;\n"
"    color: #66afe9;\n"
"    background-color: #fff;\n"
"    border-color: rgb(185, 185, 185);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #fff;\n"
"    background-color: #66afe9;\n"
"    border-color: #66afe9;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #fff;\n"
"    background-color: #518cba;\n"
"    border-color: #518cba;\n"
"}\n"
""))
        DeployWindow.setSizeGripEnabled(False)
        self.buttonAccept = QtGui.QPushButton(DeployWindow)
        self.buttonAccept.setGeometry(QtCore.QRect(90, 140, 81, 31))
        self.buttonAccept.setObjectName(_fromUtf8("buttonAccept"))
        self.buttonCancel = QtGui.QPushButton(DeployWindow)
        self.buttonCancel.setGeometry(QtCore.QRect(230, 140, 81, 31))
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.label_warning = QtGui.QLabel(DeployWindow)
        self.label_warning.setGeometry(QtCore.QRect(30, 20, 341, 91))
        self.label_warning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_warning.setObjectName(_fromUtf8("label_warning"))

        self.retranslateUi(DeployWindow)
        QtCore.QMetaObject.connectSlotsByName(DeployWindow)

    def retranslateUi(self, DeployWindow):
        DeployWindow.setWindowTitle(_translate("DeployWindow", "Deploy Project", None))
        self.buttonAccept.setText(_translate("DeployWindow", "Accept", None))
        self.buttonCancel.setText(_translate("DeployWindow", "Cancel", None))
        self.label_warning.setText(_translate("DeployWindow", "TextLabel", None))

import icons_rc
