from pyspark.sql.functions import col, lag
from pyspark import SparkContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import *

sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

####
# 1. Setup : Write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: word (string), 1: year (int), 2: frequency (int), 3: books (int)
rdd = sc.textFile("gbooks")

schema = StructType([
    StructField("word", StringType(), True),
    StructField("year", StringType(), True),
    StructField("frequency", StringType(), True),
    StructField("books", StringType(), True)
])

df = spark.createDataFrame(rdd.map(lambda x: x.split("\t")), schema)

df.createOrReplaceTempView("MP8")

###
# 2. Frequency Increase (16 points): analyze the frequency increase of words starting from the year 1500 to the year 2000
###
# Spark SQL - DataFrame API
df_filtered = df.filter((col("year") >= 1500) & (col("year") <= 2000))
window = Window.partitionBy("word").orderBy("year")
df_with_increase = df_filtered.withColumn("frequency_increase", lag("frequency", -1).over(window).cast(IntegerType()))
df_with_increase = df_with_increase.groupBy("word").agg(sum("frequency_increase").alias("total_increase"))
df_with_increase = df_with_increase.orderBy(desc("total_increase"))
df_with_increase.show(20)