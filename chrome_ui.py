# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chrome.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(569, 297)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 561, 251))
        self.treeWidget.setIndentation(0)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/key.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/notebook.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/history.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon2)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/cookie.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/accounting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon4)
        self.treeWidget.header().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave_Selected_Items = QtGui.QAction(MainWindow)
        self.actionSave_Selected_Items.setObjectName(_fromUtf8("actionSave_Selected_Items"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionDeselect_All = QtGui.QAction(MainWindow)
        self.actionDeselect_All.setObjectName(_fromUtf8("actionDeselect_All"))
        self.menuFile.addAction(self.actionSave_Selected_Items)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionDeselect_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrome", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Chrome Passowrds", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Chrome Bookmarks", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Chrome History", None))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Chrome Cookies", None))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Chrome Cache", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSave_Selected_Items.setText(_translate("MainWindow", "Save Selected Items", None))
        self.actionFind.setText(_translate("MainWindow", "Find", None))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All", None))
        self.actionDeselect_All.setText(_translate("MainWindow", "Deselect All", None))

class pass_Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(595, 358)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 591, 311))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setMinimumSectionSize(100)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrome Pass", None))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Site", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Username", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Password", None))


class history_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(739, 395)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setMinimumSectionSize(100)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrome History", None))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Url", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Visit Time", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Visit Duration", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Times Visited", None))

class cookies_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(872, 598)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(150)
        self.treeWidget.header().setMinimumSectionSize(150)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrome Cookies", None))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Website", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Name", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Value", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Expire", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Time Created", None))



