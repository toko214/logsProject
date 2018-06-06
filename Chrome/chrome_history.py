"""
author: Tomer Perets
date: 5.5.18
this file contains a function to get chrome history data
"""


import os
import usefull_things as ut

def get_chrome_history():
    """
    organizing the chrome history data in a dictonary(key = url id in the database)
    :return: history dictonary
    :return: error number
    """
    data_path = os.path.expanduser('~') + "\AppData\Local\Google\Chrome\User Data\Default"
    history_db = os.path.join(data_path, 'history')
    if not ut.file_exists(history_db):
        return ['err', 2, history_db]
    cursor = ut.connect_to_sqlite3_db(history_db)
    select_statement1 = "SELECT * FROM visits"
    select_statement2 = "SELECT * FROM urls"
    select_statement3 = "SELECT * FROM keyword_search_terms"
    results2 = ut.execute_sql(cursor, select_statement1)
    results3 = ut.execute_sql(cursor, select_statement2)
    results4 = ut.execute_sql(cursor, select_statement3)
    THE_DICT = {}

    if len(results3) > 0:
        for url in results3:
            for visit in results2:
                if url[0] == visit[1]:
                    if url[0] not in THE_DICT:
                        inner_dict = {}
                        inner_dict['url_id'] = url[0]
                        inner_dict['url'] = url[1]
                        inner_dict['visit_time'] = [str(ut.real_time_google(visit[2]))]
                        inner_dict['visit_duration'] = [str(ut.real_time_google(visit[6], True))]
                        THE_DICT[url[0]] = inner_dict
                    else:
                        THE_DICT[url[0]]['visit_time'].append(str(ut.real_time_google(visit[2])))
                        THE_DICT[url[0]]['visit_duration'].append(str(ut.real_time_google(visit[6], True)))
        THE_DICT['google_search'] = results4
        return [THE_DICT]
    return ['err', 1, select_statement2]