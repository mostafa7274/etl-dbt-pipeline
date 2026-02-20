import pandas as pd

def extract():
    data = {
        "id": [1, 2, 3],
        "name": ["Ali", "Sara", "Omar"],
        "sales": [100, 250, 175]
    }
    return pd.DataFrame(data)

def transform(df):
    df["sales_with_tax"] = df["sales"] * 1.14
    return df

def load(df):
    df.to_csv("data/output.csv", index=False)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
    print("ETL Finished Successfully")