from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3
import pandas as pd

def extract_data():
    print("Extracting data from API...")
    # Dummy extract code
    data = {"order_id": [1, 2, 3], "amount": [100, 200, 150]}
    df = pd.DataFrame(data)
    df.to_csv("/tmp/orders.csv", index=False)
    print("Data extracted successfully!")

def load_to_s3():
    print("Loading data to S3...")
    s3 = boto3.client('s3')
    s3.upload_file("/tmp/orders.csv", "your-s3-bucket-name", "orders/orders.csv")
    print("Data uploaded to S3 successfully!")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 10, 1),
    "retries": 1
}

with DAG(
    "ecommerce_etl_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    load = PythonOperator(
        task_id="load_to_s3",
        python_callable=load_to_s3
    )

    extract >> load
