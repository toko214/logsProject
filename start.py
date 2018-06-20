from PyQt4 import QtGui, QtCore
import sys
import design
import MainEngine
import os
import chrome_ui
import threading
import xlwt
import find


class FindApp(QtGui.QMainWindow, find.Ui_MainWindow):
    def __init__(self, parent=None):
        super(FindApp, self).__init__(parent)
        self.setupUi(self)
        self.parent_window = parent
        self.start_index = 0
        self.pushButton.clicked.connect(self.find_in_tree)
        self.pushButton_2.clicked.connect(self.close)
        self.items = []
        self.current_key = ""
        self.no_items_found = False

    def find_in_tree(self):
        key = self.lineEdit.text()
        if key != self.current_key:
            self.no_items_found = False
            self.current_key = key
            self.items = []
            for i in range(self.parent_window.header_count):
                items = self.parent_window.treeWidget.findItems(key, QtCore.Qt.MatchContains, i)
                if items:
                    self.items.append([i, items])
            if not self.items:
                message_box(self=self, title="No Items Found", txt="No Items Found With this keyword")
                self.no_items_found = True
            else:
                self.progress()
        else:
            if not self.no_items_found:
                if self.items:
                    self.progress()
                else:
                    message_box(self=self, title="No More Items", txt="No More Items Found")
            else:
                message_box(self=self, title="No Items Found", txt="No Items Found With this keyword")

    def progress(self):
        for j in self.items:
            if j[1]:
                self.parent_window.treeWidget.setCurrentItem(j[1][0], j[0])
                self.items[self.items.index(j)][1].remove(j[1][0])
                print self.items
                if not j[1]:
                    self.items.remove(j)
                break
            else:
                self.items.remove(j)
                print self.items

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.pushButton.click()


class GeneralSubApp(QtGui.QMainWindow, chrome_ui.general_ui):
    def __init__(self, parent=None, items=None, index=None, tree_items=None, name=""):
        super(GeneralSubApp, self).__init__(parent)
        self.setupUi(self, items, name)
        self.header_count = len(items)
        self.items_count = len(tree_items)
        self.index = index
        self.actionExit.triggered.connect(self.close)
        self.actionSave_Selected_Items.triggered.connect(self.tree_to_xl)
        self.actionSave_Selected_Items.setShortcut(QtGui.QKeySequence('Ctrl+S'))
        self.actionFind.triggered.connect(self.open_find_ui)
        self.actionFind.setShortcut(QtGui.QKeySequence('Ctrl+F'))
        self.actionSelect_All.triggered.connect(self.treeWidget.selectAll)
        self.actionSelect_All.setShortcut(QtGui.QKeySequence('Ctrl+A'))
        self.actionDeselect_All.triggered.connect(self.treeWidget.clearSelection)
        self.actionDeselect_All.setShortcut(QtGui.QKeySequence('Ctrl+D'))
        self.children_windows = []
        for i in tree_items:
            j = QtGui.QTreeWidgetItem(self.treeWidget, i)
            self.treeWidget.addTopLevelItem(j)

    def closeEvent(self, event):
        self.index.setDisabled(False)
        for i in self.children_windows:
            i.close()

    def open_find_ui(self):
        form = FindApp(self)
        self.children_windows.append(form)
        form.show()

    def tree_to_xl(self):
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = []
        for i in range(self.header_count):
            columns.append(str(self.treeWidget.headerItem().text(i)))
        for col_num in range(self.header_count):
            ws.write(0, col_num, columns[col_num], font_style)
            ws.col(col_num).width = 256 * 40
        font_style = xlwt.XFStyle()
        if len(self.treeWidget.selectedItems()) == self.items_count:
            for row_num in range(self.treeWidget.topLevelItemCount()):
                for col_num in range(self.header_count):
                    ws.write(row_num + 1, col_num, str(self.treeWidget.topLevelItem(row_num).text(col_num)), font_style)
        else:
            items = self.treeWidget.selectedItems()
            x = 0
            for item in items:
                for col_num in range(self.header_count):
                    ws.write(x + 1, col_num, str(item.text(col_num)),
                             font_style)
                x += 1
        wb.save("asd.xls")


class GeneralApp(QtGui.QMainWindow, chrome_ui.general_apps_ui):
    def __init__(self,parent=None, index=None, tree_items=None, name=None):
        super(GeneralApp, self).__init__(parent)
        self.setupUi(self, tree_items, name)
        self.treeWidget.itemDoubleClicked.connect(self.tree_handle)
        self.index = index
        self.actionExit.triggered.connect(self.close)

    def start_tree_thread(self, index):
        t = threading.Thread(target=self.tree_handle, args=(index,))
        t.start()

    def tree_handle(self, index):
        if not index.isDisabled():
            name = index.text(0).split(" ")
            if name[0] == "Chrome":
                if name[1] == "Password":
                    index.setDisabled(True)
                    passwords = MainEngine.ce.ChromeEngine().get_chrome_saved_password()
                    tree_items = []
                    for i in passwords:
                        tree_items.append([i[0], i[1], i[2]])
                    items = [[0, "Website"], [1, "Username"], [2, "Password"]]
                    form = GeneralSubApp(self, items=items,index=index, tree_items=tree_items, name=name)
                    form.show()
                if name[1] == "History":
                    index.setDisabled(True)
                    history = MainEngine.ce.ChromeEngine().get_chrome_history()
                    tree_items = []
                    for i in history:
                        tree_items.append([history[i]['url'], str(history[i]['visit_time']),str(history[i]['visit_duration']), str(len(history[i]['visit_time']))])
                    items = [[0, "Url"], [1, "Visit Time"], [2, "Visit Duration"], [3, "Times Visited"]]
                    form = GeneralSubApp(self, items=items,index=index, tree_items= tree_items, name=name)
                    form.show()
                if name[1] == "Cookies":
                    index.setDisabled(True)
                    cookies = MainEngine.ce.ChromeEngine().get_cookies()
                    tree_items = []
                    for i in cookies:
                        for k in cookies[i]:
                            tree_items.append([i, k['name'], k['value'], k['expire'], k['time_created']])
                    items = [[0, "Url"], [1, "Name"], [2, "Value"], [3, "Expire"], [4, "Time Created"]]
                    form = GeneralSubApp(self, items=items, index=index, tree_items=tree_items, name=name)
                    form.show()
            #if name[0] == "Firefox":

    def closeEvent(self, event):
        self.index.setDisabled(False)


class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton_2.clicked.connect(self.browse_file)
        # self.pushButton.clicked.connect(self.analyze)
        self.dir_path = os.getcwd() + "\logs\\"
        self.actionExit.triggered.connect(self.close)
        self.treeWidget_2.itemDoubleClicked.connect(self.check_index)
        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))
        self.dialog = QtGui.QDialog(self)
        self.dialog.setFocusPolicy(QtCore.Qt.StrongFocus)

    def check_index(self,index):
        if not index.isDisabled():
            name = index.text(0)
            if name == "Chrome":
                index.setDisabled(True)
                tree_items = [[0, "Password"], [1, "Cache"], [2, "Bookmarks"], [3, "History"], [4, "Cookies"]]
                form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                form.show()
            if name == "Firefox":
                index.setDisabled(True)
                tree_items = [[0, "Password"], [1, "Bookmarks"], [2, "History"], [3, "Cookies"]]
                form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                form.show()

    def browse_file(self):
        file = str(QtGui.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(file)
        QtGui.QTreeWidgetItem.checkState()

    def focusOutEvent(self, event):
        print "Asd"
        self.setFocus(True)
        # self.activateWindow()
        # self.raise_()
        # self.show()


# def changedFocusSlot(old, new):
#     print "old   " + str(old)
#     print "new   " + str(new)
#     window = QtGui.QApplication.activeWindow()
#     if window != None and old != None and new != None:
#         print window.windowTitle()


    #     window.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    # # if (now!=None):
    # #     # QtGui.QApplication.activeWindow().raise_()
    # #     # QtGui.QApplication.activeWindow().show()
    # #     now.setWindowState(now.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    # #     now.activateWindow()
    # #     # now.raise_()
    # #     # now.show()
    # #     # now.activateWindow()

def message_box(self=None, title="", txt=""):
    msg = QtGui.QMessageBox(self)
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText(txt)
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle(title)
    # msg.setDetailedText("The details are as follows:")
    msg.show()

def main():
    app = QtGui.QApplication(sys.argv)
    #QtCore.QObject.connect(app, QtCore.SIGNAL("focusChanged(QWidget *, QWidget *)"), changedFocusSlot)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()