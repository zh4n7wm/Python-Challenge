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
res = []
for h in range(img.size[1]):
    for w in range(img.size[0]):
        if h == 43 and w % 7 == 0:
            res.append(img.getpixel((w,h))[0])
img.close()

res = [chr(x) for x in res]
msg= ''.join(res)
print msg

start, end = (msg.find('['), msg.find(']'))
nmsg = msg[start+1:end].split(',')
print ''.join([chr(int(x)) for x in nmsg])
