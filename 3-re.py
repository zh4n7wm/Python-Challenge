#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = open('3', 'r').read()
pattern = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
print ''.join(re.findall(pattern, s))
