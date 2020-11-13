"""Pipeline

@author: vasudevgupta
"""

from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

# from scrapper import Scrapper

default_args= {
    'owner': 'Vasudev Gupta',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 29),
    'email': ['7vasudevgupta@gmail.com'],
    'retries': 2,
    'email_on_failure': True,
}

dag = DAG('arxiv-papers', default_args=default_args, 
          description='Pipeline for getting papers',
          schedule_interval=timedelta(minutes=1))

# scrapping_op = PythonOperator(task_id='scrap_data', 
#                                     python_callable=Scrapper().scrap_multiple_papers,
#                                     provide_context=True, 
#                                     op_kwargs={'max_papers': 10}, 
#                                     dag=dag)

email_op1 = EmailOperator(task_id='sending_email1',
                         to='7vasudevgupta@gmail.com', 
                         subject='hello1',
                         html_content='hello1',
                         dag=dag)


email_op2 = EmailOperator(task_id='sending_email2',
                         to='7vasudevgupta@gmail.com', 
                         subject='hello2',
                         html_content='hello2',
                         dag=dag)

email_op2 >> email_op1