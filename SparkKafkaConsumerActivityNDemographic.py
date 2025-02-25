from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, struct, lit
# Import or define your custom UDFs here
from avro_deserialization_2 import deserialize_avro_udf
from avro_serialize import serialize_avro_udf

spark = SparkSession.builder \
    .appName("PySpark Kafka Avro Integration") \
    .master("local[2]") \
    .getOrCreate()

# Kafka Source for Streaming Data
user_activity_stream = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "consumer_activity") \
    .option("startingOffsets", "earliest") \
    .option("group.id", "user_activity_grp") \
    .load()

# Deserialize Avro data from Kafka
user_activity_stream_des = user_activity_stream.select(deserialize_avro_udf(col("value")).alias("activity"))

# Read MySQL Data
jdbc_url = "jdbc:mysql://localhost:3306/users"
jdbc_properties = {"user": "root", "password": "example", "driver": "com.mysql.jdbc.Driver"}
demographic_data = spark.read.jdbc(url=jdbc_url, table="userdemographics", properties=jdbc_properties)

# Join Streaming Data with MySQL Data
joined_stream = user_activity_stream_des.join(demographic_data, expr("activity.id = i"))

# Assuming transformation logic is needed here, for example, merging tags from both sources
transformed_stream = joined_stream.withColumn("activity",
                                               struct(
                                                   col("activity.*"),  # Keeps existing activity fields
                                                   col("age"),  # Adds age from demographic data
                                                   lit("merged_tags").alias("tags")
                                               )) \
                                  .withColumn("new_field", lit("Some Value"))  # Example of adding a new field

# Serialize data back into Avro for Kafka
final_stream = transformed_stream.select(serialize_avro_udf(struct(col("activity.*"), col("new_field"))).alias("value"))

# Write Back to Kafka
query = final_stream.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "user_activity_demographics") \
    .option("checkpointLocation", "/tmp/checkpoints/") \
    .start()

query.awaitTermination()
