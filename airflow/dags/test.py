# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

from airflow.operators.python import PythonVirtualenvOperator



# def get_registerd_user():
#    from faker import Faker
#    fake = Faker()
#    print(fake.name())

def callable_virtualenv():

    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    for _ in range(4):
        print(Style.DIM + "Please wait...", flush=True)
        sleep(1)
    print("Finished")


#defining DAG arguments
default_args = {
    'owner': 'Mahesh Pathak',
    'start_date': days_ago(0),
    'email': ['mahesh@somemail.com'],
    'email_on_failuar': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# define the DAG
dag = DAG(
    dag_id= 'ETL_toll_data',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    description='Apache Airflow Final Assignment',
)

# define the task to to extract data from csv file

extract_data= BashOperator(
    task_id='extract_data_from_csv',
    bash_command='echo "Extract Mahesh"',
    dag=dag,
)

transform_data= BashOperator(
    task_id='transform_data',
    bash_command='echo "Transform Mahesh"',
    dag=dag,
)


virtualenv_task = PythonVirtualenvOperator(
    task_id="virtualenv_python",
    python_callable=callable_virtualenv,
    requirements=["colorama==0.4.0"],
    system_site_packages=False,
    dag=dag,
)

extract_data >> transform_data >> virtualenv_task