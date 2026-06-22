import yaml

from src.extract.customer_extractor import (
    extract_customers
)

from src.transform.customer_transform import (
    transform_customers
)

from src.load.snowflake_loader import (
    load_dataframe
)


def run():

    with open(
        "configs/source_metadata.yaml"
    ) as file:

        metadata = yaml.safe_load(file)

    customer_cfg = metadata["sources"]["customers"]

    df = extract_customers(
        customer_cfg["source_file"]
    )

    df = transform_customers(df)

    load_dataframe(
        df,
        customer_cfg["target_table"]
    )


if __name__ == "__main__":
    run()