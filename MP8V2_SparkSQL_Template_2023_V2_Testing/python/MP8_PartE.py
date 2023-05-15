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
    StructField("year", IntegerType(), True),
    StructField("frequency", IntegerType(), True),
    StructField("books", IntegerType(), True)
])

rdd = rdd.map(lambda x: x.split("\t")).map(lambda x: (x[0], int(x[1]), int(x[2]), int(x[3]))).cache()

df = spark.createDataFrame(rdd, schema)

# Spark SQL - DataFrame API


####
# 5. Joining (16 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

df2 = df.select("word", "year").distinct().limit(100)
df2.createOrReplaceTempView('gbooks2')

# Spark SQL API
result = spark.sql("SELECT COUNT(*) as count FROM gbooks2 A CROSS JOIN gbooks2 B ON A.year = B.year").collect()
count_value = result[0]['count']
print(count_value)
# output: 162

