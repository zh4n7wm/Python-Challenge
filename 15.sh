#!/bin/bash

for x in $(seq 0 99); do year=$(printf "1%02d6" $x); (cal 1 $year | grep -qE '\s3\s+$' && cal 2 $year | grep -qv '30') && echo $year; done
