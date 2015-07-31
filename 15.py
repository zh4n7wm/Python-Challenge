#!/usr/bin/env python
# encoding: utf-8
"""
level 15: http://www.pythonchallenge.com/pc/return/uzi.html
"""

from datetime import datetime

for x in xrange(100):
    year = int('1%02d6' % x)
    dt26 = datetime(year, 1, 26)
    dt1 = datetime(year, 1, 1)
    if dt1.isoweekday() == 4 and dt26.isoweekday() == 1:
        print year

