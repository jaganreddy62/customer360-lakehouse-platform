def transform_customers(df):

    df.columns = [
        col.upper()
        for col in df.columns
    ]

    df = df.drop_duplicates()

    return df