#!/usr/bin/env python
# encoding: utf-8
"""
level 11: http://www.pythonchallenge.com/pc/return/5808.html
"""

from StringIO import StringIO
from PIL import Image
import requests
from mylib import USER, PASSWORD

img_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
fimg = StringIO(requests.get(img_url, auth=(USER, PASSWORD)).content)
im = Image.open(fimg)
data = list(im.getdata())
even = data[::2]
odd = data[1::2]
even_im = Image.new(im.mode, im.size)
even_im.putdata(even)
even_im.show()

odd_im = Image.new(im.mode, im.size)
odd_im.putdata(odd)
odd_im.show()
