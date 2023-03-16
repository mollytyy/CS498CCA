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
    StructField("count1", IntegerType(), True),
    StructField("count2", IntegerType(), True),
    StructField("count3", IntegerType(), True)
])

rdd = rdd.map(lambda x: x.split("\t")).map(lambda x: (x[0], int(x[1]), int(x[2]), int(x[3]))).cache()


df = sqlContext.createDataFrame(rdd, schema)

# Spark SQL - DataFrame API
df.createOrReplaceTempView("MP8")

####
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

df2 = df.select("word", "count1").distinct().limit(100)
df2.createOrReplaceTempView('gbooks2')

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API
sqlContext.setConf("spark.sql.broadcastTimeout", "3000")
result = sqlContext.sql("SELECT COUNT(*) AS count FROM gbooks2 AS A INNER JOIN gbooks2 AS B ON A.count1 = B.count1").collect()
# result = sqlContext.sql("SELECT COUNT(*) AS count FROM MP8 INNER JOIN gbooks2 ON MP8.count1 = gbooks2.count1").collect()
count_value = result[0]['count']
print(count_value)
# output: 210
