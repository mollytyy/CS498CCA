#!/usr/bin/env python
import sys
import math
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1)
data = lines.collect()

all_values = []

for title in data:
    title, count = title.split('\t')
    all_values.append(int(count))

ans1 = math.floor(sum(all_values) / len(all_values))
ans2 = sum(all_values)
ans3 = min(all_values)
ans4 = max(all_values) 
ans5 = math.floor(sum((v - ans1) ** 2 for v in all_values) / len(all_values))

outputFile = open(sys.argv[2], "w")

outputFile.write('Mean\t%s\n' % ans1)
outputFile.write('Sum\t%s\n' % ans2)
outputFile.write('Min\t%s\n' % ans3)
outputFile.write('Max\t%s\n' % ans4)
outputFile.write('Var\t%s\n' % ans5)

sc.stop()
