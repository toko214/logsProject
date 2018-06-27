"""
Author: Tomer Perets
Date: 27.6.18
This file contains a function that get the firefox bookmarks
"""

import os
from datetime import datetime
import usefull_things as ut


def get_bookmarks(firefox_path):
    """
    This function extracting all the bookmarks out of the bookmarks database file.
    Its accessing the firefox bookmarks file database and uses an sql query to get the data.
    If error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param firefox_path: the firefox profiles path
    :return: list of bookmarks - [{'id':{'url':str,'date_added':str,'date_modified':str]....]
    :return: error number - ['err', [error_number, error_info]...]
    """
    select_statement1 = "SELECT id,fk,parent,dateAdded,lastModified FROM moz_bookmarks"
    select_statement2 = "SELECT id,url,visit_count FROM moz_places"
    profiles = [i for i in os.listdir(firefox_path) if i.endswith('.default')]
    bookmarks = []
    errs = ['err']
    for i in profiles:
        sqlite_path = firefox_path + i + '\places.sqlite'
        if not ut.file_exists(sqlite_path):
            errs.append([7, sqlite_path])
        cursor = ut.connect_to_sqlite3_db(sqlite_path)
        results1 = ut.execute_sql(cursor, select_statement1)
        results2 = ut.execute_sql(cursor, select_statement2)
        book_marks_dict = {}
        for row in results1:
            if row[1] > 0:
                inner_dict = {}
                fk = row[1]
                for url in results2:  # Searching for the url data from the history.
                    if url[0] == fk:
                        inner_dict['url'] = url[1]
                        date = str(datetime.fromtimestamp(row[3] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                        inner_dict['date_added'] = date
                        date = str(datetime.fromtimestamp(row[4] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                        inner_dict['date_modified'] = date
                        results2.remove(url)
                        book_marks_dict[fk] = inner_dict
                        break
        bookmarks.append(book_marks_dict)
    if len(bookmarks) > 0:
        if len(errs) > 1:
            return [bookmarks[0], errs]
        return [bookmarks[0]]
    errs.append([1, select_statement1])
    return errs
