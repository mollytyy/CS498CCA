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

rdd = sc.textFile("gbooks")

schema = StructType([
    StructField("word", StringType(), True),
    StructField("count1", StringType(), True),
    StructField("count2", StringType(), True),
    StructField("count3", StringType(), True)
])

df = sqlContext.createDataFrame(rdd.map(lambda x: x.split("\t")), schema)

# Spark SQL - DataFrame API

####
# 2. Counting (10 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL 
df.createOrReplaceTempView("MP8")
sqlContext.sql("SELECT COUNT(*) FROM MP8").show()

# +--------+                                                                              
# |count(1)|
# +--------+
# |86618505|
# +--------+


