from PyQt4 import QtGui, QtCore
import sys
import design
import MainEngine
import os
import chrome_ui


# class ChromeCookiesApp(QtGui.QMainWindow, chrome_ui.cookies_ui):
#     def __init__(self, parent=None, items=None, index=None):
#         super(ChromeCookiesApp, self).__init__(parent)
#         self.setupUi(self)
#         self.index = index
#         self.actionExit.triggered.connect(self.close)
#         for i in items:
#             for k in items[i]:
#                 j = QtGui.QTreeWidgetItem(self.treeWidget, [i, k['name'], k['value'], k['expire'], k['time_created']])
#                 self.treeWidget.addTopLevelItem(j)
#
#     def closeEvent(self, event):
#         self.index.setDisabled(False)
#         self.close()
#
#
# class ChromeHistoryApp(QtGui.QMainWindow, chrome_ui.history_ui):
#     def __init__(self, parent=None, items=None, index=None):
#         super(ChromeHistoryApp, self).__init__(parent)
#         self.setupUi(self)
#         self.index = index
#         for i in items:
#             j = QtGui.QTreeWidgetItem(self.treeWidget, [items[i]['url'],str(items[i]['visit_time']),str(items[i]['visit_duration']),str(len(items[i]['visit_time']))])
#             self.treeWidget.addTopLevelItem(j)
#
#     def closeEvent(self, event):
#         self.index.setDisabled(False)
#         self.close()
#
#
# class ChromePassApp(QtGui.QMainWindow, chrome_ui.pass_Ui):
#     def __init__(self, parent=None, items=None, index=None):
#         super(ChromePassApp, self).__init__(parent)
#         self.setupUi(self)
#         self.index = index
#         for i in items:
#             j = QtGui.QTreeWidgetItem(self.treeWidget, [i[0], i[1], i[2]])
#             self.treeWidget.addTopLevelItem(j)
#
#     def closeEvent(self, event):
#         self.index.setDisabled(False)
#         self.close()


class GeneralApp(QtGui.QMainWindow, chrome_ui.general_ui):
    def __init__(self, parent=None, items=None, index=None, tree_items=None, name=""):
        super(GeneralApp, self).__init__(parent)
        self.setupUi(self, tree_items)
        self.index = index
        self.actionExit.triggered.connect(self.close)
        if name == "pass":
            for i in items:
                j = QtGui.QTreeWidgetItem(self.treeWidget, [i[0], i[1], i[2]])
                self.treeWidget.addTopLevelItem(j)
        if name == "history":
            for i in items:
                j = QtGui.QTreeWidgetItem(self.treeWidget, [items[i]['url'],str(items[i]['visit_time']),str(items[i]['visit_duration']),str(len(items[i]['visit_time']))])
                self.treeWidget.addTopLevelItem(j)
        if name == "cookie":
            for i in items:
                    for k in items[i]:
                        j = QtGui.QTreeWidgetItem(self.treeWidget, [i, k['name'], k['value'], k['expire'], k['time_created']])
                        self.treeWidget.addTopLevelItem(j)

    def closeEvent(self, event):
        self.index.setDisabled(False)
        self.close()

class ChromeApp(QtGui.QMainWindow, chrome_ui.Ui_MainWindow):
    def __init__(self,parent=None, index=None):
        super(ChromeApp, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.itemDoubleClicked.connect(self.tree_handle)
        self.index = index
        self.statusbar.showMessage("Chrome Apps | 4")
        self.actionExit.triggered.connect(self.close)

    def tree_handle(self, index):
        if not index.isDisabled():
            if index.text(0) == "Chrome Passwords":
                index.setDisabled(True)
                passwords = MainEngine.ce.ChromeEngine().get_chrome_saved_password()
                tree_items = [[0, "Website"], [1, "Username"], [2, "Password"]]
                form = GeneralApp(self, items=passwords,index=index, tree_items=tree_items, name="pass")
                form.show()
            if index.text(0) == "Chrome History":
                index.setDisabled(True)
                history = MainEngine.ce.ChromeEngine().get_chrome_history()
                tree_items = [[0, "Url"], [1, "Visit Time"], [2, "Visit Duration"], [3, "Times Visited"]]
                form = GeneralApp(self, items=history,index=index, tree_items= tree_items, name="history")
                form.show()
            if index.text(0) == "Chrome Cookies":
                index.setDisabled(True)
                cookies = MainEngine.ce.ChromeEngine().get_cookies()
                tree_items = [[0, "Url"], [1, "Name"], [2, "Value"], [3, "Expire"], [4, "Time Created"]]
                form = GeneralApp(self, items=cookies, index=index, tree_items=tree_items, name="cookie")
                form.show()


    def closeEvent(self, event):
        self.index.setDisabled(False)
        self.close()


class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton_2.clicked.connect(self.browse_file)
        # self.pushButton.clicked.connect(self.analyze)
        self.dir_path = os.getcwd() + "\logs\\"
        self.treeWidget_2.itemDoubleClicked.connect(self.check_index)
        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))

    def check_index(self,index):
        if not index.isDisabled():
            if index.text(0) == "Chrome":
                index.setDisabled(True)
                form = ChromeApp(self, index)
                form.show()

    def browse_file(self):
        file = str(QtGui.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(file)
        QtGui.QTreeWidgetItem.checkState()


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()