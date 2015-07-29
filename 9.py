#!/usr/bin/env python
# encoding: utf-8
"""
level 9.
url: http://www.pythonchallenge.com/pc/return/good.html
user: huge
passwd: file
"""

from __future__ import print_function
import requests
from requests.auth import HTTPBasicAuth
import re
from PIL import Image
from PIL import ImageDraw


url = 'http://www.pythonchallenge.com/pc/return/good.html'
user = 'huge'
passwd = 'file'
data = requests.get(url, auth=HTTPBasicAuth(user, passwd)).content
comment = re.findall('<!--([^-]+)-->', data)[1]
first = re.findall('first:\n([\d,\n]+)\n', comment)[0].replace('\n', '').split(',')
second = re.findall('second:\n([\d,\n]+)\n', comment)[0].replace('\n', '').split(',')
first = [int(x) for x in first]
second = [int(x) for x in second]
#print(first)
#print(second)

im = Image.new('RGBA', (800, 800), )
draw = ImageDraw.Draw(im)
draw.line(first)
draw.line(second)
im.show()
