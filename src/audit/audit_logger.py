from datetime import datetime

from src.utils.snowflake_connection import get_connection


def log_pipeline_run(
    pipeline_name,
    record_count,
    status,
    error_message=None
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
    f"""
    INSERT INTO PIPELINE_AUDIT
    VALUES
    (
      '{pipeline_name}',
      CURRENT_TIMESTAMP(),
      CURRENT_TIMESTAMP(),
      {record_count},
      '{status}',
      '{error_message}'
    )
    """
    )

    conn.commit()