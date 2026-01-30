import os 
from pyspark.sql.functions import col

def write_partitioned(df, base_path, exchange):
    output_dir = os.path.join(base_path, exchange)

    query = (
        df
        .writeStream
        .outputMode("append")
        .format("parquet")
        .option("path", output_dir)
        .option("checkpointLocation", os.path.join(output_dir, "_checkpoints"))
        .option("header", "true")
        .partitionBy("year", "month", "day", "hour", "symbol")
        .trigger(processingTime = "10 seconds")
        .start()
    )
    
    return query