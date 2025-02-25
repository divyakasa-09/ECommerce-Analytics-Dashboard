from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import fastavro
from io import BytesIO

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

def deserialize_avro(data):
    if data is None:
        return None
    try:
        bytes_reader = BytesIO(data)
        decoder = fastavro.reader(bytes_reader, reader_schema=avro_schema)
        for record in decoder:
            return record  # Assuming each message contains a single record
    except Exception as e:
        return None

# Register the UDF
deserialize_avro_udf = udf(deserialize_avro, StringType())  # Adjust the return type based on the Avro schema
