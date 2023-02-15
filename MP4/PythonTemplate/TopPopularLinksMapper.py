#!/usr/bin/env python3
import sys


links_dict = {}

for line in sys.stdin:
    link, count = line.strip().split('\t')
    links_dict[int(link)] = links_dict.get(link, 0) + int(count)
    
sorted_links = sorted(links_dict.items(), key=lambda x: x[1])

for (l, c) in sorted_links[-10:]:
    print('%s\t%s' %(l, c))
