from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "marco",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="elt_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    ingestion = BashOperator(
        task_id="run_ingestion",
        bash_command="python /opt/airflow/scripts/ingestion/main.py"
    )

    dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="""
        cd /opt/airflow/dbt && \
        dbt run \
        --log-path /tmp \
        --target-path /tmp
        """
        )

    dbt_test = BashOperator(
    task_id="dbt_test",
    bash_command="""
    cd /opt/airflow/dbt && \
    dbt test \
    --log-path /tmp \
    --target-path /tmp
    """)

    ingestion >> dbt_run >> dbt_test