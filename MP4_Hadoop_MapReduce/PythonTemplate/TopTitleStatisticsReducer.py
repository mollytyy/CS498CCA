#!/usr/bin/env python3
import sys
import math

all_values = []
stats = {
    "Mean": 0,
    "Sum": 0,
    "Min": 0,
    "Max": 0,
    "Var": 0
}

for line in sys.stdin:
    line = line.strip()
    all_values.append(int(line))

stats['Mean'] = math.floor(sum(all_values) / len(all_values))
stats['Sum'] = sum(all_values)
stats['Min'] = min(all_values)
stats['Max'] = max(all_values) 
stats['Var'] = math.floor(sum((v - stats['Mean']) ** 2 for v in all_values) / len(all_values))

for s in stats:
    print('%s\t%s' % (s, stats[s]))
