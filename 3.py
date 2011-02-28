#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = file('3', 'r').read()
length = len(s)

for pos in range(length-5):
    for x in range(pos, length-5):
        if s[x:x+3] == s[x+4:x+4+3] and s[x+3].islower():
            print s[x:x+3]
            print s[x:x+4+3]
            print s[x+3]
            print s[x:7]
