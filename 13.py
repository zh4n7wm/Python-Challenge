#!/usr/bin/env python
# encoding: utf-8
"""
level 13: http://www.pythonchallenge.com/pc/return/disproportional.html
访问http://www.pythonchallenge.com/pc/phonebook.php，根据错误搜索知道是xml-rpc访问。
用Python xmlrpclib模块访问该服务。
"""

from __future__ import print_function
import xmlrpclib
import requests
from mylib import USER, PASSWORD

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.ServerProxy(url)
# 列出该服务可以方法
print(server.system.listMethods())
print('\n')

# 获取phone方法签名及帮助文档
print(server.system.methodHelp('phone'))
print('\n')
print(server.system.methodSignature('phone'))  # 第一个是返回值，后面都是参数
print('\n')

# 尝试调用phone
print(server.phone('5'))
print('\n')

# 提示He is not evil，想起level 12中有个图片内容是Bert is evil, go back!
print(server.phone('Bert'))
print('\n')
answer = server.phone('Bert').split('-')[1]
base_url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
try_url = 'http://www.pythonchallenge.com/pc/return/%s.html' % answer
print(requests.get(try_url, auth=(USER, PASSWORD)).content)
# 提示用小写字母
print('answer: %s' % answer.lower())
