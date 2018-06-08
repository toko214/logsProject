from PyQt4 import QtGui, QtCore
import sys
import design
import MainEngine
import os
import PyQt4
import chrome_ui
import chrome_history


class ChromeHistoryApp(QtGui.QMainWindow, chrome_history.Ui_MainWindow):
    def __init__(self, parent=None, items=None, index=None):
        super(ChromeHistoryApp, self).__init__(parent)
        self.setupUi(self)
        self.index = index
        for i in items:
            #j = QtGui.QTreeWidgetItem(self.treeWidget, [str(items[i]['url']), str(items[i]['visit_time']), str(items[i]['visit_duration']),len(items[i]['visit_time'])])
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
    def __init__(self,parent=None):
        super(ChromeApp, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.itemDoubleClicked.connect(self.tree_handle)

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
            pass


    def closeEvent(self, event):
        self.parent().setDisabled(False)
        self.close()


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton_2.clicked.connect(self.browse_file)
        # self.pushButton.clicked.connect(self.analyze)
        self.dir_path = os.getcwd() + "\logs\\"
        self.treeWidget_2.itemDoubleClicked.connect(self.gg)
        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))
    def gg(self,index):
        if index.text(0) == "Chrome":
            self.setDisabled(True)
            form = ChromeApp(self)
            form.show()

    def analyze(self):
        root = self.treeWidget.invisibleRootItem()
        item = root.child(0)
        child_count = item.childCount()
        child_dict = {}
        for j in range(child_count):
            item2 = item.child(j)
            name = str(item2.text(0))
            child_dict[name] = {}
            child_count3 = item2.childCount()
            if child_count3 == 0:
                if item2.checkState(0) == 2:
                    child_dict[name] = True
                else:
                    child_dict[name] = False
            else:
                state = item2.checkState(0)
                if state == 1:
                    for k in range(child_count3):
                        item3 = item2.child(k)
                        name2 = str(item3.text(0))
                        if item3.checkState(0) == 2:
                            child_dict[name][name2] = True
                        else:
                            child_dict[name][name2] = False
                    child_dict[name]['state'] = 1
                elif state == 2:
                    child_dict[name]['state'] = 2
                else:
                    child_dict[name]['state'] = 0
        MainEngine.MainEngine().do(child_dict)

    def browse_file(self):
        file = str(QtGui.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(file)
        QtGui.QTreeWidgetItem.checkState()


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()