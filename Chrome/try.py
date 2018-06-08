#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Chrome Bookmark Exporter, tested with OS X Chrome 7.0.517.41
# Jan Eden <software (a) janeden net>
# based on a Groovy script by Dan Fraser [http://www.capybara.org/~dfraser/archives/355]
# This file is public domain. Python 2.6 or newer required
 
import json
import datetime
import cgi
import os
import sys
import codecs
from datetime import datetime
import datetime
import time
import getpass
 
hostname = 'xyz'
username = 'abc'
password = '****'
database = 'database_name'
 
 
user = getpass.getuser()
 
 
def doQuery( conn, name, url, ct ) :
	cur = conn.cursor()
	ct = int(ct)
	cur.execute( "INSERT INTO personal_abstracthuman (id,user_id,slug,profile_pic) VALUES(ct, 2, name, null)" );
	cur.execute( "INSERT INTO personal_importantlinks (abstracthuman_ptr_id,title,description,related_language,link) VALUES(ct, name, name,null,link)" )
	conn.commit()
 
input_filename = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default\\Bookmarks"
#input_filename = "/Users/%s/Library/Application Support/Google/Chrome/Default/Bookmarks" % user
# modify if necessary
output_filename = "chrome-bookmarks.html"
 
input_file = codecs.open(input_filename, encoding='utf-8')
bookmark_data = json.load(input_file)
output_file = codecs.open(output_filename, 'w', encoding='utf-8')
print bookmark_data
def print_bookmarks(bookmarks):
	for entry in bookmarks:
		if entry['type'] == 'folder':
			if not len(entry['children']) == 0:
				output_file.write(u'<DT><H3 FOLDED ADD_DATE="{0}">{1}</H3>'.format(entry['date_added'], entry['name']))
				next_folder = entry['children']
				output_file.write(u'<DL><p>')
				print_bookmarks(next_folder)
				output_file.write(u'</DL><p>')
		else:
			output_file.write(u'<DT><A DATE_ADDED="{0}" HREF="{1}">{2}</A>'.format(entry['date_added'], cgi.escape(entry['url']), entry['name']))
 
 
output_file.write(u'<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<Title>Bookmarks</Title>\n<H1>Bookmarks</H1><DL>\n')
 
roots = bookmark_data['roots']
 
#print roots
s = 1
for entry in roots:
	try:
		print s
		#print len(roots[entry]['children'])
		ct = 283
		#ids = 4		
		for i in roots[entry]['children']:
			#print int(i['date_added'])
			s, ms = divmod(int(i['date_added']), 1000)
			date_created = '%s.%03d' % (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), ms)			
			print i['name']
			print i['url']
			#print i['url']
			output_file.write(u'<DT><H3 FOLDED><a href="{1}" >{0} on date <strong style="color:red;">{2}</strong></a></H3>'.format(i['name'], i['url'], date_created))
			output_file.write(u'</DL><p>')
			#myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
			#doQuery( myConnection, i['name'], i['url'], ct, ids )
			#myConnection.close()
			ct = ct+1
			#ids = ids+1
 
		s = s+1
		#print roots[entry]['date_added']
		#output_file.write(u'<DT><H3 FOLDED ADD_DATE={0}>{1}</H3>'.format(roots[entry]['date_added'], entry))
		#print_bookmarks(roots[entry]['children'])
		#output_file.write(u'</DL><p>')
	except:
		pass
 
output_file.write(u'</DL>')