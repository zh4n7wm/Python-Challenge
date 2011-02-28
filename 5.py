#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import urllib

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.load(urllib.urlopen(url))
r = ''

for line in data:
    for x in line:
        r += x[0] * int(x[1])
    r += '\n'

print r
