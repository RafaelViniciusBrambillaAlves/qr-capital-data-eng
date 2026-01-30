from pyspark.sql import DataFrame

def write_partitioned(df: DataFrame, base_output_path: str, exchange: str):
    output_path = f"{base_output_path}/{exchange}"

    return (
        df.writeStream
        .format("parquet")
        .outputMode("append")
        .option("path", output_path)
        .option("checkpointLocation", f"{output_path}/_checkpoints")
        .partitionBy("year", "month", "day", "hour", "symbol")
        .trigger(availableNow=True)   # 🔥 A CHAVE DA SOLUÇÃO
        .start()
    )
