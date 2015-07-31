#!/usr/bin/env python
# encoding: utf-8
"""
level15: http://www.pythonchallenge.com/pc/return/uzi.html
TODO:
1.Python datetime, calendar 和Linux date, cal 输出结果不一致.
如:

In [40]: import calendar
In [41]: c = calendar.TextCalendar(calendar.SUNDAY)
In [42]: c.prmonth(1036, 1)
    January 1036
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

In [43]: !cal 1 1036
    January 1036
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""

from calendar import isleap
import calendar

for year in xrange(1006, 2000, 10):
    if isleap(year) and calendar.weekday(year, 1, 27) == 1:
        print year
