from pyspark.sql.types import *

KRAKEN_SCHEMA = StructType([
    StructField("pair", StringType()),
    StructField("price", DoubleType()),
    StructField("volume", DoubleType()),
    StructField("timestamp_ms", LongType()),
    StructField("side", StringType()),
    StructField("order_type", StringType()),
    StructField("misc", StringType()),
    StructField("source", StringType())
])