import json 
from kafka import KafkaProducer
from app.config import settings

def create_kafka_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers = settings.kafka_bootsrap_servers,
        value_serializer = lambda v: json.dumps(v).encode("utf-8"),
        acks = "all",
        retries = 5,
        linger_ms = 50
    )