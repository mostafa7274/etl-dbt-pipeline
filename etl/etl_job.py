import pandas as pd
from sqlalchemy import create_engine

def extract():
    df = pd.read_csv("data/customers.csv")
    return df

def load(df):
    engine = create_engine(
    "postgresql://postgres:postgres@postgres:5432/postgres"
)
    df.to_sql("raw_customers", engine, if_exists="replace", index=False)
    print("Data loaded into Postgres!")

if __name__ == "__main__":
    data = extract()
    load(data)