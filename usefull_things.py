import sqlite3
import os
import datetime
from urlparse import urlparse
from PyQt4 import QtGui

TITLE_NOT_INSTALLED = " Not Installed"
TXT_NOT_INSTALLED = " Is Not Installed Or His Files Is Corrupted"
CHROME_STR = "Chrome"
FIREFOX_STR = "Firefox"
SKYPE_STR = "Skype"
PROGRAMS_STR = "Programs"
PASSWORD_STR = "Password"
BOOKMARKS_STR = "Bookmarks"
HISTORY_STR = "History"
COOKIES_STR = "Cookies"
HELP_STR = "You can always use help window to know more on the program. | Its may take some time...."
NO_ITEMS_FOUND_TITLE = "No Items Found"
NO_ITEMS_FOUND_TXT = "No Items Found With this keyword"
NO_MORE_ITEMS_TITLE = "No More Items"
NO_MORE_ITEMS_TXT = "No More Items Found"
ITEMS_COUNT_STR = "Items Count: "
SHOURCUT_CTRL_A = 'Ctrl+A'
SHOURCUT_CTRL_S = 'Ctrl+S'
SHOURCUT_CTRL_F = 'Ctrl+F'
SHOURCUT_CTRL_D = 'Ctrl+D'
USERNAME_STR = "Username"
WEBSITE_STR = "Website"
URL_STR = "url"
URL_STR2 = "Url"


def connect_to_sqlite3_db(sqlite3_path):
    return sqlite3.connect(sqlite3_path).cursor()


def execute_sql(cursor,select_statement):
    return cursor.execute(select_statement).fetchall()


def file_exists(path):
    return os.path.exists(path)


def real_time_google(google_time,duration=False):
    try:
        start_time = datetime.datetime(1601,1,1)
        delta = datetime.timedelta(microseconds=int(google_time))
        if duration:
            return delta
        return start_time + delta + datetime.timedelta(microseconds=3600000000*3)
    except Exception:
        return 5


def get_domain(url):
    """
    this function gets the domain out of a url
    :param url: the url
    :return: domain out of the url
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    indx = domain.find('/')
    domain = domain[indx + 2:]
    if not os.path.isdir(domain):
        os.makedirs(domain)
    return domain

def message_box(self=None, title="", txt="", icon=""):
    msg = QtGui.QMessageBox(self)
    msg.setIcon(QtGui.QMessageBox.Critical)
    msg.setText(txt)
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle(title)
    # msg.setDetailedText("The details are as follows:")
    msg.show()