from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from config import settings
from schema import KRAKEN_SCHEMA

def read_from_kafka(spark: SparkSession):
    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", settings.kafka_bootstrap_servers)
        .option("subscribe", settings.kafka_topic)
        .option("startingOffsets", "earliest")
        .load()
        .selectExpr("CAST(value AS STRING) as json_string")
        .select(from_json(col("json_string"), KRAKEN_SCHEMA).alias("data"))
        .select("data.*")
    )
