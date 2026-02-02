# kraken_spark_streaming_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_eng',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='kraken_spark_streaming',
    default_args = default_args,
    description = 'Stream Bitcoin prices from Kraken to Parquet',
    schedule_interval = '@daily', 
    catchup = False,
    tags = ['bitcoin', 'kraken', 'spark', 'kafka'],
) as dag:
    
    start = DummyOperator(task_id='start')
    
    check_services = BashOperator(
        task_id = 'check_services',
        bash_command="""
        docker ps | grep spark-master && \
        docker ps | grep kafka && \
        echo "All services are running"
        """
    )
    
    run_spark_stream = BashOperator(
        task_id = 'run_spark_stream',
        bash_command = """
        docker exec spark-master \
        /opt/spark/bin/spark-submit \
        --master spark://spark-master:7077 \
        --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
        --conf spark.jars.ivy=/tmp/.ivy2 \
        /opt/spark/jobs/kraken_to_parquet/main.py
        """
    )

    monitor_stream = BashOperator(
        task_id = 'monitor_stream',
        bash_command = """
        echo "Streaming job started. Check Spark UI at http://localhost:4040"
        """,
    )
    
    end = DummyOperator(task_id = 'end')
    
    start >> check_services >> run_spark_stream >> monitor_stream >> end