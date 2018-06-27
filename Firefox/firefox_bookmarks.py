"""
author: Tomer Perets
date: 5.5.18
this file contains a function that get the firefox bookmarks
"""
import os
from datetime import datetime
import usefull_things as ut

def bookmarks():
    """
    :return: bookmarks
    """
    select_statement1 = "SELECT id,fk,parent,dateAdded,lastModified FROM moz_bookmarks"
    select_statement2 = "SELECT id,url,visit_count FROM moz_places"
    firefox_path = os.path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\"
    profiles = [i for i in os.listdir(firefox_path) if i.endswith('.default')]
    BOOKMARKS = []
    errs = ['err']
    for i in profiles:
        sqlite_path = firefox_path + i + '\places.sqlite'
        if not ut.file_exists(sqlite_path):
             errs.append([7, sqlite_path])
        cursor = ut.connect_to_sqlite3_db(sqlite_path)
        results1 = ut.execute_sql(cursor, select_statement1)
        results2 = ut.execute_sql(cursor, select_statement2)
        BOOK_MARKS_DICT = {}
        for row in results1:
            if row[1] > 0:
                inner_dict = {}
                fk = row[1]
                for url in results2:
                    if url[0] == fk:
                        inner_dict['url'] = url[1]
                        inner_dict['id'] = fk
                        date = str(datetime.fromtimestamp(row[3] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                        inner_dict['date_added'] = date
                        date = str(datetime.fromtimestamp(row[4] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                        inner_dict['date_modified'] = date
                        results2.remove(url)
                        BOOK_MARKS_DICT[fk] = inner_dict
                        break
        BOOKMARKS.append(BOOK_MARKS_DICT)
    if len(BOOKMARKS) > 0:
        if len(errs) > 1:
            print "asd"
            return [BOOKMARKS[0],errs]
        return [BOOKMARKS[0]]
    errs.append([1, select_statement1])
    return errs
