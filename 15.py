from calendar import isleap
import calendar

for year in xrange(1006, 2000, 10):
    if isleap(year) and calendar.weekday(year, 1, 27) == 1:
        print year
