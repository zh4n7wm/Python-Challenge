#!/bin/bash

url='http://www.pythonchallenge.com/pc/def/equality.html'
curl -s $url | sed -ne '/<!--/,/-->/p' | \
    grep -Eo '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]' | \
    cut -c5 | xargs | tr -d ' '
