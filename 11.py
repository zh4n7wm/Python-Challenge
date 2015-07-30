#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ox0spy <Ox0spy@gmail.com>
# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
from StringIO import StringIO
import requests
from mylib import USER, PASSWORD

img_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
fimg = StringIO(requests.get(img_url, auth=(USER, PASSWORD)).content)
img = Image.open(fimg)
data = []
for h in range(img.size[1]):
    for w in range(img.size[0]):
        data.append(img.getpixel((w, h)))
odds = data[1::2]
evens = data[::2]

evens.extend(odds)
data = evens
width = img.size[0]
height = img.size[1]
new_img = Image.new('RGB', (width, height),  'white')

i = 0
for h in range(new_img.size[1]):
    for w in range(new_img.size[0]):
        new_img.putpixel((w, h), data[i])
        i += 1
new_img.show()
