#!/usr/bin/env python
# encoding: utf-8

import string

s = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = r"http://www.pythonchallenge.com/pc/def/map.html"

def tran(s):
    sl = [chr(ord(x)+2) if x in string.ascii_letters else x for x in s]
    ss = ''.join(sl)
    table = string.maketrans('{|', 'ab')
    return string.translate(ss, table)

print tran(s)
print
surl = tran(url.split('/')[-1].split('.')[0])
suf = url.split('.')[-1]
print '/'.join(url.split('/')[:-1]) + '/' + surl + '.' + suf
