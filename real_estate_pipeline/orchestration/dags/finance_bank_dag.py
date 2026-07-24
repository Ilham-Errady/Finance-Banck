from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'rime_errady',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'finance_bank_pipeline',
    default_args=default_args,
    description='Pipeline dbt et Ingestion pour Finance-Bank Data Warehouse',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task 1: Ingestion / Chargement des données brutes
    start_pipeline = BashOperator(
        task_id='start_pipeline',
        bash_command='echo "Demarrage du pipeline Finance-Bank..."',
    )

    # Task 2: Exécution des modèles dbt (Silver + Gold)
    run_dbt_models = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /opt/airflow/dbt_project && dbt run',
    )

    # Task 3: Exécution des tests Data Quality dbt
    test_dbt_models = BashOperator(
        task_id='test_dbt_models',
        bash_command='cd /opt/airflow/dbt_project && dbt test',
    )

    # Task 4: Fin du Pipeline
    end_pipeline = BashOperator(
        task_id='end_pipeline',
        bash_command='echo "Pipeline Finance-Bank termine avec succes !"',
    )

    # Ordre d'exécution des tâches (Dependencies)
    start_pipeline >> run_dbt_models >> test_dbt_models >> end_pipeline