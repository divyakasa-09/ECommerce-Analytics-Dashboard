from pyspark.sql import SparkSession
from pyspark.sql.functions import rand
from demo_graphic_data_util import get_country, get_age, get_gender, get_state
import pandas as pd

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Batch User Demographic Data") \
    .master("local") \
    .getOrCreate()

# Generate User Demographic Data
users = [{
    "i": i,
    "age": get_age(),
    "gender": get_gender(),
    "state": get_state(get_country()),
    "country": get_country()
} for i in range(100000)]

# Convert to Spark DataFrame
user_df = spark.createDataFrame(pd.DataFrame(users))

# Write to MySQL
user_df.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/users") \
    .option("dbtable", "userdemographics") \
    .option("user", "root") \
    .option("password", "example") \
    .mode("overwrite") \
    .save()

print("Data Creation is completed")
