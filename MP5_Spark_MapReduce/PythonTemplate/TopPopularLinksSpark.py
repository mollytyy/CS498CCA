#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 100) 
data = lines.collect()

popular = {}

for line in data:
    page, links = line.strip().split(':')
    links = links.split()
    
    for link in links:
        popular[int(link)] = popular.get(int(link), 0) + 1

sorted_popular = sorted(popular.items(), key=lambda x: int(x[1]), reverse=True)
ssorted_popular = sorted(sorted_popular[:10], key=lambda x: str(x[0]))

output = open(sys.argv[2], "w")
for (k, v) in ssorted_popular:
    output.write(str(k) + '\t' + str(v) + '\n')

sc.stop()
