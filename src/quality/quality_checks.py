import pandas as pd


def check_null_customer_ids(df):

    failed = df["CUSTOMER_ID"].isnull().sum()

    return failed


def check_duplicate_customers(df):

    failed = df.duplicated(
        subset=["CUSTOMER_ID"]
    ).sum()

    return failed