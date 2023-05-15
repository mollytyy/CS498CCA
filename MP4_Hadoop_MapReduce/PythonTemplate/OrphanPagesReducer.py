#!/usr/bin/env python3
import sys

orphans_dict = {}


for line in sys.stdin:
    page, counts = line.strip().split('\t')
    
    orphans_dict[page] = orphans_dict.get(page, 0) + int(counts)
    
sorted_orphans = sorted(orphans_dict.items(), key=lambda x: int(x[0]))

for (k, v) in sorted_orphans:
    if orphans_dict[k] == 0:
        print('%s'%k)

