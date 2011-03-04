#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ox0spy <Ox0spy@gmail.com>
# http://www.pythonchallenge.com/pc/return/bull.html

import re

a = ['1', '11', '21', '1211', '111221',]
def seq_func(n):
    s = '1'
    res = [1]
    while n > 1:
        q = ''
        i = 0
        l = len(s)
        while i < l:
            start = i
            i += 1
            while i < l and s[i] == s[start]:
                i += 1
            q += str(i - start) + str(s[start])
        n, s = n-1, q

    return s

def seq_func_max2(n):
    s = '1'
    res = [1]
    while n > 1:
        q = ''
        i = 0
        l = len(s)
        while i < l:
            start = i
            i += 1
            while i < l and s[i] == s[start]:
                i += 1
                if (i - start) == 2:
                    break
            q += str(i-start) + str(s[start])
        n, s = n-1, q

    return s
def seq_func_base3(n):
    s = '1'
    res = [1]
    while n > 1:
        q = ''
        i = 0
        l = len(s)
        while i < l:
            start = i
            i += 1
            while i < l and s[i] == s[start]:
                i += 1
            t = i - start
            if t == 3:
                t = '10'
            else:
                t = str(t)
            q += t + str(s[start])
        n, s = n-1, q

    return s

print len(seq_func(31))
