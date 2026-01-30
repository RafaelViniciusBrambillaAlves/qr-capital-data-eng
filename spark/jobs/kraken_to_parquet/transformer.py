from pyspark.sql.functions import (
    from_unixtime, col, hour, dayofmonth, month, year, lit 
)

def transform(df, exchange: str, symbol: str):
    return (
        df.withColumn(
            "event_time",
            from_unixtime(col("timestamp_ms") / 1000).cast("timestamp")
        )
        .withColumn("hour", hour("event_time"))
        .withColumn("day", dayofmonth("event_time"))
        .withColumn("month", month("event_time"))
        .withColumn("year", year("event_time"))
        .withColumn("exchange", lit(exchange))
        .withColumn("symbol", lit(symbol))
    )