import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
# Get Spark context
sc = SparkContext()
# From spark context get glue context and spark session
glueContext = GlueContext(sc)
# Create and init job
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Begin TODOs - add your code starting from here. Comments
# are provided for each statement that you may need to add.

# 1. Create a Glue client to access the Data Catalog API
client = boto3.client('glue')

# 2. Create a dynamic frame from AWS Glue catalog table. In the following lines
# use the create_dynamic_frame.from_catalog() API of the GlueContext class. Use
# the Glue catalog database and table name (output of job 1) as arguments.
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="mp9v2-flights-db", table_name="job1output")

# 3. Get Spark dataframe from the Glue dynamic frame created above
f1 = dynamic_frame.toDF()

# 4. Create a new time_zone_difference column and add it to the Spark data frame.
# See the MP description on how to calculate the value of the time zone
# difference between the arrival and departure airports.
f1 = f1.withColumn("time_zone_difference", (col("scheduled_arrival") / 100)*60 + (col("scheduled_arrival") % 100) -
                   ((col("scheduled_departure") / 100)*60 + (col("scheduled_departure") % 100) + col("scheduled_time")) % (24*60))
f1 = f1.withColumn("time_zone_difference", col(
    "time_zone_difference").cast(IntegerType()))

# 5. Convert Spark data frame back to Glue dynamic frame
# Note - you can do step 4 using AWS Glue dynamic frame APIs also if you want
# to avoid steps 3 and 5. However, it maybe easier to do the transformations
# in step 4 using Spark data frame.
dynamic_frame = DynamicFrame.fromDF(f1, glueContext, "dynamic_frame")

# 6. Get the existing Glue catalog table schema. You can use the glue client
# created in step 1 and use its get_table() API to get the table schema which
# will be a python dictionary. You can see the response of get_table() here:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_table.html
table_name = "job1output"
database_name = "mp9v2-flights-db"
response = client.get_table(DatabaseName=database_name, Name=table_name)
table_schema = response["Table"]["StorageDescriptor"]["Columns"]

# 7. Delete the following fields in the table schema dictionary as
# the update_table API gives ParamValidationError when these fields are present:
# 'UpdateTime', 'IsRegisteredWithLakeFormation', 'CreatedBy', 'DatabaseName',
# 'CreateTime', 'CatalogId'
fields_to_delete = ['UpdateTime', 'IsRegisteredWithLakeFormation',
                    'CreatedBy', 'DatabaseName', 'CreateTime', 'CatalogId']
for field in fields_to_delete:
    del response["Table"][field]

# 8. Define the new column 'time_zone_difference' to be added to the table schema
new_column = {
    "Name": "time_zone_difference",
    "Type": "int",
    "Comment": "Time difference between arrival and departure airports in minutes"
}

# 9. Append the new column info to the table dictionary (obtained in step 6) columns list
table_schema.append(new_column)
response["Table"]["StorageDescriptor"]["Columns"] = table_schema

# 10. Update the table with the new schema. Use the update_table() API of glue client:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_table.html
client.update_table(DatabaseName=database_name, TableInput=response["Table"])

# 11. Get the output S3 bucket in which the transformed table data will be
# stored. Use the getSink() API of the GlueContext class.
sink = glueContext.getSink("s3", path="s3://mp9v2job2output/")

# 12. Set the catalog database and table using the setCatalogInfo() API on
# the object obtained in step 11.
sink.setCatalogInfo(catalogDatabase=database_name,
                    catalogTableName="job2output")

# 13. Set the format to 'json' using setFormat() API
sink.setFormat("json")

# 14. Write data into S3 bucket using writeFrame()
sink.writeFrame(dynamic_frame)
# End TODOs

# Commit job
job.commit()
