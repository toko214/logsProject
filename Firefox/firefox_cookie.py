"""
Author: Tomer Perets
Date: 27.6.18
this file contains a function that get the firefox cookies
"""

import os
from datetime import datetime
import usefull_things as ut


def get_all_cookies(firefox_path):
    """
    This function extracting all the cookies out of the cookies database file.
    Its accessing the firefox cookies file database and uses an sql query to get the data.
    If error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param firefox_path: the firefox profiles path
    :return: list of bookmarks:[{'host':{'name':str,'value':str,'creationTime':str,'expiry':str]-some cookies for host}]
    :return: error number - ['err', [error_number, error_info]...]
    """
    select_statement1 = "SELECT baseDomain, name, value, expiry,creationTime FROM moz_cookies"
    profiles = [i for i in os.listdir(firefox_path) if i.endswith('.default')]
    cookies = []
    errs = ['err']
    for i in profiles:
        sqlite_path = firefox_path + i + '\cookies.sqlite'
        if not ut.file_exists(sqlite_path):
            errs.append([9, sqlite_path])
        cursor = ut.connect_to_sqlite3_db(sqlite_path)
        results1 = ut.execute_sql(cursor, select_statement1)
        cookies_dict = {}
        if len(results1) > 0:
            for cookie in results1:
                creation = str(datetime.fromtimestamp(cookie[4] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                expiry = str(datetime.fromtimestamp(cookie[3] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                inner_dict = {"name": cookie[1], 'value': cookie[2], 'creationTime': creation, 'expiry': expiry}
                if not cookie[0] in cookies_dict:
                    cookies_dict[cookie[0]] = [inner_dict]
                else:
                    cookies_dict[cookie[0]].append(inner_dict)
            cookies.append(cookies_dict)
    if len(cookies) > 0:
        if len(errs) > 1:
            return [cookies[0], errs]
        return [cookies[0]]
    errs.append([1, select_statement1])
    return errs
