#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string
import requests
import re

url = r'http://www.pythonchallenge.com/pc/def/ocr.html'
data = requests.get(url).content
s = re.findall('<!--([^>]+)-->', data)
if len(s) != 2:
    print 'web page source code changed??'
    sys.exit()

t = [x for x in s[1] if x in string.letters]

print ''.join(t)
