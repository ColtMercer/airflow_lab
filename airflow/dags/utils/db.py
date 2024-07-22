import psycopg2
import pandas as pd


def db_engine_source(query):
    conn = psycopg2.connect(
        host="postgres",
        database="sample_data_source",
        user="devuser",
        password="devpasswd"
    )
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def db_engine_destination(data, table_name):
    conn = psycopg2.connect(
        host="postgres",
        database="sample_tableau",
        user="devuser",
        password="devpasswd"
    )
    # upsert data into table specified
    query = f"INSERT INTO {table_name} VALUES %s"