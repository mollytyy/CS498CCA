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
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)
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
# 3. Filtering (16 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL
df.createOrReplaceTempView("MP8")
spark.sql("SELECT COUNT(*) FROM MP8 WHERE word = 'ATTRIBUTE'").show()

# +--------+
# |count(1)|
# +--------+
# |      11|
# +--------+


