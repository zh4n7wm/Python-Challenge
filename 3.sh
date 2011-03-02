#!/bin/bash

grep -Po '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]' 3 | cut -c5 | xargs | tr -d ' '
