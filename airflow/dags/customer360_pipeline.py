from airflow import DAG

from airflow.operators.python import (
    PythonOperator
)

from datetime import datetime

from src.customer_pipeline import run


with DAG(
    dag_id="customer360_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    load_customer_data = PythonOperator(
        task_id="load_customer_data",
        python_callable=run
    )