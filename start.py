# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PyQt4 import QtCore
import xlwt

from uis import general_ui, find, help, design
from Chrome import ChromeEngine as ce
from Skype import SkypeEngine as se
from Firefox import FireFoxEngine as ff
from Programs_installed import programs_installed as pi
from usefull_things import *

ch = ce.ChromeEngine()
fff = ff.FireFoxEngine()
sky = se.SkypeEngine()


class HelpApp(QtGui.QMainWindow, help.Ui_Form):
    def __init__(self, parent=None, text=1):
        super(HelpApp, self).__init__(parent)
        self.setupUi(self)
        if text == 1:
            self.textBrowser2.close()
            self.textBrowser3.close()
        elif text == 2:
            self.textBrowser1.close()
            self.textBrowser3.close()
        else:
            self.textBrowser1.close()
            self.textBrowser2.close()


class FindApp(QtGui.QMainWindow, find.Ui_MainWindow):
    def __init__(self, parent=None):
        super(FindApp, self).__init__(parent)
        self.setupUi(self)
        self.parent_window = parent
        self.pushButton.clicked.connect(self.find_in_tree)
        self.pushButton_2.clicked.connect(self.close)
        self.checkBox.clicked.connect(self.change_box1)
        self.checkBox_2.clicked.connect(self.change_box2)
        self.items = []
        self.current_key = ""
        self.current_state = False
        self.current_state2 = True
        self.state_changed = True
        self.no_items_found = False
        self.checkBox_2.setChecked(True)

        self.lab.setText(HELP_STR)

    def change_box1(self):
        if self.current_state:
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(False)
            self.current_state2 = False
        else:
            self.state_changed = True
            self.current_state = True
            self.current_state2 = False
            self.checkBox_2.setChecked(False)

    def change_box2(self):
        if self.current_state2:
            self.checkBox_2.setChecked(True)
            self.checkBox.setChecked(False)
            self.current_state = False
        else:
            self.state_changed = True
            self.current_state2 = True
            self.current_state = False
            self.checkBox.setChecked(False)

    def find_in_tree(self):
        key = self.lineEdit.text()
        if key != self.current_key or self.state_changed:
            self.no_items_found = False
            self.state_changed = False
            self.current_key = key
            self.items = []
            if self.checkBox.isChecked():
                match = QtCore.Qt.MatchExactly
            else:
                match = QtCore.Qt.MatchContains
            for i in range(self.parent_window.header_count):
                items = self.parent_window.treeWidget.findItems(key, match, i)
                if items:
                    self.items.append([i, items])
            if not self.items:
                message_box(self=self, title=NO_ITEMS_FOUND_TITLE, txt=NO_ITEMS_FOUND_TXT)
                self.no_items_found = True
            else:
                self.progress()
        else:
            if not self.no_items_found:
                if self.items:
                    self.progress()
                else:
                    message_box(self=self, title=NO_MORE_ITEMS_TITLE, txt=NO_MORE_ITEMS_TXT)
            else:
                message_box(self=self, title=NO_MORE_ITEMS_TITLE, txt=NO_MORE_ITEMS_TXT)

    def progress(self):
        for j in self.items:
            if j[1]:
                self.parent_window.treeWidget.setCurrentItem(j[1][0], j[0])
                self.items[self.items.index(j)][1].remove(j[1][0])
                if not j[1]:
                    self.items.remove(j)
                break
            else:
                self.items.remove(j)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.pushButton.click()


class GeneralSubApp(QtGui.QMainWindow, general_ui.general_ui):
    def __init__(self, parent=None, items=None, index=None, tree_items=None, name=""):
        super(GeneralSubApp, self).__init__(parent)
        self.setupUi(self, items, name)
        self.header_count = len(items)
        self.items_count = len(tree_items)
        self.lab.setText(ITEMS_COUNT_STR + str(self.items_count) + " | " + HELP_STR)
        self.index = index
        self.actionExit.triggered.connect(self.close)
        self.actionSave_Selected_Items.triggered.connect(self.tree_to_xl)
        self.actionSave_Selected_Items.setShortcut(QtGui.QKeySequence(SHOURCUT_CTRL_S))
        self.actionFind.triggered.connect(self.open_find_ui)
        self.actionFind.setShortcut(QtGui.QKeySequence(SHOURCUT_CTRL_F))
        self.actionSelect_All.triggered.connect(self.treeWidget.selectAll)
        self.actionSelect_All.setShortcut(QtGui.QKeySequence(SHOURCUT_CTRL_A))
        self.actionDeselect_All.triggered.connect(self.treeWidget.clearSelection)
        self.actionDeselect_All.setShortcut(QtGui.QKeySequence(SHOURCUT_CTRL_D))
        self.actionTurorial.triggered.connect(self.open_help_ui)
        self.children_windows = []

        for i in tree_items:
            j = QtGui.QTreeWidgetItem(self.treeWidget, i)
            self.treeWidget.addTopLevelItem(j)

    def closeEvent(self, event):
        self.index.setDisabled(False)
        for i in self.children_windows:
            i.close()

    def open_help_ui(self):
        form = HelpApp(self, text=3)
        self.children_windows.append(form)
        form.show()

    def open_find_ui(self):
        form = FindApp(self)
        self.children_windows.append(form)
        form.show()

    def tree_to_xl(self):
        wb = xlwt.Workbook(encoding='utf8')
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


class GeneralApp(QtGui.QMainWindow, general_ui.general_apps_ui):
    def __init__(self, parent=None, index=None, tree_items=None, name=None):
        super(GeneralApp, self).__init__(parent)
        self.setupUi(self, tree_items, name)
        self.treeWidget.itemDoubleClicked.connect(self.tree_handle)
        self.actionExit.triggered.connect(self.close)
        self.index = index
        self.children_windows = []
        self.actionTurorial.triggered.connect(self.open_help_ui)
        self.lab.setText(HELP_STR)

    def open_help_ui(self):
        form = HelpApp(self, text=2)
        self.children_windows.append(form)
        form.show()

    def tree_handle(self, index):
        if not index.isDisabled():
            index.setDisabled(True)
            name = index.text(0).split(" ")
            items = []
            tree_items = []
            if name[0] == CHROME_STR:
                if name[1] == PASSWORD_STR:
                    passwords = ch.get_chrome_saved_password()
                    for i in passwords:
                        tree_items.append([i[0], i[1], i[2]])
                    items.extend([[0, WEBSITE_STR], [1, USERNAME_STR], [2, PASSWORD_STR]])
                elif name[1] == HISTORY_STR:
                    history = ch.get_chrome_history()
                    for i in history[0]:
                        for j in range(len(history[0][i]['visit_time'])):
                            tree_items.append([history[0][i][URL_STR], history[0][i]['visit_time'][j], history[0][i]['visit_duration'][j], str(len(history[0][i]['visit_time']))])
                    for i in history[1]:
                        if history[1][i] != "":
                            for j in range(len(history[1][i]['visit_time'])):
                                tree_items.append(["Keyword: " + i, history[1][i]['visit_time'][j], history[1][i]['visit_duration'][j], str(len(history[1][i]['visit_time']))])
                        else:
                            tree_items.append(["Keyword: "+ i.encode('utf-8').decode('utf-8'), "", "", "1"])
                    items.extend([[0, URL_STR2], [1, "Visit Time"], [2, "Visit Duration"], [3, "Times Visited"]])
                else:
                    cookies = ch.get_cookies()
                    for i in cookies:
                        for k in cookies[i]:
                            tree_items.append([i, k['name'], k['value'], k['expire'], k['time_created']])
                    items.extend([[0, URL_STR2], [1, "Name"], [2, "Value"], [3, "Expire"], [4, "Time Created"]])
            elif name[0] == FIREFOX_STR:
                if name[1] == PASSWORD_STR:
                    passwords = fff.get_saved_password()
                    for i in passwords:
                        tree_items.append([i[0], i[1], i[2]])
                    items.extend([[0, WEBSITE_STR], [1, USERNAME_STR], [2, PASSWORD_STR]])
                elif name[1] == HISTORY_STR:
                    history = fff.get_history()
                    for i in history:
                        tree_items.append([history[i][URL_STR], str(history[i]["visit_dates"]), str(len(history[i]["visit_dates"]))])
                    items.extend([[0, URL_STR2], [1, "Visit Time"], [2, "Times Visited"]])
                elif name[1] == BOOKMARKS_STR:
                    bookmarks = fff.get_bookmarks()
                    for i in bookmarks:
                        tree_items.append([bookmarks[i][URL_STR], bookmarks[i]['date_added'], bookmarks[i]["date_modified"]])
                    items.extend([[0, URL_STR2], [1, "Date Added"], [2, "Date Modified"]])

                else:
                    cookies = fff.get_cookies()
                    for i in cookies:
                        for j in cookies[i]:
                            tree_items.append([i, j['name'], j['value'], j['creationTime'], j['expiry']])
                    items.extend([[0, WEBSITE_STR], [1, "Name"], [2, "Value"], [3, "Time Created"], [4, "Expire Date"]])

            elif name[0] == SKYPE_STR:
                if name[1] == "Contacts":
                    contacts = sky.get_contacts()
                    for i in contacts:
                        for j in i:
                            fullname = i[j]['fullname']
                            if fullname:
                                fullname = fullname.encode('utf-8').decode('utf-8')
                            else:
                                fullname = ""
                            country = i[j]['country']
                            if country:
                                country = country.encode('utf-8').decode('utf-8')
                            else:
                                country = ""
                            city = i[j]['city']
                            if city:
                                city = city.encode('utf-8').decode('utf-8')
                            else:
                                city = ""
                            email = ""
                            if 'email' in i[j]:
                                email = str(i[j]['email'])
                            tree_items.append([str(j), fullname, i[j]['birthday'], i[j]['gender'], country, city, str(i[j]['phones']), str(email), str(i[j]['realeted_urls']), str(i[j]['avatar_profile'])])
                    items.extend([[0, USERNAME_STR], [1, "Full Name"], [2, "Birthday"], [3, "Gender"], [4, "Country"], [5, "City"], [6, "Phone Numbers"], [7, "Email"], [8, "Realeted Urls"], [9, "Avatar Profile"]])
                elif name[1] == 'Messages':
                    messages = sky.get_messages()
                    for i in messages:
                        for j in i:
                            group = i[j]['group']
                            partis = ""
                            if 'participatins' in i[j]:
                                partis = i[j]['participatins']
                            for msg in i[j]['messages']:
                                if msg['message']:
                                    message = msg['message'].encode('utf-8').decode('utf-8')
                                else:
                                    message = ""
                                tree_items.append([str(group), str(partis), message.encode('utf-8').decode('utf-8'), str(msg['from']), str(msg['time'])])
                    items.extend([[0, "Group Chat"], [1, 'Participates'], [2, 'Message'], [3, 'From'], [4, "Time Sent"]])
                else:
                    accounts = sky.get_accounts()
                    for i in accounts:
                        birthday = ""
                        if 'birthday' in i:
                            birthday = i['birthday']
                        gender = ""
                        if 'gender' in i:
                            gender = i['gender']
                        language = ""
                        if 'language' in i:
                            language = i['language']
                        country = ""
                        if 'country' in i:
                            country = i['country']
                        city = ""
                        if 'city' in i:
                            city = i['city']
                        email = ""
                        if 'email' in i:
                            email = i['email']
                        tree_items.append([i['username'], i['fullname'], str(i['mood']), str(birthday), gender, str(language), str(country), str(city), str(email)])
                    items.extend([[0, "Username"], [1, 'Full Name'], [2, 'Mood'], [3, 'Birthday'], [4, "Gender"], [5, "Language"], [6, "Country"], [7, "City"], [8, "Email"]])
            elif name[0] == PROGRAMS_STR:
                progs = pi.get_programs_installed()
                for i in progs:
                    tree_items.append([str(i)])
                items.extend([[0, "Program"]])
            else:
                pass
            if items:
                form = GeneralSubApp(self, items=items, index=index, tree_items=tree_items, name=name)
                self.children_windows.append(form)
                form.show()

    def closeEvent(self, event):
        self.index.setDisabled(False)
        for i in self.children_windows:
            i.close()


class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.dir_path = os.getcwd() + "\logs\\"
        self.actionExit.triggered.connect(self.close)
        self.treeWidget_2.itemDoubleClicked.connect(self.check_index)
        self.actionTutorial.triggered.connect(self.open_help_ui)
        self.lab.setText(HELP_STR)

        if not os.path.exists(os.path.dirname(self.dir_path)):
            os.makedirs(os.path.dirname(self.dir_path))

    def open_help_ui(self):
        form = HelpApp(self, text=1)
        form.show()

    def check_index(self, index):
        if not index.isDisabled():
            name = index.text(0)
            if name == CHROME_STR:
                if ch.is_valid:
                    index.setDisabled(True)
                    tree_items = [[0, PASSWORD_STR], [1, "Cache"], [2, BOOKMARKS_STR], [3, HISTORY_STR], [4, COOKIES_STR]]
                    form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                    form.show()
                else:
                    message_box(self=self, title=name + TITLE_NOT_INSTALLED, txt=name + TXT_NOT_INSTALLED)
            elif name == FIREFOX_STR:
                if fff.is_valid:
                    index.setDisabled(True)
                    tree_items = [[0, PASSWORD_STR], [1, BOOKMARKS_STR], [2, HISTORY_STR], [3, COOKIES_STR]]
                    form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                    form.show()
                else:
                    message_box(self=self, title=name + TITLE_NOT_INSTALLED, txt=name + TXT_NOT_INSTALLED)
            elif name == SKYPE_STR:
                if sky.is_valid:
                    index.setDisabled(True)
                    tree_items = [[0, "Contacts"], [1, "Messages"], [2, "Accounts"]]
                    form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                    form.show()
                else:
                    message_box(self=self, title=name + TITLE_NOT_INSTALLED, txt=name + TXT_NOT_INSTALLED)
            elif name == PROGRAMS_STR:
                index.setDisabled(True)
                tree_items = [[0, "Installed on pc"]]
                form = GeneralApp(self, index=index, tree_items=tree_items, name=name)
                form.show()
            else:
                pass

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
