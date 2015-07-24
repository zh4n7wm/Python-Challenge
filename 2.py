#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string
from mylib import get_comment_from_src

url = r'http://www.pythonchallenge.com/pc/def/ocr.html'
s = get_comment_from_src(url)
if len(s) != 2:
    print 'web page source code changed??'
    sys.exit()

t = [x for x in s[1] if x in string.letters]

print ''.join(t)
