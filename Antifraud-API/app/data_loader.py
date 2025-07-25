import pandas as pd 
import requests
import io 

CSV_URL = "https://gist.githubusercontent.com/cloudwalk-tests/76993838e65d7e0f988f40f1b1909c97/raw/295d9f7cb8fdf08f3cb3bdf1696ab245d5b5c1c9/transactional-sample.csv"


def load_data():
    response = requests.get(CSV_URL)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text), parse_dates=["transaction_date"])
    df["has_cbk"] = df["has_cbk"].astype(bool)
    return df

