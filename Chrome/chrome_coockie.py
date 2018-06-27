"""
author: Tomer Perets
date: 27.6.18
this file contains functions that help get chrome cookies
"""
import os
import win32crypt
import usefull_things as ut

SELECT_STATEMENT1 = 'SELECT encrypted_value,host_key,name,expires_utc,creation_utc FROM cookies'


def get_all_cookies(chrome_path):
    """
    this function decrypt all the encrypted cookis out of the cookie file.
    its accessing the chrome bookmarks file database and uses an sql query to get the data.
    if error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param chrome_path: the chrome databases path
    :return: list of cookies - [{'host':{'name':str,'value':str,'expire':str,'time_created':str}]....]
    :return: error number - ['err', error_number, error_info]
    """
    data_path = os.path.join(chrome_path, 'Cookies')
    if not ut.file_exists(data_path):  # checking if the database file exists
        return ['err', 4, data_path]
    cursor = ut.connect_to_sqlite3_db(data_path)
    data = ut.execute_sql(cursor, SELECT_STATEMENT1)
    x = 0
    if len(data) > 0:
        cookies = {}
        for result in data:
            try:
                cookie = win32crypt.CryptUnprotectData(result[0], None, None, None, 0)[1]  # Decrypts the cookie
            except Exception, e:
                continue
            if cookie:
                if len(result[1]) > 0:
                    if result[1][0] == '.':
                        host = result[1][1:]
                    else:
                        host = result[1]
                else:
                    host = "no site" + str(x)
                    x += 1
                time = ut.real_time_google(result[3])
                time2 = ut.real_time_google(result[4])
                inner_dict = {"name": result[2], "value": cookie, "expire": str(time), "time_created": str(time2)}
                if host not in cookies:  # Its possible that a site have a multiply cookies
                    cookies[host] = [inner_dict]
                else:
                    cookies[host].append(inner_dict)
        return [cookies]
    else:
        return ['err', 1, SELECT_STATEMENT1]
