#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

s = sys.argv[1]
r = ''

for x in s:
    r = r + chr(ord(x)+2)

print r
