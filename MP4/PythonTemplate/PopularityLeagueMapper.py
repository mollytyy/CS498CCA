#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
league = []
league_dict = {}

with open(leaguePath) as f:
    for line in f:
        league.extend(line.strip().split(','))

for line in sys.stdin:
    page, link = line.strip().split('\t')
    
    if page in league:
       league_dict[page] = league_dict.get(link, 0) + int(link)

for l in league_dict:
	print('%s\t%s' % (l, league_dict.get(l)))
