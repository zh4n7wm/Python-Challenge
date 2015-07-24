#!/usr/bin/env python
# encoding: utf-8

import requests
import re


def get_comment_from_src(url):
    data = requests.get(url).content
    comment = re.findall('<!--([^>]+)-->', data)
    return comment

