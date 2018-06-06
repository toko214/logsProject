import ffcache
import os

# Hard-wired location of some cache directory  (Will depend on your machine)
cachedir = r"C:\Users\tomer\AppData\Local\Mozilla\Firefox\Profiles\6h5734qn.default\Cache"

f = open(os.path.join(cachedir,"_CACHE_001_"),"rb")
f.seek(4096)
headerdata = f.read(36)
meta = ffcache.parse_meta_header(headerdata)
print meta
requestdata = f.read(meta['requestsize']+meta['infosize'])
ffcache.parse_request_data(meta,requestdata)
print meta

print meta['request']
print meta['info']
ffcache.add_content_info(meta)
print meta['content-type']
print meta['content-encoding']
print meta['charset']

f = open(os.path.join(cachedir,"_CACHE_001_"),"rb")
for meta in ffcache.scan_cachefile(f,256):
    print meta['request']
for meta in ffcache.scan_cache(cachedir):
    print meta['request']
# Find all requests related to slashdot
for meta in ffcache.scan_cache(cachedir):
    if 'slashdot' in meta['request']:
        print meta['request']


# Find all large JPEG images
jpegs = (meta for meta in ffcache.scan_cache(cachedir)
              if meta['content-type'] == 'image/jpeg'
              and meta['datasize'] > 100000)

for j in jpegs:
    print j['request']