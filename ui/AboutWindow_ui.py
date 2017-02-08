# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import changelog

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

class ExtendedQLabel(QtGui.QLabel):
 
    def __init(self, parent):
        QtGui.QLabel.__init__(self, parent)
 
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.emit(QtCore.SIGNAL('clicked()'))

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutWindow.setWindowFlags(QtCore.Qt.Window |
                                  QtCore.Qt.WindowTitleHint |
                                  QtCore.Qt.WindowCloseButtonHint)
        AboutWindow.resize(500, 500)
        AboutWindow.setFixedSize(AboutWindow.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/compare.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setStyleSheet(_fromUtf8("QDialog {\n"
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
"QLabel#label_title {\n"
"    color: #386bd2;\n"
"    font-size: 20px;\n"
"    font-family: Candara, Calibri, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QLabel#label_change {\n"
"    font-size: 12px;\n"
"    font-family: Tahoma, Verdana, Segoe, sans-serif;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
""))
        AboutWindow.setSizeGripEnabled(False)
        self.frame = QtGui.QFrame(AboutWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 481, 71))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_icon = QtGui.QLabel(self.frame)
        self.label_icon.setGeometry(QtCore.QRect(10, 10, 41, 51))
        self.label_icon.setText(_fromUtf8(""))
        self.label_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/compare.ico")))
        self.label_icon.setObjectName(_fromUtf8("label_icon"))
        self.label_title = QtGui.QLabel(self.frame)
        self.label_title.setGeometry(QtCore.QRect(60, 20, 301, 31))
        self.label_title.setStyleSheet(_fromUtf8(""))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.widget_details = QtGui.QWidget(AboutWindow)
        self.widget_details.setGeometry(QtCore.QRect(10, 96, 481, 71))
        self.widget_details.setStyleSheet(_fromUtf8("QWidget {\n"
"    font-size: 12px;\n"
"    font-family: Tahoma, Verdana, Segoe, sans-serif;\n"
"    padding-left: 10px;\n"
"}\n"
""))
        self.widget_details.setObjectName(_fromUtf8("widget_details"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_details)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_details = QtGui.QLabel(self.widget_details)
        self.label_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_details.setObjectName(_fromUtf8("label_details"))
        self.horizontalLayout.addWidget(self.label_details)
        self.label_contact = ExtendedQLabel(self.widget_details)#QtGui.QLabel(self.widget_details)
        #self.label_contact.setTextFormat(QtCore.Qt.RichText)
        self.label_contact.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_contact.setOpenExternalLinks(True)
        self.label_contact.setObjectName(_fromUtf8("label_contact"))
        self.horizontalLayout.addWidget(self.label_contact)
        self.label_change = QtGui.QLabel(AboutWindow)
        self.label_change.setGeometry(QtCore.QRect(20, 190, 451, 291))
        self.label_change.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_change.setObjectName(_fromUtf8("label_change"))

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About", None))
        self.label_title.setText(_translate("AboutWindow", "SSIS Deployment Checker", None))
        self.label_details.setText(_translate("AboutWindow", details_text(), None))
        #self.label_contact.setText(_translate("AboutWindow", "<html><head/><body><p>Contact</p><p><a href=\"mailto:pglucas@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">pglucas@gmail.com</span></a></p></body></html>", None))
        self.label_contact.setText(_translate("AboutWindow", "Contact\nPGLucas87@gmail.com", None))
        self.label_change.setText(_translate("AboutWindow", changelog_text(), None))

def details_text():
    """Creates the details text, pulling in the altest version."""
    text =  "SSIS Deployment Checker\n©2016, Paul Lucas\nVersion {}"
    version = changelog.main()[-1]

    return text.format(version[0])

def changelog_text():
    """Creates changelog history text."""
    text = 'Changelog:'
    fmt = '\n{:5} - {}'
    for version, description in changelog.main():
        text += fmt.format(version, description)

    return text

import icons_rc
