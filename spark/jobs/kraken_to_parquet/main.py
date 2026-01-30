from pyspark.sql import SparkSession
from config import settings
from reader import read_from_kafka
from transformer import transform
from writer import write_partitioned
from datetime import time

def main():
    spark = (
        SparkSession.builder
        .appName(settings.spark_app_name)
        .master("spark://spark-master:7077")
        .getOrCreate()
    )
    
    df = read_from_kafka(spark)

    df = transform(df, settings.exchange, settings.symbol)

    query = write_partitioned(df, settings.base_output_path, settings.exchange)
    
    query.awaitTermination()

    time.sleep(60)  
    query.stop()

    spark.stop()

if __name__ == "__main__":
    main()