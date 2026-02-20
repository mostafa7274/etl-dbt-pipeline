import pandas as pd

def extract():
    print("Reading CSV file...")
    df = pd.read_csv("data/customers.csv")
    return df

def transform(df):
    print("Transforming data...")
    # Example transformation
    df["customer_name"] = df["customer_name"].str.upper()
    return df

def load(df):
    print("Final Data:")
    print(df)

if __name__ == "__main__":
    data = extract()
    data = transform(data)
    load(data)