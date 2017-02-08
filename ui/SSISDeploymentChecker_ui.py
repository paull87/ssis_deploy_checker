# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SSISDeploymentChecker.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QStyledItemDelegate
from PyQt4.QtGui import QCommonStyle

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setWindowFlags(QtCore.Qt.Window |
                                  QtCore.Qt.WindowTitleHint |
                                  QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/compare.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8('''QWidget#centralwidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #e0effa, stop:1 rgba(255, 255, 255, 255));
                }
                /* Combo Box Styles*/
                QComboBox {
                        padding: 6px 12px;
                        font-size: 14px;
                        color: #555;
                        background-color: #fff;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                }
                QComboBox:focus{
                        border-color: #66afe9;
                        outline: 0;
                }
                QComboBox:editable:on {
                         border-color: #66afe9;
                }

                /*Combo Box DropDown Button*/
                QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                    border-left-width: 1px;
                    border-left-color: #ccc;
                    border-left-style: solid; /* just a single line */
                    border-top-right-radius: 4px; /* same radius as the QComboBox */
                    border-bottom-right-radius: 4px;
                        background-color: #fff;
                }
                QComboBox::drop-down:hover {
                        border-color: #66afe9;
                        background-color: #66afe9;
                }

                /*Combo Box DropDown Arrow*/
                QComboBox::down-arrow {
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #fff;
                        border-right: 4px solid #fff;
                        border-top: 4px solid #66afe9;
                }
                QComboBox::down-arrow:hover {
                width: 0; 
                  height: 0; 
                  border-left: 4px solid #66afe9;
                  border-right: 4px solid #66afe9;
                  border-top: 4px solid #fff;}

                /*Combo Box DropDown List*/
                QComboBox QAbstractItemView::item {
                        padding: 6px 12px;
                        font-size: 14px;
                        color: #555; 
                }

                QComboBox QAbstractItemView {
                        border: 1px solid #66afe9;
                }
            
                QToolBar {
                    background-color: #b2d7f4;
                        border: transparent
                }
                QMenuBar {
                    background-color: #66afe9;
                font-size:14px;
                /*font-family: Century Gothic, sans-serif;*/
                font-family: Futura, "Trebuchet MS", Arial, sans-serif;
                }
                QMenuBar::item {
                    spacing: 10px; /* spacing between menu bar items */
                    padding: 8px 10px;
                    background: transparent;
                    border-radius: 4px;
                        color: #fff;
                        font: 20px;
                }
                QMenuBar::item:selected { /* when selected using mouse or keyboard */
                    background: #518cba;
                }

                QMenuBar::item:pressed {
                    background: #3d698b;
                }                
                QMenu {
                    background-color: #66afe9; /* sets background of the menu */
                    border: transparent;
                        border-radius: 4px;
                }

                QMenu::item {
                    /* sets background of menu item. set this to something non-transparent
                        if you want menu color and menu item color to be different */
                    background-color: transparent;
                }
                QMenu::item:selected {
                    background-color: #518cba;
                }
                QMenu::item:pressed {
                    background-color: #3d698b;
                }'''))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        item_delegate = QtGui.QStyledItemDelegate()
        
        # Server Combo Box
        self.comboServer = QtGui.QComboBox(self.centralwidget)
        self.comboServer.setGeometry(QtCore.QRect(40, 30, 161, 31))
        self.comboServer.setStyleSheet(_fromUtf8(""))
        self.comboServer.setEditable(True)
        self.comboServer.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.comboServer.setObjectName(_fromUtf8("comboServer"))
        self.comboServer.lineEdit().setPlaceholderText('Enter Server')
        self.comboServer.setCurrentIndex(0)
        self.comboServer.setItemDelegate(item_delegate)
        #self.comboServer.view().parentWidget().setWindowFlags(QtCore.Qt.SplashScreen)
        
        # File Combo Box
        self.comboFile = QtGui.QComboBox(self.centralwidget)
        self.comboFile.setGeometry(QtCore.QRect(40, 80, 601, 33))
        self.comboFile.setStyleSheet(_fromUtf8(""))
        self.comboFile.setEditable(True)
        self.comboFile.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.comboFile.setObjectName(_fromUtf8("comboFile"))
        self.comboFile.lineEdit().setPlaceholderText('Local Solution Folder')
        self.comboFile.setCurrentIndex(0)
        self.comboFile.setItemDelegate(item_delegate)

        # Project Combo Box
        self.comboProject = QtGui.QComboBox(self.centralwidget)
        self.comboProject.setGeometry(QtCore.QRect(340, 30, 210, 31))
        self.comboProject.setStyleSheet(_fromUtf8(""))
        self.comboProject.setEditable(True)
        self.comboProject.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.comboProject.setObjectName(_fromUtf8("comboProject"))
        self.comboProject.setCurrentIndex(0)
        self.comboProject.setItemDelegate(item_delegate)
        self.comboProject.hide()

        # Browse Button
        self.buttonBrowse = QtGui.QPushButton(self.centralwidget)
        self.buttonBrowse.setGeometry(QtCore.QRect(660, 80, 81, 31))
        self.buttonBrowse.setStyleSheet(_fromUtf8('''QPushButton {
                        font-size: 14px;
                        border: 2px solid transparent;
                        border-radius: 4px;
                        color: #66afe9;
                        background-color: #fff;
                        border-color: rgb(185, 185, 185);
                }

                QPushButton:hover {
                        color: #fff;
                        background-color: #66afe9;
                        border-color: #66afe9;
                }
                QPushButton:pressed {
                        color: #fff;
                        background-color: #518cba;
                        border-color: #518cba;
                }'''))
        self.buttonBrowse.setObjectName(_fromUtf8("buttonBrowse"))

        # Compare Button
        self.buttonCompare = QtGui.QPushButton(self.centralwidget)
        self.buttonCompare.setGeometry(QtCore.QRect(360, 160, 81, 31))
        self.buttonCompare.setStyleSheet(_fromUtf8('''QPushButton {
                        font-size: 14px;
                        border: 2px solid transparent;
                        border-radius: 4px;
                        color: #66afe9;
                        background-color: #fff;
                        border-color: rgb(185, 185, 185);
                }

                QPushButton:hover {
                        color: #fff;
                        background-color: #66afe9;
                        border-color: #66afe9;
                }
                QPushButton:pressed {
                        color: #fff;
                        background-color: #518cba;
                        border-color: #518cba;
                }'''))
        self.buttonCompare.setObjectName(_fromUtf8("buttonCompare"))
        
        # Server Success Label
        self.labelSuccessImage = QtGui.QLabel(self.centralwidget)
        self.labelSuccessImage.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.labelSuccessImage.setText(_fromUtf8(""))
        self.labelSuccessImage.setScaledContents(True)
        self.labelSuccessImage.setObjectName(_fromUtf8("labelSuccessImage"))
        
        # File Success Label
        self.labelSuccessImage_File = QtGui.QLabel(self.centralwidget)
        self.labelSuccessImage_File.setGeometry(QtCore.QRect(10, 80, 31, 31))
        self.labelSuccessImage_File.setText(_fromUtf8(""))
        self.labelSuccessImage_File.setScaledContents(True)
        self.labelSuccessImage_File.setObjectName(_fromUtf8("labelSuccessImage_File"))

        # Tree Widget
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 230, 761, 281))
        self.treeWidget.setStyleSheet(_fromUtf8('''/* Tree View Settings */
                QTreeView {
                    padding: 3px 3px;
                        padding-right: 3px;
                        font-size: 14px;
                        color: #555;
                        background-color: #fff;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                }
                QTreeView::item:selected {
                        font-weight: bold;
                }

                /* Header Settings */
                QHeaderView {
                        height: 70px;
                        font-size: 16px;
                        color: rgb(53, 53, 53);
                        background-color: #fff;
                }

                /* Scroll Bar Settings */
                QScrollBar:vertical {
                     border-left: 1px solid #ccc;
                        border-right: 1px solid #ccc;
                     background: #fff;
                     width: 15px;
                     margin: 22px 0 22px 0;
                 }
                /* Scroll Bar Handle */
                 QScrollBar::handle:vertical {
                     background: #66afe9;
                     max-height: 10px;
                 }
                 QScrollBar::handle:vertical:hover {
                     background: #518cba;
                     max-height: 10px;
                 }
                QScrollBar::handle:vertical:pressed {
                     background: #3d698b;
                     max-height: 10px;
                 }
                /* Scroll Bar Bottom Button Settings */
                 QScrollBar::add-line:vertical {
                     border: 1px solid #ccc;
                     background: #fff;
                     height: 20px;
                     subcontrol-position: bottom;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-bottom-left-radius: 4px;
                 }
                 QScrollBar::add-line:vertical:hover {
                     border: 1px solid #ccc;
                     background: #66afe9;
                     height: 20px;
                     subcontrol-position: bottom;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-bottom-left-radius: 4px;
                 }
                 QScrollBar::add-line:vertical:pressed {
                     border: 1px solid #ccc;
                     background: #518cba;
                     height: 20px;
                     subcontrol-position: bottom;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-bottom-left-radius: 4px;
                 }
                /* Scroll Bar Top Button Settings */
                 QScrollBar::sub-line:vertical {
                     border: 1px solid #ccc;
                     background: #fff;
                     height: 20px;
                     subcontrol-position: top;
                     subcontrol-origin: margin;
                        border-top-right-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                  QScrollBar::sub-line:vertical:hover {
                     border: 1px solid #ccc;
                     background: #66afe9;
                     height: 20px;
                     subcontrol-position: top;
                     subcontrol-origin: margin;
                        border-top-right-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                 QScrollBar::sub-line:vertical:pressed {
                     border: 1px solid #ccc;
                     background: #518cba;
                     height: 20px;
                     subcontrol-position: top;
                     subcontrol-origin: margin;
                        border-top-right-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                /* Scroll Bar Down Arrow Settings */
                QScrollBar::down-arrow:vertical {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #fff;
                        border-right: 4px solid #fff;
                        border-top: 4px solid #66afe9;
                }
                QScrollBar::down-arrow:vertical:hover {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #66afe9;
                        border-right: 4px solid #66afe9;
                        border-top: 4px solid #fff;
                }
                QScrollBar::down-arrow:vertical:pressed {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #518cba;
                        border-right: 4px solid #518cba;
                        border-top: 4px solid #fff;
                }
                /* Scroll Bar Up Arrow Settings */
                QScrollBar::up-arrow:vertical {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #fff;
                        border-right: 4px solid #fff;
                        border-bottom: 4px solid #66afe9;
                }
                QScrollBar::up-arrow:vertical:hover {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #66afe9;
                        border-right: 4px solid #66afe9;
                        border-bottom: 4px solid #fff;
                }
                QScrollBar::up-arrow:vertical:pressed {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-left: 4px solid #518cba;
                        border-right: 4px solid #518cba;
                        border-bottom: 4px solid #fff;
                }
                 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                     background: none;
                 }
                /* Scroll Bar Settings */
                QScrollBar:horizontal {
                     border-top: 1px solid #ccc;
                        border-bottom: 1px solid #ccc;
                     background: #fff;
                     height: 15px;
                     margin: 0 22px 0 22px;
                 }
                /* Scroll Bar Handle */
                 QScrollBar::handle:horizontal {
                     background: #66afe9;
                    min-width: 20px;
                 }
                 QScrollBar::handle:horizontal:hover {
                     background: #518cba;
                    min-width: 20px;
                 }
                QScrollBar::handle:horizontal:pressed {
                     background: #3d698b;
                        min-width: 20px;
                 }
                /* Scroll Bar Right Button Settings */
                 QScrollBar::add-line:horizontal {
                     border: 1px solid #ccc;
                     background: #fff;
                     width: 20px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-top-right-radius: 4px;
                 }
                 QScrollBar::add-line:horizontal:hover {
                     border: 1px solid #ccc;
                     background: #66afe9;
                     width: 20px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-top-right-radius: 4px;
                 }
                 QScrollBar::add-line:horizontal:pressed {
                     border: 1px solid #ccc;
                     background: #518cba;
                     width: 20px;
                     subcontrol-position: right;
                     subcontrol-origin: margin;
                        border-bottom-right-radius: 4px;
                        border-top-right-radius: 4px;
                 }
                /* Scroll Bar Left Button Settings */
                 QScrollBar::sub-line:horizontal {
                     border: 1px solid #ccc;
                     background: #fff;
                     width: 20px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                        border-bottom-left-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                  QScrollBar::sub-line:horizontal:hover {
                     border: 1px solid #ccc;
                     background: #66afe9;
                     width: 20px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                        border-bottom-left-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                 QScrollBar::sub-line:horizontal:pressed {
                     border: 1px solid #ccc;
                     background: #518cba;
                     width: 20px;
                     subcontrol-position: left;
                     subcontrol-origin: margin;
                        border-bottom-left-radius: 4px;
                        border-top-left-radius: 4px;
                 }
                /* Scroll Bar Left Arrow Settings */
                QScrollBar::left-arrow:horizontal {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #fff;
                        border-bottom: 4px solid #fff;
                        border-right: 4px solid #66afe9;
                }
                QScrollBar::left-arrow:horizontal:hover {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #66afe9;
                        border-bottom: 4px solid #66afe9;
                        border-right: 4px solid #fff;
                }
                QScrollBar::left-arrow:horizontal:pressed {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #518cba;
                        border-bottom: 4px solid #518cba;
                        border-right: 4px solid #fff;
                }
                /* Scroll Bar Right Arrow Settings */
                QScrollBar::right-arrow:horizontal {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #fff;
                        border-bottom: 4px solid #fff;
                        border-left: 4px solid #66afe9;
                }
                QScrollBar::right-arrow:horizontal:hover {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #66afe9;
                        border-bottom: 4px solid #66afe9;
                        border-left: 4px solid #fff;
                }
                QScrollBar::right-arrow:horizontal:pressed {
                        subcontrol-origin: margin;
                        subcontrol-position: center;
                        width: 0; 
                        height: 0; 
                        border-top: 4px solid #518cba;
                        border-bottom: 4px solid #518cba;
                        border-left: 4px solid #fff;
                }
                 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                     background: none;
                 }'''))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.project_icon = QtGui.QIcon()
        self.project_icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/project.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folder_icon = QtGui.QIcon()
        self.folder_icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.package_icon = QtGui.QIcon()
        self.package_icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/package.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.success_icon = QtGui.QIcon()
        self.success_icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/green_tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.error_icon = QtGui.QIcon()
        self.error_icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/red_cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setMinimumSectionSize(50)
        self.treeWidget.header().setStretchLastSection(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.statusBar().setSizeGripEnabled(False) 
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionReset = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon1)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tool_tips = {
            '1.No Server Version':
                'The local packages are not in the server project.',
            '2.No Local Version':
                'The server packages are not in the local project.',
            '3.Upgraded Version':
                'These packages have newer versions on the local project.',
            '4.Downgraded Version':
                'These packages have older versions on the local project.',
            }

    def server_success(self):
        """Change labels to show successful server connection."""
        self.comboServer.setStyleSheet(_fromUtf8("QComboBox {\n"
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    color: rgb(0, 170, 0);\n"
"    background-color: #fff;\n"
"    border: 1px solid rgb(0, 170, 0);\n"
"    border-radius: 4px;\n"
"}\n"))
        self.labelSuccessImage.setStyleSheet(_fromUtf8("QLabel {\n"
"    padding: 5px 5px;\n"
"}"))
        self.labelSuccessImage.setPixmap(QtGui.QPixmap(_fromUtf8(":/green_tick.png")))
        """self.labelSuccess.setStyleSheet(_fromUtf8("QLabel {\n"
"    font: 75 14pt;\n"
"    padding: 6px;\n"
"    font: bold;\n"
"    color: rgb(0, 170, 0);\n"
"}"))
        self.labelSuccess.setText(_translate("MainWindow", "Success", None))"""
        self.statusbar.showMessage("")

    def server_failure(self, error):
        """Change labels to show failed server connection."""
        self.comboServer.setStyleSheet(_fromUtf8("QComboBox {\n"                      
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    color: rgb(255, 0, 0);\n"
"    background-color: #fff;\n"
"    border: 1px solid rgb(255, 0, 0);\n"
"    border-radius: 4px;\n"
"}\n"))
        self.labelSuccessImage.setStyleSheet(_fromUtf8("QLabel {\n"
"    padding: 5px 5px;\n"
"}"))
        self.labelSuccessImage.setPixmap(QtGui.QPixmap(_fromUtf8(":/red_cross.png")))
        """self.labelSuccess.setStyleSheet(_fromUtf8("QLabel {\n"
"    font: 75 14pt;\n"
"    padding: 6px;\n"
"    font: bold;\n"
"    color: rgb(255, 0, 0);\n"
"}"))
        self.labelSuccess.setText(_translate("MainWindow",
                                             "Error", None))"""
        self.statusbar.showMessage(error)

    def server_neutral(self):
        """Hide server connection status."""
        self.comboServer.setStyleSheet(_fromUtf8(""))
        self.labelSuccessImage.setPixmap(QtGui.QPixmap(_fromUtf8("")))
        """self.labelSuccess.setText(_translate("MainWindow", "", None))"""
        self.statusbar.showMessage("")

    def folder_success(self):
        """Change labels to show folder is a directory."""
        self.comboFile.setStyleSheet(_fromUtf8("QComboBox {\n"
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    color: rgb(0, 170, 0);\n"
"    background-color: #fff;\n"
"    border: 1px solid rgb(0, 170, 0);\n"
"    border-radius: 4px;\n"
"}\n"))
        self.labelSuccessImage_File.setStyleSheet(_fromUtf8("QLabel {\n"
"    padding: 5px 5px;\n"
"}"))
        self.labelSuccessImage_File.setPixmap(QtGui.QPixmap(_fromUtf8(":/green_tick.png")))
        """self.labelSuccess.setStyleSheet(_fromUtf8("QLabel {\n"
"    font: 75 14pt;\n"
"    padding: 6px;\n"
"    font: bold;\n"
"    color: rgb(0, 170, 0);\n"
"}"))
        self.labelSuccess.setText(_translate("MainWindow", "Success", None))"""
        self.statusbar.showMessage("")

    def folder_failure(self, error):
        """Change labels to show the folder is not a directory."""
        self.comboFile.setStyleSheet(_fromUtf8("QComboBox {\n"                      
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    color: rgb(255, 0, 0);\n"
"    background-color: #fff;\n"
"    border: 1px solid rgb(255, 0, 0);\n"
"    border-radius: 4px;\n"
"}\n"))
        self.labelSuccessImage_File.setStyleSheet(_fromUtf8("QLabel {\n"
"    padding: 5px 5px;\n"
"}"))
        self.labelSuccessImage_File.setPixmap(QtGui.QPixmap(_fromUtf8(":/red_cross.png")))
        """self.labelSuccess.setStyleSheet(_fromUtf8("QLabel {\n"
"    font: 75 14pt;\n"
"    padding: 6px;\n"
"    font: bold;\n"
"    color: rgb(255, 0, 0);\n"
"}"))
        self.labelSuccess.setText(_translate("MainWindow",
                                             "Error", None))"""
        self.statusbar.showMessage(error)

    def folder_neutral(self):
        """Hide folder check status."""
        self.comboFile.setStyleSheet(_fromUtf8(""))
        self.labelSuccessImage_File.setPixmap(QtGui.QPixmap(_fromUtf8("")))
        """self.labelSuccess.setText(_translate("MainWindow", "", None))"""
        self.statusbar.showMessage("")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SSIS Deployment Check", None))
        self.buttonBrowse.setText(_translate("MainWindow", "Browse", None))
        self.buttonCompare.setText(_translate("MainWindow", "Compare", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Project", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Local", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Server", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.setColumnWidth(0, 450)
        self.treeWidget.setColumnWidth(1, 150)
        self.treeWidget.setColumnWidth(2, 150)
        
        

import icons_rc
