#!/usr/bin/env python3
import sys


links_count = {}

# input comes from STDIN
for line in sys.stdin:
    line, count = line.strip().split('\t')
    links_count[line] = links_count.get(line, 0) + int(count)

for l in links_count:
    if links_count[l]:
        print('%s\t%s' % (l , links_count[l]))