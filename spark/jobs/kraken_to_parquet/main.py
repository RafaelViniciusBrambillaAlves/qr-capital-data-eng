from pyspark.sql import SparkSession
from config import settings
from reader import read_from_kafka
from transformer import transform
from writer import write_partitioned

def main():
    spark = (
        SparkSession.builder
        .appName(settings.spark_app_name)
        .master("spark://spark-master:7077")
        .config("spark.sql.parquet.compression.codec", "snappy")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    df = read_from_kafka(spark)
    df = transform(df, settings.exchange, settings.symbol)

    query = write_partitioned(
        df,
        settings.base_output_path,
        settings.exchange
    )

    query.awaitTermination()

if __name__ == "__main__":
    main()
