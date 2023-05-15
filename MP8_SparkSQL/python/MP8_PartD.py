from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API
rdd = sc.textFile("gbooks")

schema = StructType([
    StructField("word", StringType(), True),
    StructField("count1", StringType(), True),
    StructField("count2", StringType(), True),
    StructField("count3", StringType(), True)
])

df = sqlContext.createDataFrame(rdd.map(lambda x: x.split("\t")), schema)


####
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL
df.createOrReplaceTempView("MP8")
# sqlContext.sql("SELECT place AS word, COUNT(*) FROM MP8 ORDER BY COUNT(*) DESC").show(3)
sqlContext.sql("SELECT word, COUNT(*) FROM MP8 GROUP BY word ORDER BY COUNT(*) DESC").show(3)

# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+

