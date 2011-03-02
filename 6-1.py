#!/usr/bin/env python
# -*- coding: utf-8 -*-

fname = '94191'
while True:
    f = open(fname + '.txt', 'r')
    line = f.read().replace('\n', '')
    print line
    if line.find('Next nothing is') != -1:
        fname = line.split()[-1]
    else:
        break
