#!/usr/bin/env python3

import sys
import string


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopwords = []
with open(stopWordsPath) as f:
    for l in f:
        stopwords.append(l.strip())

delims = ''
with open(delimitersPath) as f:
    for l in f:
        delims += l

for line in sys.stdin:
    line = line.strip()
    for d in delims:
        line = line.replace(d, ' ')
    splitted = line.split(' ')
    
    smaller = []
    
    for s in splitted:
        if s.lower() not in stopwords and s != '':
            smaller.append(s.lower())
    
    for s in smaller:
        print('%s\t%s' % (s, 1))

    # print('%s\t%s' % (  ,  )) pass this output to reducer

