def copy_into_table(
    file_name,
    table_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        f"""
        PUT file://{file_name}
        @customer_stage
        OVERWRITE=TRUE
        """
    )

    cursor.execute(
        f"""
        COPY INTO {table_name}
        FROM @customer_stage
        FILE_FORMAT=(TYPE=CSV)
        """
    )

    conn.commit()