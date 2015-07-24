#!/usr/bin/env python
# encoding: utf-8

import requests
import re
import sys

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
url = url + '?nothing='
start = 12345
next = start

if (sys.argv) == 1:
    next = sys.argv[1]

while True:
    next_url = url + str(next)
    data = requests.get(next_url).content

    if re.match('\.html$', data):
        print data
        break

    nlist = re.findall('\d+$', data)
    if len(nlist) == 1:
        next = nlist[0]
    else:
        print data
        if re.findall('\.html$', data):
            break
        else:
            next = start/2
    print next
