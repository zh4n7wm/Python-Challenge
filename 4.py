#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

ori_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = ori_url + "12345"
x = 0

while True:
    print x
    data = urllib.urlopen(url).read()
    if data.find('and the next nothing is') == -1:
        print data, id
        if data.endswith('.html'):
            break
        elif data.startswith('Yes. Divide by two and keep going.'):
            id = str(int(id)/2);
    else:
        id = data.split()[-1]

    url = ori_url + id
    x = x + 1
