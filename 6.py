#!/usr/bin/env python
# encoding: utf-8
import requests
from zipfile import ZipFile
from StringIO import StringIO
import re


url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
data = requests.get(url).content
zf = ZipFile(StringIO(data))
start = None

for x in zf.namelist():
    if x.lower().startswith('readme'):
        msg = zf.read(x)
        print msg
        start = re.findall('\s(\d+)', msg)[0]
        break

hints = ''
next = start
while True:
    fname = next + '.txt'
    msg = zf.read(fname)
    print msg
    info = zf.getinfo(fname)
    hints += info.comment
    try:
        next = re.findall('\s(\d+)', msg)[0]
    except:
        print hints
        break
