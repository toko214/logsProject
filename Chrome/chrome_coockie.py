"""
author: Tomer Perets
date: 5.5.18
this file contains functions that help get chrome cookies
"""
import os
import win32crypt
import usefull_things as ut
import threading


def get_all_cookies():
    """
    this function decrypt all the encrypted cookis out of the cookie file
    :return: list of cookies
    :return: error number
    """
    path = os.path.expanduser('~') + "\AppData\Local\Google\Chrome\User Data\Default\Cookies"
    if not ut.file_exists(path):
        return ['err', 4, path]
    cursor = ut.connect_to_sqlite3_db(path)
    select_statement1 = 'SELECT encrypted_value,host_key,name,expires_utc,creation_utc FROM cookies'
    data = ut.execute_sql(cursor, select_statement1)
    x = 0
    if len(data) > 0:
        cookies = {}
        for result in data:
            try:
                cookie = win32crypt.CryptUnprotectData(result[0], None, None, None, 0)[1]
            except Exception, e:
                continue
            if cookie:
                if len(result[1]) > 0:
                    if result[1][0] == '.':
                        host = result[1][1:]
                    else:
                        host = result[1]
                else:
                    print "jj"
                    host = "no site" + str(x)
                    x += 1
                time = ut.real_time_google(result[3])
                time2 = ut.real_time_google(result[4])
                inner_dict = {"name": result[2], "value": cookie, "expire": str(time), "time_created": str(time2)}
                if host not in cookies:
                    cookies[host] = [inner_dict]
                else:
                    cookies[host].append(inner_dict)
        return [cookies]
    else:
        return ['err', 1, select_statement1]



