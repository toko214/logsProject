"""
Author: Tomer Perets
Date: 27.6.18
this file contains a functions that help get the firefox history
"""


import os
from datetime import datetime
import usefull_things as ut


def get_history(firefox_path):
    """
    This function extracting all the history out of the history database file.
    Its accessing the firefox history file database and uses an sql query to get the data.
    If error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param firefox_path: the firefox profiles path
    :return: list of bookmarks - [{'id':{'url':str,'visit_dates': list of str]....]
    :return: error number - ['err', [error_number, error_info]...]
    """
    select_statement1 = "SELECT id,url,last_visit_date FROM moz_places order by id"
    select_statement2 = "SELECT place_id, visit_date FROM moz_historyvisits order by place_id"
    profiles = [i for i in os.listdir(firefox_path) if i.endswith('.default')]
    history = []
    errs = ['err']
    for i in profiles:
        sqlite_path = firefox_path + i + '\places.sqlite'
        if not ut.file_exists(sqlite_path):
            errs.append([8, sqlite_path])
        cursor = ut.connect_to_sqlite3_db(sqlite_path)
        results1 = ut.execute_sql(cursor, select_statement1)
        results2 = ut.execute_sql(cursor, select_statement2)
        if len(results1) > 0:
            history_dict = {}
            for row in results1:  # Url data
                if row[2] > 0:
                    inner_dict = {}
                    to_remove = []
                    for visit in results2:  # Each url visit data
                        if visit[0] == row[0]:
                            if 'url' in inner_dict:  # Checking if the url is already in dictionary
                                date = str(datetime.fromtimestamp(visit[1] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                                inner_dict['visit_dates'].append(date)
                                to_remove.append(visit)
                            else:  # Adding the visit times if the url is already in the dictionary
                                inner_dict['url'] = row[1]
                                date = str(datetime.fromtimestamp(visit[1] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                                inner_dict['visit_dates'] = [date]
                                to_remove.append(visit)
                        else:
                            break
                    history_dict[row[0]] = inner_dict
                    for r in to_remove:  # To reduce runtime
                        results2.remove(r)
            history.append(history_dict)
    if len(history) > 0:
        if len(errs) > 1:
            return [history[0], errs]
        return [history[0]]
    errs.append([1, select_statement1])
    return errs
