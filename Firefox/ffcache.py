# ffcache.py
#
# Functions for extracting meta-data from the Firefox browser cache

# -------------------------------------------------------------------
# Part 1

import struct

# This function parses a cache metadata header into a dict
# of named fields (listed in _headernames below)

_headernames = ['magic', 'location', 'fetchcount',
                'fetchtime', 'modifytime', 'expiretime',
                'datasize', 'requestsize', 'infosize']


def parse_meta_header(headerdata):
    head = struct.unpack(">9I", headerdata)
    meta = dict(zip(_headernames, head))
    return meta


# -------------------------------------------------------------------
# Part 2

import re

part_pat = re.compile(r'[\n\r -~]*$')


def parse_request_data(meta, requestdata):
    parts = requestdata.split('\x00')
    for part in parts:
        if not part_pat.match(part):
            return False

    request = parts[0]
    if len(request) != (meta['requestsize'] - 1):
        return False

    info = dict(zip(parts[1::2], parts[2::2]))
    meta['request'] = request.split(':', 1)[1]
    meta['info'] = info
    return True


# -------------------------------------------------------------------
# Part 3

# Given a metadata dictionary, this function adds additional
# fields related to the content type, charset, and encoding

import email


def add_content_info(meta):
    info = meta['info']
    if 'response-head' not in info:
        meta['content-type'] = 'unknown'
        meta['content-encoding'] = None
        meta['charset'] = ''
    else:
        rhead = info.get('response-head').split("\n", 1)[1]
        m = email.message_from_string(rhead)
        content = m.get_content_type()
        encoding = m.get('content-encoding', None)
        charset = m.get_content_charset()
        meta['content-type'] = content
        meta['content-encoding'] = encoding
        meta['charset'] = charset


# -------------------------------------------------------------------
# Part 4

# Scan a single file in the firefox cache
def scan_cachefile(f, blocksize):
    maxsize = 4 * blocksize  # Maximum size of an entry
    f.seek(4096)  # Skip the bit-map
    while True:
        headerdata = f.read(36)
        if not headerdata: break
        meta = parse_meta_header(headerdata)
        if (meta['magic'] == 0x00010008 and
                meta['requestsize'] + meta['infosize'] < maxsize):
            requestdata = f.read(meta['requestsize'] +
                                 meta['infosize'])
            if parse_request_data(meta, requestdata):
                add_content_info(meta)
                yield meta

        # Move the file pointer to the start of the next block
        fp = f.tell()
        if (fp % blocksize):
            f.seek(blocksize - (fp % blocksize), 1)


# -------------------------------------------------------------------
# Part 5

# Given the name of a Firefox cache directory, the function
# scans all of the _CACHE_00n_ files for metadata. A sequence
# of dictionaries containing metadata is returned.

import os


def scan_cache(cachedir):
    files = [('_CACHE_001_', 256),
             ('_CACHE_002_', 1024),
             ('_CACHE_003_', 4096)]

    for cname, blocksize in files:
        cfile = open(os.path.join(cachedir, cname), "rb")
        for meta in scan_cachefile(cfile, blocksize):
            meta['cachedir'] = cachedir
            meta['cachefile'] = cname
            yield meta
        cfile.close()


# -------------------------------------------------------------------
# Part 6

# scan an entire list of cache directories producing
# a sequence of records

def scan(cachedirs):
    if isinstance(cachedirs, str):
        cachedirs = [cachedirs]
    for cdir in cachedirs:
        for meta in scan_cache(cdir):
            yield meta