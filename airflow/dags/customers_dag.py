from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from utils.db import db_engine_source, db_engine_destination
import re


def get_customers():
    with open('sql/customers.sql') as file:
        query = file.read()
    df = db_engine_source(query)
    return df

def clean_customers_data():
    df = get_customers()
    df.rename(columns=['job': 'job_title'], inplace=True)
    return df

def save_cleaned_customers_data():
    df = clean_customers_data()
    db_engine_destination(df, 'customers')


    