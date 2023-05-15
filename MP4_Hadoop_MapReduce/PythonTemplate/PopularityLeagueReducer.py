#!/usr/bin/env python3
import sys

league_dict = {}

# input comes from STDIN
for line in sys.stdin:
    page, links = line.strip().split('\t')
    league_dict[page] = league_dict.get(page, 0) + int(links)

sorted_league = sorted(league_dict.items(), key=lambda x: int(x[0]), reverse=True)
    
for page, link in sorted_league:
    rank = 0
    for l in league_dict:
        if league_dict.get(l) < link:
            rank += 1
    
    print('%s\t%s' % (page, rank))