from pyspark import SparkContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession

sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

####
# 1. Setup : Write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: word (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)
rdd = sc.textFile("gbooks")

schema = StructType([
    StructField("word", StringType(), True),
    StructField("count1", StringType(), True),
    StructField("count2", StringType(), True),
    StructField("count3", StringType(), True)
])

df = spark.createDataFrame(rdd.map(lambda x: x.split("\t")), schema)


# Spark SQL - DataFrame API

####
# 2. Counting (16 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL 
df.createOrReplaceTempView("MP8")
spark.sql("SELECT COUNT(*) FROM MP8").show()

# sqlContext.sql(query).show() or df.show()
# +--------+
# |count(1)|
# +--------+
# |   50013|
# +--------+


