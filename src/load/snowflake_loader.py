from src.utils.snowflake_connection import get_connection


def load_dataframe(df, table_name):

    conn = get_connection()

    cursor = conn.cursor()

    for _, row in df.iterrows():

        values = tuple(row)

        placeholders = ",".join(
            ["%s"] * len(values)
        )

        sql = f"""
        INSERT INTO {table_name}
        VALUES ({placeholders})
        """

        cursor.execute(sql, values)

    conn.commit()

    cursor.close()

    conn.close()