# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cookies.ui'
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
        MainWindow.resize(890, 542)
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setToolTip(_fromUtf8(""))
        self.treeWidget.setStatusTip(_fromUtf8(""))
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menubar.setMouseTracking(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setMouseTracking(False)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setMouseTracking(False)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setMouseTracking(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setMouseTracking(False)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
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
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTurorial = QtGui.QAction(MainWindow)
        self.actionTurorial.setObjectName(_fromUtf8("actionTurorial"))
        self.actionShow_Grid_Lines = QtGui.QAction(MainWindow)
        self.actionShow_Grid_Lines.setObjectName(_fromUtf8("actionShow_Grid_Lines"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.menuFile.addAction(self.actionSave_Selected_Items)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionDeselect_All)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionTurorial)
        self.menuView.addAction(self.actionShow_Grid_Lines)
        self.menuView.addAction(self.actionRefresh)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

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
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSave_Selected_Items.setText(_translate("MainWindow", "Save Selected Items                         Ctrl + S", None))
        self.actionSave_Selected_Items.setIconText(_translate("MainWindow", "Save Selected Items                         Ctrl + S", None))
        self.actionFind.setText(_translate("MainWindow", "Find                       Ctrl + F", None))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All              Ctrl + A", None))
        self.actionDeselect_All.setText(_translate("MainWindow", "Deselect All          Ctrl + D", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionTurorial.setText(_translate("MainWindow", "Tutorial", None))
        self.actionShow_Grid_Lines.setText(_translate("MainWindow", "Show Grid Lines", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh                                F5", None))

