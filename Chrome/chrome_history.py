"""
author: Tomer Perets
date: 27.6.18
this file contains a function to get chrome history data
"""


import os
import usefull_things as ut


def get_chrome_history(chrome_path):
    """
    organizing the chrome history data in a dictonary(key = url id in the database)
    its accessing the chrome history file database and uses an sql query to get the data.
    if error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param chrome_path: the chrome databases path
    :return: history dictionary - [{url_id:{'url':str,'visit_time':list, 'visit_duration':list}....},google_searches]
    :return: error number - ['err', error_number, error_info]
    """
    history_db = os.path.join(chrome_path, 'history')
    if not ut.file_exists(history_db):  # Checking if the database file exists
        return ['err', 2, history_db]
    cursor = ut.connect_to_sqlite3_db(history_db)
    select_statement1 = "SELECT * FROM visits"
    select_statement2 = "SELECT * FROM urls"
    select_statement3 = "SELECT * FROM keyword_search_terms"
    results2 = ut.execute_sql(cursor, select_statement1)
    results3 = ut.execute_sql(cursor, select_statement2)
    results4 = ut.execute_sql(cursor, select_statement3)
    the_dict = {}
    if len(results3) > 0:
        for url in results3:  # Url data
            to_remove = []
            for visit in results2:  # Each url visit data
                if url[0] == visit[1]:
                    if url[0] not in the_dict:  # Checking if the url is already in dictionary
                        inner_dict = {}
                        inner_dict['url'] = url[1]
                        inner_dict['visit_time'] = [str(ut.real_time_google(visit[2]))]
                        inner_dict['visit_duration'] = [str(ut.real_time_google(visit[6], True))]
                        the_dict[url[0]] = inner_dict
                        to_remove.append(visit)
                    else:  # Adding the visit times and durations if the url is already in the dictionary
                        the_dict[url[0]]['visit_time'].append(str(ut.real_time_google(visit[2])))
                        the_dict[url[0]]['visit_duration'].append(str(ut.real_time_google(visit[6], True)))
                        to_remove.append(visit)
            for r in to_remove:  # To reduce runtime
                results2.remove(r)
        searches = {}
        for search in results4:  # Adding the google searches
            if search[1] in the_dict:  # Chrome saving the history for 90 days but the searches fo longer
                url = the_dict[search[1]]
                searches[search[2]] = url
            else:  # Occurs if the search is older than 90 days
                searches[search[2]] = ""
        return [the_dict, searches]
    return ['err', 1, select_statement2]
