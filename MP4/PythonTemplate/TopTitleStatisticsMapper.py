#!/usr/bin/env python3
import sys


for line in sys.stdin:
    word, value = line.strip().split('\t')
    if int(value) > 0:
        print(int(value))
