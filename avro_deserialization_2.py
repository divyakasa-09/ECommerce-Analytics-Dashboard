from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, StructType, StructField, IntegerType, MapType
import fastavro
from io import BytesIO

# Define the schema corresponding to your Avro data
avro_schema = {
    "type": "record",
    "name": "ConsumerActivity",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "campaignid", "type": "int"},
        {"name": "orderid", "type": "int"},
        {"name": "total_amount", "type": "int"},
        {"name": "units", "type": "int"},
        {"name": "tags", "type": {"type": "map", "values": "string"}}
    ]
}

def deserialize(data):
    if data is None:
        return None
    try:
        bytes_reader = BytesIO(data)
        avro_reader = fastavro.reader(bytes_reader, reader_schema=avro_schema)
        return next(avro_reader)  # Assuming each Kafka message contains a single Avro record
    except Exception as e:
        return None

deserialize_avro_udf = udf(deserialize, StringType())  # Adjust the return type according to your needs
