from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import yaml


def process_source(source_name):

    print(
        f"Processing source {source_name}"
    )


with DAG(
    dag_id="customer360_pipeline",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    schedule="@daily"
) as dag:

    with open(
        "/opt/airflow/configs/source_metadata.yaml"
    ) as file:

        metadata = yaml.safe_load(file)

    for source_name in metadata["sources"]:

        PythonOperator(
            task_id=f"ingest_{source_name}",
            python_callable=process_source,
            op_kwargs={
                "source_name": source_name
            }
        )