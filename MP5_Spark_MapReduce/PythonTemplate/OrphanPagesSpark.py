#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 100) 
data = lines.collect()

orphans = {}

for line in data:
    page, links = line.strip().split(':')
    links = links.split()
    
    orphans[page] = orphans.get(page, 0)
    
    for link in links:
        # if link != page:
        orphans[link] = orphans.get(link, 0) + 1
            
sorted_orphans = sorted(orphans.items(), key=lambda x: str(x[0]), reverse=True)

output = open(sys.argv[2], "w")
for (k, v) in sorted_orphans[:10]:
    if v == 0:
        output.write('%s\t%s\n' % (k, v))

sc.stop()

