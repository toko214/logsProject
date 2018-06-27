"""
Author: Tomer Perets
Date: 27.6.18
This file contains a class that responsible for extracting the data from firefox.
The class contains functions that calls other functions to receive the requested data.
"""
import firefoxHistory
import firefox_bookmarks
import firepwd
import firefox_cookie
import os
import usefull_things as ut
import erros as err


class FireFoxEngine:
    def __init__(self):
        """
        This is the init function that comes up when the object is created.
        Its defining if its possible to to extract data from firefox.
        """
        self.name = "firefox"
        self.firefox_path = os.path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\"
        if not ut.file_exists(self.firefox_path):
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.info_bank = {}

    def get_bookmarks(self):
        """
        Calling a function to receive the firefox bookmarks.
        Writing to a file if error occurs.
        :return: List of firefox bookmarks.
        """
        info = firefox_bookmarks.bookmarks(self.firefox_path)
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['bookmarks'] = info[0]
            return info[0]

    def get_history(self):
        """
        Calling a function to receive the firefox history.
        Writing to a file if error occurs.
        :return: List of firefox history.
        """
        info = firefoxHistory.get_history(self.firefox_path)
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['history'] = info[0]
            return info[0]

    def get_saved_password(self):
        """
        Calling a function to receive the firefox passwords.
        Writing to a file if error occurs.
        :return: List of firefox passwords.
        """
        info = firepwd.get_saved_password(self.firefox_path)
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['passwords'] = info
            return info

    def get_cookies(self):
        """
        Calling a function to receive the firefox cookies.
        Writing to a file if error occurs.
        :return: List of firefox cookies.
        """
        info = firefox_cookie.get_all_cookies(self.firefox_path)
        if info[0] == 'err':
            err.error_handle(info[1:], self.name)
        else:
            self.info_bank['cookies'] = info[0]
            return info[0]
