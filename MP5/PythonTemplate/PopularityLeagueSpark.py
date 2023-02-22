#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 100) 
data = lines.collect()

leagueIds = sc.textFile(sys.argv[2], 1)
league_list = leagueIds.collect()

league_dict = {}

for line in data:
    page, links = line.strip().split(':')
    links = links.split()
    
    for link in links:
        if link in league_list:
            league_dict[int(link)] = league_dict.get(int(link), 0) + 1

sorted_league = sorted(league_dict.items(), key=lambda x: int(x[1]))

ssorted = []
rank = 0

for page, count in sorted_league:
    ssorted.append((str(page), str(rank)))
    rank += 1

ssorted_league = sorted(ssorted, key=lambda x: x[0])

output = open(sys.argv[3], "w")
for k, v in ssorted_league:
    output.write(k + '\t' + v + '\n')


sc.stop()

