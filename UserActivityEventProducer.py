from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import random
from user_activity_util import generate_user_activity

# Kafka and Schema Registry configuration
config = {
    'bootstrap.servers': 'http://localhost:9092',
    'schema.registry.url': 'http://localhost:8081',
    'key.serializer': avro.loads,
    'value.serializer': avro.loads
}

# Define Avro schema for UserActivity
value_schema_str = """
{
   "namespace": "jobs.stream",
   "name": "UserActivity",
   "type": "record",
   "fields" : [
     {
       "name" : "id",
       "type" : "int"
     },
     {
       "name" : "campaignId",
       "type" : "int"
     },
     {
       "name" : "orderId",
       "type" : "int"
     },
     {
       "name" : "amount",
       "type" : "int"
     },
     {
       "name" : "units",
       "type" : "int"
     },
     {
       "name" : "activity",
       "type" : "string"
     },
     {
       "name" : "tags",
       "type" : {"type": "map", "values": "string"}
     }
   ]
}
"""
value_schema = avro.loads(value_schema_str)
key_schema = avro.loads('{"type": "string"}')

producer = AvroProducer(config, default_key_schema=key_schema, default_value_schema=value_schema)

topic = "consumer_activity"

def send_user_activity_event():
    activity = generate_user_activity()
    key = str(random.randint(1, 10000))
    value = {
        "id": activity["id"],
        "campaignId": activity["campaignId"],
        "orderId": activity["orderId"],
        "amount": activity["amount"],
        "units": activity["units"],
        "activity": activity["activity"],
        "tags": {"activity": activity["activity"]}
    }
    producer.produce(topic=topic, key=key, value=value)
    producer.flush()
    print(f"Sent activity for user {activity['id']}")

if __name__ == "__main__":
    while True:
        send_user_activity_event()
        # Simulate event production interval
        time.sleep(1)
