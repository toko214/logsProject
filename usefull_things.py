import sqlite3
import os
import datetime
from urlparse import urlparse

def connect_to_sqlite3_db(sqlite3_path):
    return sqlite3.connect(sqlite3_path).cursor()

def execute_sql(cursor,select_statement):
    return cursor.execute(select_statement).fetchall()

def file_exists(path):
    return os.path.exists(path)

def real_time_google(google_time,duration=False):
    try:
        start_time = datetime.datetime(1601,1,1)
        delta = datetime.timedelta(microseconds=int(google_time))
        if duration:
            return delta
        return start_time + delta + datetime.timedelta(microseconds=3600000000*3)
    except Exception:
        return 5

def get_domain(url):
    """
    this function gets the domain out of a url
    :param url: the url
    :return: domain out of the url
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    indx = domain.find('/')
    domain = domain[indx + 2:]
    if not os.path.isdir(domain):
        os.makedirs(domain)
    return domain