import pandas as pd

from src.utils.snowflake_connection import (
    get_connection
)


def run_query(sql):

    conn = get_connection()

    df = pd.read_sql(sql, conn)

    conn.close()

    return df