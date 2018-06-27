"""
Author: Tomer Perets
Date: 27.6.18
This file contains a class that responsible for extracting the data from google chrome.
The class contains functions that calls other functions to receive the requested data.
"""
import chrome_bookmarks
import chrome_coockie
import chrome_password
import chrome_history
import os
import usefull_things as ut
import erros as err


class ChromeEngine:
    def __init__(self):
        """
        This is the init function that comes up when the object is created.
        Its defining if its possible to to extract data from chrome.
        """
        self.name = "chrome"
        self.chrome_path = os.path.expanduser('~') + "\AppData\Local\Google\Chrome\User Data\Default"
        if not ut.file_exists(self.chrome_path):
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.info_bank = {}

    def get_chrome_saved_password(self):
        """
        Calling a function to receive the google chrome passwords.
        Writing to a file if error occurs.
        :return: List of google chrome passwords.
        """
        info = chrome_password.get_chrome_saved_password(self.chrome_path)
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['passwords'] = info
            return info

    def get_chrome_history(self):
        """
        Calling a function to receive the google chrome history and google search.
        Writing to a file if error occurs.
        :return: List of google chrome history and google search.
        """
        info = chrome_history.get_chrome_history(self.chrome_path)
        if info[0] == 'err':
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['history'] = info
            return info

    def get_chrome_bookmarks(self):
        """
        Calling a function to receive the google chrome bookmarks.
        Writing to a file if error occurs.
        :return: List of google chrome bookmarks.
        """
        info = chrome_bookmarks.get_bookmarks(self.chrome_path)
        if info[0] == 'err':  # The function returns an array of data or errors if error occurs
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['bookmarks'] = info

    def get_cookies(self):
        """
        Calling a function to receive the google chrome cookies.
        Writing to a file if error occurs.
        :return: List of google chrome cookies.
        """
        info = chrome_coockie.get_all_cookies(self.chrome_path)
        if info[0] == 'err':  # The function returns an array of data or errors if error occurs
            err.error_handle([info[1:]], self.name)
        else:
            self.info_bank['cookies'] = info
            return info[0]

    # def get_all_cache_files(self):
    #     info = cache.get_all_cache()
    #     if info != None:
    #         f = open('/logs/chrome_erros.txt', 'a')
    #         f.write("-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[info[1]] + " - " + info[2])
    #         f.close()
    #
    # def get_last_tabs(self):
    #     return lt.get_last_tabs()
    #
    # def get_session_info(self):
    #     return ses.get_last_session_info()
