# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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
        MainWindow.resize(698, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/maple-leaf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget_2 = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setLineWidth(2)
        self.treeWidget_2.setIndentation(0)
        self.treeWidget_2.setExpandsOnDoubleClick(False)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/skype.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/development.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon2)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/mozilla.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/chrome.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon4)
        font = QtGui.QFont()
        font.setPointSize(8)
        item_0.setFont(2, font)
        self.treeWidget_2.header().setVisible(True)
        self.treeWidget_2.header().setDefaultSectionSize(120)
        self.treeWidget_2.header().setMinimumSectionSize(100)
        self.treeWidget_2.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.treeWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionTutorial)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.lab = QtGui.QLabel(MainWindow)
        self.lab.setText("")
        self.lab.setObjectName(_fromUtf8("lab"))
        self.statusbar.addWidget(self.lab)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Logs Taker", None))
        self.treeWidget_2.setSortingEnabled(True)
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Program", None))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Description", None))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "Version", None))
        self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "Last Updated", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Skype", None))
        self.treeWidget_2.topLevelItem(0).setText(2, _translate("MainWindow", "0.01", None))
        self.treeWidget_2.topLevelItem(0).setText(3, _translate("MainWindow", "29/2/2 15:15:15", None))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "Programs", None))
        self.treeWidget_2.topLevelItem(1).setText(2, _translate("MainWindow", "0.01", None))
        self.treeWidget_2.topLevelItem(1).setText(3, _translate("MainWindow", "30/2/2 15:15:15", None))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "Firefox", None))
        self.treeWidget_2.topLevelItem(2).setText(2, _translate("MainWindow", "0.01", None))
        self.treeWidget_2.topLevelItem(2).setText(3, _translate("MainWindow", "31/2/2 15:15:15", None))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("MainWindow", "Chrome", None))
        self.treeWidget_2.topLevelItem(3).setText(2, _translate("MainWindow", "0.01", None))
        self.treeWidget_2.topLevelItem(3).setText(3, _translate("MainWindow", "29/1/2 15:15:15", None))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))

