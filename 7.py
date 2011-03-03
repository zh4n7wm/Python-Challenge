#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
from PIL import Image

png_fname = 'oxygen.png'
png_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
if not os.path.exists(png_fname):
    fout = open(png_fname, 'w')
    fout.write(urllib2.urlopen(png_url).read())
    fout.close()

img = Image.open(png_fname, 'r')
res = []
for h in range(img.size[1]):
    for w in range(img.size[0]):
        if h == 43 and (w+1) % 7 == 0:
            res.append(img.getpixel((w,h))[0])

res = [chr(x) for x in res]
print ''.join(res)
