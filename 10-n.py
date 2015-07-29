#!/usr/bin/env python
# encoding: utf-8
"""
level 10: http://www.pythonchallenge.com/pc/return/bull.html
sequence: a = [1, 11, 21, 1211, 111221,
len(a[30]) = ?
a list index start from zero!
"""

from __future__ import print_function

def look_and_say(n):
    if n < 0:
        return None

    if n == 0:
        return 1
    else:
        s = str(look_and_say(n - 1))
        # [(key1, count1), (key2, count2), ...]
        # [k1, k2, ...]
        # [c1, c2, ...]
        keys = []
        counts = []
        n = 0
        while True:
            if n < len(s):
                if n > 0 and s[n] in keys and s[n] == s[n - 1]:
                    counts[-1] += 1
                else:
                    keys.append(s[n])
                    counts.append(1)
                n += 1
            else:
                break

        res = []
        i = 0
        while i < len(keys):
            res.append(str(counts[i]))
            res.append(str(keys[i]))
            i += 1

        return ''.join(res)


print(len(look_and_say(30)))
