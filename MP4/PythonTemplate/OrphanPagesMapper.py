#!/usr/bin/env python3
import sys


for line in sys.stdin:
    page, links = line.strip().split(':')
    links = links.split()
    
    if len(links) > 0:
        print('%s\t0'%page)
        
        for link in links:
            if link != page:
                print('%s\t1'%link)
