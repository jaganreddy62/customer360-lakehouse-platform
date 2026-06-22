import pandas as pd


def extract_customers(file_path):

    df = pd.read_csv(file_path)

    return df