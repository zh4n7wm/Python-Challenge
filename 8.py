#!/usr/bin/env python
# encoding: utf-8
"""
level 8: http://www.pythonchallenge.com/pc/def/integrity.html
"""

from __future__ import print_function
from mylib import get_comment_from_src
import re
import bz2

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
comment = get_comment_from_src(url)[0]
un = re.findall("un: '([^']+)'", comment)[0]
pw = re.findall("pw: '([^']+)'", comment)[0]
#print(un)
#print(pw)

print('username:', bz2.decompress(un.decode('string_escape')))
print('password:', bz2.decompress(pw.decode('string_escape')))
