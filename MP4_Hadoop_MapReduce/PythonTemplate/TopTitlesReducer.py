#!/usr/bin/env python3
import sys


words = {}

for line in sys.stdin:
	token = line.split('\t')
	words[token[0]] = words.get(token[0], 0) + int(token[1])
       
sorted_words = sorted(words.items(), key=lambda x: x[1])

for w in sorted_words[-10:]:
    print('%s\t%s' % (w[0], w[1]))
