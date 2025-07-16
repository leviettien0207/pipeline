 import datetime

 from airflow.sdk import DAG
 from airflow.providers.standard.operators.empty import EmptyOperator

 with DAG(
     dag_id="example_dag",
     start_date=datetime.datetime(2025, 7, 17),
     schedule="@daily",
 ):
     EmptyOperator(task_id="task")
