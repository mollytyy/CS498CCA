#!/usr/bin/env python3
from operator import itemgetter
import sys


words = {}
# input comes from STDIN
for line in sys.stdin:
    token = line.split('\t')
    words[token[0]] = words.get(token[0], 0) + 1

for w in words:
    print('%s\t%s' % (w, words[w]))