import yaml


def get_sources():

    with open(
        "configs/source_metadata.yaml"
    ) as f:

        cfg = yaml.safe_load(f)

    return cfg["sources"]