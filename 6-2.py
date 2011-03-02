#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import zipfile
import os

zip_fname = 'channel.zip'
if not os.path.exists(zip_fname):
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    data = urllib2.urlopen(url).read()
    fout = open(zip_fname, 'w')
    fout.write(data)
    fout.close()

fname = '90052'
zfile = zipfile.ZipFile(zip_fname, 'r')
zip_comments = []

while True:
    zip_comments.append(zfile.getinfo('%s.txt' % fname).comment)
    data = zfile.read('%s.txt' % fname)
    if data.find('Next nothing is') != -1:
        fname = data.split()[-1]
    else:
        break

print ''.join(zip_comments)
