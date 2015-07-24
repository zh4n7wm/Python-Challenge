#!/usr/bin/env python
# encoding: utf-8

from mylib import get_comment_from_src
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
comment = get_comment_from_src(url)[0]
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', comment))
