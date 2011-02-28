#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

ori_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = ori_url + "12345"
x = 0

while True:
    print x
    data = urllib.urlopen(url).read()
    if not data.startswith('and the next nothing is'):
        print data
        print id
        if data.endswith('.html'):
            break

    id = data.split()[-1]
    url = ori_url + id
    x = x + 1
