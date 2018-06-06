from PyQt4 import QtGui, QtCore
import sys
import design
import MainEngine
import os

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.analyze)
        self.dir_path = os.getcwd() + "/logs"
        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))

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
        MainEngine.MainEngine().do(child_dict,str(self.lineEdit.text()))

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