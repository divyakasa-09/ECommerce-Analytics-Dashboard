from pyspark.sql.functions import udf
from pyspark.sql.types import BinaryType
import fastavro
from io import BytesIO

def serialize(record):
    if record is None:
        return None
    try:
        bytes_writer = BytesIO()
        fastavro.schemaless_writer(bytes_writer, avro_schema, record)
        return bytes_writer.getvalue()
    except Exception as e:
        return None

# Define the UDF
serialize_avro_udf = udf(serialize, BinaryType())
