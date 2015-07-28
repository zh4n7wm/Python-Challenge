#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from StringIO import StringIO
from PIL import Image

png_fname = 'oxygen.png'
png_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
print 'downloading %s, please wait ...' % png_fname
fimg = StringIO(urllib2.urlopen(png_url).read())

img = Image.open(fimg)
w = img.size[0] # width
h = img.size[1] # heigh
m = h/2         # middle
res = []
for i in range(0, w, 7):
    p = img.getpixel((i, m))  # note: m in m-4 ~ m+4 is OK
    if p[0] == p[1] == p[2]:  # also can img.convert("L") first
        res.append(p[0])
img.close()

res = [chr(x) for x in res]
msg= ''.join(res)
print msg

start, end = (msg.find('['), msg.find(']'))
nmsg = msg[start+1:end].split(',')
print ''.join([chr(int(x)) for x in nmsg])
