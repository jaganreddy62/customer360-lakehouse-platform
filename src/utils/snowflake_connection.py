import yaml
import snowflake.connector


def get_connection():

    with open(
        "configs/snowflake_config.yaml",
        "r"
    ) as file:

        cfg = yaml.safe_load(file)

    conn = snowflake.connector.connect(
        account=cfg["account"],
        user=cfg["user"],
        password=cfg["password"],
        warehouse=cfg["warehouse"],
        database=cfg["database"],
        schema=cfg["schema"],
        role=cfg["role"]
    )

    return conn