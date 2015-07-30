#!/usr/bin/env python
# encoding: utf-8
"""
level 12: http://www.pythonchallenge.com/pc/return/evil.html
evil1.jpg, evil2.jpg, evil2.gfx, ...
"""

import requests
from mylib import USER, PASSWORD

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
gfx = requests.get(url, auth=(USER, PASSWORD)).content
for i in xrange(5):
    f = open('%d.jpg' % i, 'wb')
    f.write(gfx[i::5])
    f.close()
