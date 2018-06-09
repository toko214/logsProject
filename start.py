from PyQt4 import QtGui, QtCore
import sys
import design
import MainEngine
import os
import PyQt4
import chrome_ui


class ChromeCookiesApp(QtGui.QMainWindow, chrome_ui.cookies_ui):
    def __init__(self, parent=None, items=None, index=None):
        super(ChromeCookiesApp, self).__init__(parent)
        self.setupUi(self)
        self.index = index
        for i in items:
            for k in items[i]:
                j = QtGui.QTreeWidgetItem(self.treeWidget, [i, k['name'], k['value'], k['expire'], k['time_created']])
                self.treeWidget.addTopLevelItem(j)

    def closeEvent(self, event):
        self.index.setDisabled(False)
        self.close()


class ChromeHistoryApp(QtGui.QMainWindow, chrome_ui.history_ui):
    def __init__(self, parent=None, items=None, index=None):
        super(ChromeHistoryApp, self).__init__(parent)
        self.setupUi(self)
        self.index = index
        for i in items:
            j = QtGui.QTreeWidgetItem(self.treeWidget, [items[i]['url'],str(items[i]['visit_time']),str(items[i]['visit_duration']),str(len(items[i]['visit_time']))])
            self.treeWidget.addTopLevelItem(j)

    def closeEvent(self, event):
        self.index.setDisabled(False)
        self.close()


class ChromePassApp(QtGui.QMainWindow, chrome_ui.pass_Ui):
    def __init__(self, parent=None, items=None, index=None):
        super(ChromePassApp, self).__init__(parent)
        self.setupUi(self)
        self.index = index
        for i in items:
            j = QtGui.QTreeWidgetItem(self.treeWidget, [i[0], i[1], i[2]])
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

    def tree_handle(self, index):
        if index.text(0) == "Chrome Passowrds":
            index.setDisabled(True)
            passwords = MainEngine.ce.ChromeEngine().get_chrome_saved_password()
            form = ChromePassApp(self, items=passwords,index=index)
            form.show()
        if index.text(0) == "Chrome History":
            index.setDisabled(True)
            history = MainEngine.ce.ChromeEngine().get_chrome_history()
            form = ChromeHistoryApp(self, items=history,index=index)
            form.show()
        if index.text(0) == "Chrome Cookies":
            index.setDisabled(True)
            cookies = MainEngine.ce.ChromeEngine().get_cookies()
            form = ChromeCookiesApp(self, items=cookies, index=index)
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
        self.treeWidget_2.itemDoubleClicked.connect(self.gg)
        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))

    def gg(self,index):
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