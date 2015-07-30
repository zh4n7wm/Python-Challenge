#!/usr/bin/env python
# encoding: utf-8
"""
level 14: http://www.pythonchallenge.com/pc/return/italy.html
参考了kosl90的答案
  --------> x
  |
  |
  |
  v
  y
"""

import requests
from mylib import USER, PASSWORD
from StringIO import StringIO
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/wire.png'
fimg = StringIO(requests.get(url, auth=(USER, PASSWORD)).content)
im = Image.open(fimg)
data = list(im.getdata())
nim = Image.new(im.mode, (100, 100))

l = [[x, x - 1, x - 1, x - 2] for x in range(100, 0, -2)]
seq = reduce(lambda x, y: x + y, l)
n = 0  # data index
direct = [(1, 0),   # right; x+1, y
          (0, 1),   # down;    x, y+1
          (-1, 0),  # left;  x-1, y
          (0, -1),  # up;      x, y-1
          ]
k = 0  # direct index
pos = (-1, 0)

for i in seq:
    for j in xrange(i):
        pos = map(lambda x, y: x + y, pos, direct[k])
        nim.putpixel(pos, data[n])
        n += 1
    k = (k + 1) % len(direct)

nim.show()
