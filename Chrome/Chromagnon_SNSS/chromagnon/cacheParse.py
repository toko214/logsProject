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
Parse the Chrome Cache File
See http://www.chromium.org/developers/design-documents/network-stack/disk-cache
for design details
"""

import gzip
import os
import struct
import sys

import csvOutput
import SuperFastHash
from cacheAddress import CacheAddress
from cacheBlock import CacheBlock
from cacheData import CacheData
from cacheEntry import CacheEntry
import threading

usi = []
cache = []

def defi():
    raw = struct.unpack('I', usi[1].read(4))[0]
    if raw != 0:
        entry = CacheEntry(CacheAddress(raw, path=usi[0]))
        # Checking if there is a next item in the bucket because
        # such entries are not stored in the Index File so they will
        # be ignored during iterative lookup in the hash table
        while entry.next != 0:
            cache.append(entry)
            entry = CacheEntry(CacheAddress(entry.next, path=usi[0]))
        cache.append(entry)
def parse(path, urls=None):
    """
    Reads the whole cache and store the collected data in a table
    or find out if the given list of urls is in the cache. If yes it
    return a list of the corresponding entries.
    """
    # Verifying that the path end with / (What happen on windows?)
    path = os.path.abspath(path) + '/'

    cacheBlock = CacheBlock(path + "index")

    # Checking type
    if cacheBlock.type != CacheBlock.INDEX:
        raise Exception("Invalid Index File")

    index = open(path + "index", 'rb')
    usi.append(path)
    usi.append(index)
    usi.append(cacheBlock)
    # Skipping Header
    index.seek(92*4)

    # If no url is specified, parse the whole cache
    if urls == None:
        for key in range(cacheBlock.tableSize):
            t = threading.Thread(target=defi)
            t.start()
    else:
        # Find the entry for each url
        for url in urls:
            # Compute the key and seeking to it
            hash = SuperFastHash.superFastHash(url)
            key = hash & (cacheBlock.tableSize - 1)
            index.seek(92*4 + key*4)

            addr = struct.unpack('I', index.read(4))[0]
            # Checking if the address is initialized (i.e. used)
            if addr & 0x80000000 == 0:
                print >> sys.stderr, \
                      "\033[32m%s\033[31m is not in the cache\033[0m" % url

            # Follow the chained list in the bucket
            else:
                entry = CacheEntry(CacheAddress(addr, path=path))
                while entry.hash != hash and entry.next != 0:
                    entry = CacheEntry(CacheAddress(entry.next, path=path))
                if entry.hash == hash:
                    cache.append(entry)
    return cache

