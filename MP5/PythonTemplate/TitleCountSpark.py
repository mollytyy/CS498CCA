#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopwords = []
delims = []
title_counts = {}

with open(stopWordsPath) as f:
    for line in f:
        stopwords.append(line.strip())

with open(delimitersPath) as f:
    for line in f:
        delims = [l for l in line]

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)
data = lines.collect()

for title in data:
    for d in delims:
        title = title.replace(d, ' ')
    splitted = title.split(' ')
    for s in splitted:
        s = s.strip().lower()
        if s not in stopwords and s != '':
            title_counts[s] = title_counts.get(s, 0) + 1

sorted_counts = dict(sorted(title_counts.items(), key=lambda x: x[1])[-10:])
sorted_counts = sorted(sorted_counts.items(), key=lambda x: x[0])

outputFile = open(sys.argv[4],"w")
for c in sorted_counts:
    outputFile.write('%s\t%s\n' %(c[0], c[1]))
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
