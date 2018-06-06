#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Jean-Rémy Bancel <jean-remy.bancel@telecom-paristech.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Chromagon Project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Jean-Rémy Bancel BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
author: Tomer Perets
date: 5.5.18
Frontend script using Chrome Cache parsing library
"""

import chromagnon.cacheParse
import os
import usefull_things as ut
import threading
DIR_PATH = ""
def get_cache_from_i(entry,i):
    if entry.httpHeader.headers.has_key('content-type'):
        ty = entry.httpHeader.headers['content-type']
       # print "content-type: " + ty
        if ';' in ty:
            name = hex(entry.hash) + "_" + str(i) + "." + entry.httpHeader.headers['content-type'][
                                                          ty.find("/") + 1:ty.find(';')]
        else:
            name = hex(entry.hash) + "_" + str(i) + "." + entry.httpHeader.headers['content-type'][
                                                       ty.find("/") + 1:]
        #print entry.creationTime
        domain = ut.get_domain(entry.keyToStr())
        name = DIR_PATH + domain + name
        entry.data[i].save(name)
    else:
        name = hex(entry.hash) + "_" + str(i) + ".txt"
        domain = ut.get_domain(entry.keyToStr())
        name = DIR_PATH + domain + name
        entry.data[i].save(name)

def get_cache_from_entry(entry):
    for i in range(len(entry.data)):
        t = threading.Thread(target=get_cache_from_i,args=(entry,i,))
        t.start()

def get_all_cache():
    """
    parses the cache files and then its organizing the cache files
    each one in a directory by its original site
    :return: error number
    """
    global DIR_PATH
    cache_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default\Cache"
    if not ut.file_exists(cache_path):
        return ['err',6,cache_path]
    dir_path = os.getcwd() + "/saved/Chrome/Cache/"
    if not os.path.exists(os.path.dirname(dir_path)):
        os.makedirs(os.path.dirname(dir_path))
    DIR_PATH = dir_path
    cache = chromagnon.cacheParse.parse(cache_path)
    if len(cache) > 0:
        for entry in cache:
            t = threading.Thread(target=get_cache_from_entry,args=(entry,))
            t.start()
        return None
    return ['err',10, cache_path]

