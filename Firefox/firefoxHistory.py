'''
author: Tomer Perets
date: 5.5.18
this file contains a functions that help get the firefox history
'''


import os
from datetime import datetime
import usefull_things as ut

def history():
    """
    :return: firefox history
    """
    select_statement1 = "SELECT id,url,last_visit_date FROM moz_places order by id"
    select_statement2 = "SELECT place_id, visit_date FROM moz_historyvisits order by place_id"
    firefox_path = os.path.expanduser('~') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\"
    profiles = [i for i in os.listdir(firefox_path) if i.endswith('.default')]
    HISTORY = []
    errs = ['err']
    for i in profiles:
        sqlite_path = firefox_path + i + '\places.sqlite'
        if not ut.file_exists(sqlite_path):
            errs.append([8, sqlite_path])
        cursor = ut.connect_to_sqlite3_db(sqlite_path)
        results1 = ut.execute_sql(cursor, select_statement1)
        results2 = ut.execute_sql(cursor, select_statement2)
        if len(results1) > 0:
            HISTORY_DICT = {}
            for row in results1:
                if row[2] > 0:
                    inner_dict = {}
                    to_remove = []
                    for visit in results2:
                        if visit[0] == row[0]:
                            if 'id' in inner_dict:
                                date = str(datetime.fromtimestamp(visit[1] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                                inner_dict['visit_dates'].append(date)
                                to_remove.append(visit)
                            else:
                                inner_dict['url'] = row[1]
                                inner_dict['id'] = row[0]
                                date = str(datetime.fromtimestamp(visit[1] / 1000000).strftime('%Y-%m-%d %H:%M:%S'))
                                inner_dict['visit_dates'] = [date]
                                to_remove.append(visit)
                        else:
                            break
                    HISTORY_DICT[row[0]] = inner_dict
                    for r in to_remove:
                        results2.remove(r)
            HISTORY.append(HISTORY_DICT)
    if len(HISTORY) > 0:
        if len(errs) > 1:
            return [HISTORY[0], errs]
        return [HISTORY[0]]
    errs.append([1, select_statement1])
    return errs