"""
author: Tomer Perets
date: 5.5.18
this file contains functions that get chrome bookmarks data
"""

import io
from json import loads
from re import match
import os
import usefull_things as ut

script_version = "2.0.1"
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&#39;",
    ">": "&gt;",
    "<": "&lt;",
}

BOOKMARKS = []
def html_escape(text):
    return ''.join(html_escape_table.get(c, c) for c in text)

def sanitize(string):
    res = ''
    string = html_escape(string)

    for i in range(len(string)):
        if ord(string[i]) > 127:
            res += '&#x{:x};'.format(ord(string[i]))
        else:

            res += string[i]
    return res

def html_for_node(node):
    if 'url' in node:
        return html_for_url_node(node)
    elif 'children' in node:
        return html_for_parent_node(node)
    else:
        return ''

def html_for_url_node(node):
    if not match("javascript:", node['url']):
        return sanitize(node['url'])
    else:
        return ''

def html_for_parent_node(node):
     BOOKMARKS.extend(html_for_node(n) for n in node['children'])

def get_bookmarks():
    """
    this function read all the bookmarks from the bookmark file
    :return: bookmarks
    :return: error number
    """
    path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default\\Bookmarks"
    if not ut.file_exists(path):
        return ['err',3,path]
    input_file = io.open(path, 'r', encoding='utf-8')
    contents = loads(input_file.read())
    html_for_node(contents['roots']['bookmark_bar'])
    html_for_node(contents['roots']['other'])
    return BOOKMARKS



