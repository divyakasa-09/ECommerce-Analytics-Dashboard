from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from avro_deserialization import deserialize_avro_udf
from pyspark.sql.types import StringType, IntegerType, StructType, StructField, MapType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("realtime spark kafka consumer") \
    .master("local") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

kafka_source_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "consumer_activity") \
    .option("startingOffsets", "earliest") \
    .option("group.id", "user_activity_grp") \
    .load()

# This schema should match the Avro schema deserializing
activity_schema = StructType([
    StructField("id", IntegerType()),
    StructField("campaignid", IntegerType()),
    StructField("orderid", IntegerType()),
    StructField("total_amount", IntegerType()),
    StructField("units", IntegerType()),
    StructField("tags", MapType(StringType(), StringType()))
])


# Note: You might need to adjust the deserialization UDF to return a structure that matches this schema
df_deserialized = kafka_source_df.withColumn("activity", deserialize_avro_udf(col("value")).cast(activity_schema))

# Read MySQL Table for Joining with Streaming Data
jdbc_url = "jdbc:mysql://localhost:3306/users"
jdbc_properties = {"user": "root", "password": "example", "driver": "com.mysql.jdbc.Driver"}

demoGraphicData_df = spark.read.jdbc(url=jdbc_url, table="userdemographics", properties=jdbc_properties)

# Join Streaming Data with MySQL Data
# Adjust the join condition based on the structure of the deserialized data
joined_df = df_deserialized.join(demoGraphicData_df, df_deserialized["activity.id"] == demoGraphicData_df["i"])

# Aggregate Data
aggregated_df = joined_df.groupBy("country").count()

# Write Aggregated Data to Console for Testing
query_console = aggregated_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Define a function for writing aggregated data back to MySQL
def write_to_mysql(batch_df, batch_id):
    batch_df.write.jdbc(url=jdbc_url, table="users.countryAgg", mode="overwrite", properties=jdbc_properties)

# Write Aggregated Data Back to MySQL using foreachBatch
query_mysql = aggregated_df.writeStream \
    .outputMode("complete") \
    .foreachBatch(write_to_mysql) \
    .start()

query_mysql.awaitTermination()
