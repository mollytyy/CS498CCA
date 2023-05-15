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
    StructField("year", IntegerType(), True),
    StructField("frequency", IntegerType(), True),
    StructField("books", IntegerType(), True)
])

df = spark.createDataFrame(rdd.map(lambda x: x.split("\t")), schema)

# Spark SQL - DataFrame API

df.printSchema()


# Spark SQL - DataFrame API




